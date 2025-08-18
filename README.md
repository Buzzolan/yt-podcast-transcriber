# YouTube Podcast Transcriber

Download podcasts from YouTube and transcribe them automatically using **OpenAI Whisper**.

---

## Features

- Download audio from YouTube videos (supports single videos, ignores playlists by default)
- Transcribe audio with Whisper into readable text
- Automatically formats the transcript into paragraphs
- Fully local and portable (uses a local `ffmpeg` binary)
- MIT licensed

---

## Requirements

- Python 3.9+
- `yt-dlp` (`pip install yt-dlp`)
- `openai-whisper` (`pip install openai-whisper`)
- `ffmpeg` executable in PATH or in `ffmpeg/bin` folder

---

## Setup

1. Clone the repo:

```bash
git clone https://github.com/username/yt-podcast-transcriber.git
cd yt-podcast-transcriber
````

2. **Download FFmpeg**:

   * Go to [BtbN/FFmpeg-Builds](https://github.com/BtbN/FFmpeg-Builds/releases)
   * Download the latest Windows static build (zip)
   * Extract it and place the `bin` folder inside your project at `ffmpeg/bin`, or install FFmpeg system-wide and make sure `ffmpeg.exe` is in your PATH.

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Edit `main.py` and replace `URL` with your podcast URL.

5. Run the script:

```bash
python main.py
```

6. The transcript will be saved as `transcript.txt`, formatted in paragraphs.

---

## License

MIT License © 2025 Buzzolan

```
