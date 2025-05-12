# Music Downloader CLI

A simple **Python-based CLI** tool to download songs and playlists from YouTube/YouTube Music, convert them to MP3 with embedded metadata and cover art, and center-crop album artwork to a perfect square.

*Programmed by Muhammad Saaim*

---

## Features

* **Single Song** & **Playlist** download
* **Audio Extraction** to MP3 with `yt-dlp` and `ffmpeg`
* **Embedded Metadata**: title, artist, thumbnails
* **Cover Art Processing**: center-crop to 1:1 square via `Pillow` + `mutagen`
* **Download Archive** support: skip already-downloaded tracks in a playlist
* **Interactive Mode** or **Argument Mode**

## Requirements

* **Windows** (needs `yt-dlp.exe` & `ffmpeg.exe` bundled)
* **Python 3.8+**

### Python Dependencies

Install dependencies via `pip`:

```bash
pip install \
  mutagen \
  Pillow \
  eyed3 \
  yt-dlp
```

> **Note**: Lyrics fetching has been removed. Use separate LRC files with MusicBee for synced lyrics.

## Setup

1. **Clone** or **download** this repository.
2. **Place** the following executables in the project root (alongside `music_downloader.py`):

   * `yt-dlp.exe`
   * `ffmpeg\bin\ffmpeg.exe` (FFmpeg Windows build)
3. **(Optional)** Set environment variables for extra features:

   * `[Not used in this release]`

## Usage

### Interactive Mode

Run without arguments to launch the interactive menu:

```bash
python music_downloader.py
```

Follow prompts to download a single song or a playlist.

### Argument Mode

Download a single song:

```bash
python music_downloader.py song <URL> [-o OUTPUT_DIR]
```

Download a playlist (with optional archive skip):

```bash
python music_downloader.py playlist <URL> [-o OUTPUT_DIR] [--archive ARCHIVE_PATH]
```

* **`-o, --out`**: Output directory (defaults to current folder)
* **`--archive`**: Path to a download archive file or directory (will use `downloaded.txt` inside)

## Packaging

To create a standalone Windows executable, use **PyInstaller**:

```bash
pip install pyinstaller
pyinstaller --onefile \
  --add-binary "yt-dlp.exe;." \
  --add-binary "ffmpeg\\bin\\ffmpeg.exe;ffmpeg\\bin" \
  music_downloader.py
```

The generated `dist/music_downloader.exe` will include `yt-dlp` and `ffmpeg`.

## Recommended Player

Use [MusicBee](https://getmusicbee.com/) for the best listening experience, including support for **embedded LRC lyrics** and **custom artwork display**.

---

**Thank you for using Music Downloader CLI!**

*Program by Muhammad Saaim*
