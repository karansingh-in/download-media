# Download-media

(still in development, having some issue with ffmpeg will fix it later)

Download media (videos/audio) via a simple web interface.

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

## Demo

Live demo available at:  
[download-media-alpha.vercel.app](https://download-media-alpha.vercel.app)

## Features

- Easily download media (videos or audio) from supported sources.
- Minimal, responsive HTML/CSS/JavaScript frontend.
- Lightweight backend Python,flask.
- Consistent styling using provided icons and templates.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, flask   
- **Assets & Structure**:
  - `icons/` – UI icons.
  - `templates/` – HTML templates.
  - `ffmpeg_file` – Utility or script for media processing (e.g., using FFmpeg).
  - `.gitattributes`, `.gitignore`, plus a utility note `fixing git lfs in terminal.txt`.

## Installation & Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/karansingh-in/download-media.git
   cd download-media