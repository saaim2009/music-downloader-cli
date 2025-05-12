# Music Downloader CLI

A simple **Python-based CLI** tool to download songs and playlists from YouTube/YouTube Music, convert them to MP3 with embedded metadata and cover art, and center-crop album artwork to a perfect square.

*Programmed by Muhammad Saaim*

---
📸 Screenshot
Below is an example of the Music Downloader CLI in action (run in your Windows Command Prompt):

![image](https://github.com/user-attachments/assets/f67f9b76-9d27-48a9-8c3e-49b89ce4215a)


## 📥 Download

You can download the **all-in-one ZIP package** (contains the compiled executable, `yt-dlp.exe`, and `ffmpeg` binaries) from our Release page:

https://drive.google.com/file/d/1k96JVCJwOjr-2_PjdT3hxuZkTfkTrtkU/

> ⚠️ **Note:** The ZIP is ≈400 MB because it includes FFmpeg and yt-dlp for broader use beyond this CLI.

Alternatively, if you prefer to use your own Python environment, you can download just the **`music_downloader.py`** script from the main branch and follow the Python setup below.

---

## 🔧 Features

* **Single Song** & **Playlist** download
* **Audio Extraction** to MP3 with `yt-dlp` & `ffmpeg`
* **Embedded Metadata**: title, artist, thumbnails
* **Cover Art Processing**: center-crop to 1:1 square via `Pillow` + `mutagen`
* **Download Archive** support: skip already-downloaded tracks in playlist
* **Interactive Mode** or **Argument Mode**

---

## ⚙️ Requirements

### For ZIP Package (Recommended)

* **Windows** (no Python required)
* Extract the ZIP and run the EXE directly

### For Python Script

* **Windows** or **macOS/Linux**
* **Python 3.8+** installed

#### Python Dependencies

Install via `pip`:

```bash
pip install mutagen Pillow eyed3 yt-dlp
```

> **Note:** Lyrics embedding has been removed. Use separate LRC files (e.g., in LRCGET) for synced lyrics.

---

## 🚀 Usage

### 1) Using the EXE (no setup)

1. Download the ZIP from the Release page.
2. Extract it.
3. Double-click `MusicDownloader.exe` to launch the interactive CLI.

### 2) Using the Python Script

1. Clone or download this repo.
2. Place `yt-dlp.exe` and the `ffmpeg/bin/ffmpeg.exe` folder alongside `music_downloader.py`.
3. Install dependencies (see above).
4. Run:

   ```bash
   python music_downloader.py        # interactive mode
   python music_downloader.py song <URL>      # single song
   python music_downloader.py playlist <URL> [--archive PATH]  # playlist
   ```

---

## ⚠️ Disclaimer & Feedback

This program is **not** fully developed. Use at your own risk; we are **not responsible** for any misuse or policy violations.

**Suggestions and contributions** are very welcome! Feel free to open issues or pull requests on GitHub.

---

**Thank you for trying Music Downloader CLI!**

*Program by Muhammad Saaim*
