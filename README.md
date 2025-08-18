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
MIT License

Copyright (c) 2025 Tommaso Buzzolan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.```
