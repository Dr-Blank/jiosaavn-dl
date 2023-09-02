# jiosaavn-dl
# made by bunny

import argparse
import os

from config import ARCHIVE_DIR, DOWNLOAD_DIR
from handler import Jiosaavn


logo = """
           /$$            /$$$$$$                                                         /$$ /$$
          |__/           /$$__  $$                                                       | $$| $$
       /$$ /$$  /$$$$$$ | $$  \__/  /$$$$$$   /$$$$$$  /$$    /$$ /$$$$$$$           /$$$$$$$| $$
      |__/| $$ /$$__  $$|  $$$$$$  |____  $$ |____  $$|  $$  /$$/| $$__  $$ /$$$$$$ /$$__  $$| $$
       /$$| $$| $$  \ $$ \____  $$  /$$$$$$$  /$$$$$$$ \  $$/$$/ | $$  \ $$|______/| $$  | $$| $$
      | $$| $$| $$  | $$ /$$  \ $$ /$$__  $$ /$$__  $$  \  $$$/  | $$  | $$        | $$  | $$| $$
      | $$| $$|  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$   \  $/   | $$  | $$        |  $$$$$$$| $$
      | $$|__/ \______/  \______/  \_______/ \_______/    \_/    |__/  |__/         \_______/|__/
 /$$  | $$                                                                                       
|  $$$$$$/                                                                             --by bunny, Dr.B
 \______/                                                                                        
"""


def clear() -> None:
    """Clears The Console Of All Text"""
    os.system("clear" if os.name == "posix" else "cls")


def main():
    """accepts the url and calls the appropriate function"""
    clear()
    print(logo)

    parser = argparse.ArgumentParser(
        description="Downloads songs/albums/playlist from JioSaavn"
    )
    parser.add_argument("url", help="Song/album/playlist URL")
    # add an argument for output directory
    parser.add_argument("-o", "--output", help="Output directory")
    parser.add_argument("-a", "--archive-dir", help="archive directory")
    args = parser.parse_args()

    url = args.url
    out_dir = args.output if args.output else DOWNLOAD_DIR
    archive_dir = args.archive_dir if args.archive_dir else ARCHIVE_DIR

    # create the output directory if it doesn't exist
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # create the archive directory if it doesn't exist
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # create the archive files if it doesn't exist
    archive_files = {}
    for cat in ["song", "album", "playlist", "artist"]:
        archive_file = os.path.join(archive_dir, f"{cat}.txt")
        if not os.path.exists(archive_file):
            with open(archive_file, "w", encoding="utf-8") as f:
                f.write("")
        archive_files[cat] = archive_file

    jiosaavn = Jiosaavn()

    jiosaavn.processUrl(url, out_dir, archive_files)


if __name__ == "__main__":
    main()
