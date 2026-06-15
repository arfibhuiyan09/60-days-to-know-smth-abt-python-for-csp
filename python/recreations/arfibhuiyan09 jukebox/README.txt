the audio files are too big itself to upload to github and so to access the audio folders, go to the following google drive links and download each of them individually:

2: The Album, The Movie (TTATM) --> https://drive.google.com/drive/folders/1ihTKHtdG4y1e0-55W8ebSEJnYCN5lTqk?usp=sharing <--
light fabricated sound technician (lfst) --> https://drive.google.com/drive/folders/1vZaop2-34WLf-bPwQT0526jV2_e5AcW1?usp=sharing <--
le idot (li) -> https://drive.google.com/drive/folders/1q1_woAKjZDtv8uEZKCtrWKdcSSY4gefu?usp=sharing <--
unreleased --> https://drive.google.com/drive/folders/1NVuhRMDjVknbih5PBYTYVIqFHBzxMLF6?usp=drive_link <--


SETUP INSTRUCTIONS

1. Install Python and Pygame:
   pip install pygame

2. Download all audio files from the Google Drive folder (if you havent already)

3. Place the Python script and audio folders in the same directory:

   project_folder/
   ├── p.18.py
   ├── 2_thealbum_themovie/
   ├── li/
   ├── lfst/
   └── unreleased/

4. Do NOT rename any folders or audio files.
   The filenames must match exactly, including spaces,
   symbols, accents, and capitalization.

5. Run the script:
   python p18.py

TROUBLESHOOTING

• "No file found" error:
  - Verify all folders are present.
  - Verify no files were renamed.
  - Verify the script is in the same folder as the album folders.

• Audio does not play:
  - Make sure Pygame is installed.
  - Confirm your computer audio is working.
  - Try opening the audio files manually.

• Unicode filename errors:
  - Re-download the original files.
  - Avoid changing special characters in filenames.

• If the program crashes immediately:
  - Run it from a terminal/command prompt and read the error message.
