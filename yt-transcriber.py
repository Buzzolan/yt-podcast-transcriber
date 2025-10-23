from datetime import datetime
import os
import yt_dlp
import whisper
import re
import sys

# ---- CONFIG ----
MODEL = "small"  # tiny, base, small, medum, large

def sanitize_filename(name):
    """Clean video title for safe filenames."""
    return re.sub(r"[\\/*?:<>'|]", "_", name).strip()

def format_transcript(text, max_words_per_line=14):
    """
    Format transcript in readable paragraphs.
    - Breaks text into sentences using punctuation.
    - Limits number of words per line for readability.
    """
    # Step 1: Split into sentences (punto, esclamativo, interrogativo)
    sentences = re.split(r'(?<=[.!?])\s+', text)

    # Step 2: Break each sentence into lines of max_words_per_line
    formatted_lines = []
    for sentence in sentences:
        words = sentence.split()
        for i in range(0, len(words), max_words_per_line):
            line = " ".join(words[i:i+max_words_per_line])
            formatted_lines.append(line)
        formatted_lines.append("")  # empty line between sentences/paragraphs

    return "\n".join(formatted_lines)

def get_video_title(url):
    """Fetch video title without downloading."""
    ydl_opts = {'quiet': True, 'skip_download': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get("title", "untitled")

def download_audio(url, output_file):
    """Download best audio using yt-dlp"""
    print("[INFO] Downloading audio...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_file,
        'noplaylist': True,  # Download only the single video, not the playlist
        'extractor_args': {'youtube': {'player_client': ['android']}}
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("[INFO] Audio downloaded:", output_file)

def transcribe_audio(audio_file, model_name):
    """Transcribe audio with Whisper"""
    print("[INFO] Loading Whisper model:", model_name)
    model = whisper.load_model(model_name)
    print("[INFO] Transcribing...")
    result = model.transcribe(audio_file)
    
    return  result  # Return the result for further processing

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <YouTube_URL>")
        sys.exit(1)

    url = sys.argv[1]

    # ensure ffmpeg is in PATH
    ffmpeg_path = os.path.join(os.getcwd(), "ffmpeg", "bin")
    os.environ["PATH"] += os.pathsep + ffmpeg_path

    # Prepare filenames
    today = datetime.now().strftime("%m-%d")
    title = get_video_title(url)
    safe_title = sanitize_filename(title)
    output_audio = f"{today}_{safe_title}.mp3"
    output_transcript = f"{today}_{safe_title}.txt"

    # Download audio and transcribe
    download_audio(url, output_audio)
    result = transcribe_audio(output_audio, MODEL)
    
    # Process the transcription result
    transcript_text = result["text"]  # Whisper output
    formatted_text = format_transcript(transcript_text)

    with open(output_transcript, "w", encoding="utf-8") as f:
        f.write(formatted_text)
    
    print(f"[INFO] Transcript saved as: {output_transcript}")
    print(f"[INFO] Audio saved as: {output_audio}")
