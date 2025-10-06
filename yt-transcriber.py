import os
import yt_dlp
import whisper
import re
import sys

# ---- CONFIG ----
URL = "https://www.youtube.com/watch?v=KAwCm-d7980&t=6s"  # replace with your podcast URL
OUTPUT_AUDIO = "03_10-Nel_fango_del_dio_AI.mp3"
OUTPUT_TRANSCRIPT = "03_10-Nel_fango_del_dio_AI_transcript.txt"
MODEL = "small"  # tiny, base, small, medium, large

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

def download_audio(url, output_file):
    """Download best audio using yt-dlp"""
    print("[INFO] Downloading audio...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_file,
        'noplaylist': True,  # Download only the single video, not the playlist
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("[INFO] Audio downloaded:", output_file)

def transcribe_audio(audio_file, model_name, transcript_file):
    """Transcribe audio with Whisper"""
    print("[INFO] Loading Whisper model:", model_name)
    model = whisper.load_model(model_name)
    print("[INFO] Transcribing...")
    result = model.transcribe(audio_file)
    
    return  result  # Return the result for further processing

if __name__ == "__main__":
    ffmpeg_path = os.path.join(os.getcwd(), "ffmpeg", "bin")
    os.environ["PATH"] += os.pathsep + ffmpeg_path
    url = sys.argv[1]
    download_audio(url, OUTPUT_AUDIO)
    result = transcribe_audio(OUTPUT_AUDIO, MODEL, OUTPUT_TRANSCRIPT)
    
    # Process the transcription result
    transcript_text = result["text"]  # Whisper output
    formatted_text = format_transcript(transcript_text)

    with open(OUTPUT_TRANSCRIPT, "w", encoding="utf-8") as f:
        f.write(formatted_text)
    
    print("[INFO] Transcript saved in readable format as transcript.txt")
