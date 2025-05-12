#!/usr/bin/env python3
"""
Music Downloader CLI (Interactive)

Features:
 - Download single song or playlist via bundled yt-dlp
 - Convert to MP3, embed metadata & cover art via bundled ffmpeg
 - Center-crop covers to 1:1 square via Pillow + Mutagen
 - Maintain download archive for playlists

Note: Lyrics embedding removed. Use LRC files separately.

Usage:
 - Place this script alongside yt-dlp.exe and the ffmpeg/bin/ffmpeg.exe folder.
 - Run: python music_downloader.py
"""
import os
import io
import sys
import subprocess
from pathlib import Path
from mutagen.id3 import ID3, APIC
from mutagen.id3 import ID3NoHeaderError
from PIL import Image

# Determine the bundle/runtime folder (supports PyInstaller)
APP_DIR = getattr(sys, "_MEIPASS", Path(__file__).parent.resolve())
YTDLP_EXE = Path(APP_DIR) / "yt-dlp.exe"
FFMPEG_EXE = Path(APP_DIR) / "ffmpeg" / "bin" / "ffmpeg.exe"

def run_cmd(cmd):
    """Run a subprocess and abort on failure."""
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print(f"❌ Command failed: {' '.join(cmd)}")
        sys.exit(1)

def download_song(url, out_dir):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(YTDLP_EXE),
        "--ffmpeg-location", str(FFMPEG_EXE),
        "--extract-audio", "--audio-format", "mp3",
        "--embed-metadata", "--embed-thumbnail", "--add-metadata",
        "-o", str(out / "%(title)s.%(ext)s"),
        url
    ]
    run_cmd(cmd)

def download_playlist(url, out_dir, archive_path=None):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(YTDLP_EXE),
        "--ffmpeg-location", str(FFMPEG_EXE),
        "--extract-audio", "--audio-format", "mp3",
        "--embed-metadata", "--embed-thumbnail", "--add-metadata"
    ]
    if archive_path:
        cmd += ["--download-archive", str(archive_path)]
    cmd += [
        "-o", str(out / "%(playlist_title)s" / "%(playlist_index)s - %(title)s.%(ext)s"),
        url
    ]
    run_cmd(cmd)

def crop_cover(mp3_file: Path):
    """Center-crop embedded APIC cover to square."""
    try:
        tags = ID3(mp3_file)
    except ID3NoHeaderError:
        return
    apics = tags.getall("APIC")
    if not apics:
        return
    apic = apics[0]
    img = Image.open(io.BytesIO(apic.data))
    w, h = img.size
    if w == h:
        return
    left = (w - h) // 2
    square = img.crop((left, 0, left + h, h))
    bio = io.BytesIO()
    square.save(bio, format="JPEG")
    tags.delall("APIC")
    tags.add(APIC(
        encoding=apic.encoding, mime=apic.mime,
        type=apic.type, desc=apic.desc,
        data=bio.getvalue()
    ))
    tags.save(v2_version=3)

def process_directory(directory):
    for mp3 in Path(directory).rglob("*.mp3"):
        print(f"🔧 Processing cover for {mp3.name}")
        crop_cover(mp3)

def interactive_menu():
    print("=== Music Downloader CLI ===")
    choice = input("[1] Song  [2] Playlist: ").strip()
    if choice == "1":
        url = input("Enter song URL: ").strip()
        out = input("Output dir [default .]: ").strip() or "."
        download_song(url, out)
        process_directory(out)
    elif choice == "2":
        url = input("Enter playlist URL: ").strip()
        out = input("Output dir [default .]: ").strip() or "."
        is_new = input("New playlist? [y/n]: ").strip().lower() == "y"
        archive = None
        if not is_new:
            a = input("Archive file or folder: ").strip()
            p = Path(a)
            if p.is_dir():
                p = p / "downloaded.txt"
            p.parent.mkdir(parents=True, exist_ok=True)
            archive = p
        download_playlist(url, out, archive)
        process_directory(out)
    else:
        print("❌ Invalid selection.")

def main():
    if len(sys.argv) == 1:
        interactive_menu()
    else:
        import argparse
        parser = argparse.ArgumentParser(prog="musicdl")
        subs = parser.add_subparsers(dest="cmd", required=True)
        s1 = subs.add_parser("song");    s1.add_argument("url"); s1.add_argument("-o","--out",default=".")
        s2 = subs.add_parser("playlist");s2.add_argument("url"); s2.add_argument("-o","--out",default="."); s2.add_argument("--archive")
        args = parser.parse_args()
        if args.cmd == "song":
            download_song(args.url, args.out); process_directory(args.out)
        else:
            arch = Path(args.archive) if args.archive else None
            if arch and arch.is_dir():
                arch = arch / "downloaded.txt"
            if arch:
                arch.parent.mkdir(parents=True, exist_ok=True)
            download_playlist(args.url, args.out, arch)
            process_directory(args.out)

if __name__ == "__main__":
    main()

# USE LRC GET FOR LYRICS
# THANKS FOR USING OUR PROGRAM
# USE MUSICBEE FOR BEST EXPERIENCE
# PROGRAM BY MUHAMMAD SAAIM
