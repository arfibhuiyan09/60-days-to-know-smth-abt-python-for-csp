import pygame
import time
import random
from pathlib import Path

pygame.mixer.init()


BASE_DIR = Path(__file__).resolve().parent

ttatm = [ 
    str(BASE_DIR / "2_thealbum_themovie" / "i am the 2.wav"),
    str(BASE_DIR / "2_thealbum_themovie" / "i am the 2 part 2….wav"),
    str(BASE_DIR / "2_thealbum_themovie" / "bœwœißt_-_the_1st_edition_KLICKAUD.wav"),
    str(BASE_DIR / "2_thealbum_themovie" / "buddy holly lick w_ 32 instruments-674408712.wav"),
    str(BASE_DIR / "2_thealbum_themovie" / "coca_cola_-_parody_of_the_strokes.wav"),
    str(BASE_DIR / "2_thealbum_themovie" / "Duaduaoauaudua!.wav"),
    str(BASE_DIR / "2_thealbum_themovie" / "Eins, Zwei, Drei, Vier, Fünf, Sechs, Sieben, Acht!.wav"),
    str(BASE_DIR / "2_thealbum_themovie" / "good morning bob!.wav"),
    str(BASE_DIR / "2_thealbum_themovie" / "27.wav"),
    str(BASE_DIR / "2_thealbum_themovie" / "My Song 87.wav"),
    str(BASE_DIR / "2_thealbum_themovie" / "pipa + fx.wav"),
    str(BASE_DIR / "2_thealbum_themovie" / "the noise of the great awakening.wav"),
    str(BASE_DIR / "2_thealbum_themovie" / "wonkykoanbeats.wav"),
    str(BASE_DIR / "2_thealbum_themovie" / "the_boreen.wav"),
    str(BASE_DIR / "2_thealbum_themovie" / "ι.wav"),
]

li = [
    str(BASE_DIR / "li" / "1.mp3"),
    str(BASE_DIR / "li" / "2 (3).mp3"),
    str(BASE_DIR / "li" / "3 (1).mp3"),
    str(BASE_DIR / "li" / "4.mp3"),
    str(BASE_DIR / "li" / "5.mp3"),
    str(BASE_DIR / "li" / "6.mp3"),
    str(BASE_DIR / "li" / "7？.mp3"),
    str(BASE_DIR / "li" / "8.mp3"),
    str(BASE_DIR / "li" / "9.mp3"),
    str(BASE_DIR / "li" / "Micheal J.R.mp3"),
    str(BASE_DIR / "li" / "ι (1).mp3"),
    str(BASE_DIR / "li" / "λ.mp3"),
]

lfst = [
    str(BASE_DIR / "lfst" / "good morning bob! (1).mp3"),
    str(BASE_DIR / "lfst" / "las_r.mp3"),
    str(BASE_DIR / "lfst" / "the böreen.mp3"),
    str(BASE_DIR / "lfst" / "the las_r asylum.mp3"),
    str(BASE_DIR / "lfst" / "the noise of the great awakening (1).mp3"),
    str(BASE_DIR / "lfst" / "wadenos.mp3"),
]

unreleased = [
    str(BASE_DIR / "unreleased" / "arfibhuiyan09 + 3 stringed uke.mp3"),
    str(BASE_DIR / "unreleased" / "dirf.mp3"),
    str(BASE_DIR / "unreleased" / "HELP.mp3"),
    str(BASE_DIR / "unreleased" / "make this into song pls.mp3"),
    str(BASE_DIR / "unreleased" / "Record (online-voice-recorder.com) (9).mp3"),
    str(BASE_DIR / "unreleased" / "use code zackydaddy in the Fortnite item shop.mp3"),
    str(BASE_DIR / "unreleased" / "voices.mp3"),
    str(BASE_DIR / "unreleased" / "yes.mp3")
]

def play(playlist):
    random.shuffle(playlist)
    for song in playlist:
        print(f"Playing: {Path(song).name}")

        pygame.mixer.music.load(song)
        volume = 0.7
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play()
        

        while pygame.mixer.music.get_busy():
            cmd = input("Press Enter to skip, or X to lower, and Z to increase the volume: ").lower()

            if cmd == "":
                break
            elif cmd == "x":
                if volume <= 0:
                    print(f"--> Error: the volume is at the max it could be, which is {volume}!")
                    continue
                else:
                    volume = round(volume - 0.1, 1)
                    pygame.mixer.music.set_volume(volume)
                    print(f"The player is now at {volume}")
                    continue
            elif cmd == "z":
                if volume >= 1:
                    print(f"--> Error: the volume is at the max it could be, which is {volume}!")
                    continue
                else:  
                    volume = round(volume + 0.1, 1)
                    pygame.mixer.music.set_volume(volume)
                    print(f"The player is now at {volume}")
            else:
                print(f"--> Error: '{cmd}' is an invalid prompt answer!")

    print("All songs finished.")

while True:
    choice = input("which album by Azizur Bhuiyan℗ do you want to play? ('2: The Album, The Movie', 'li', 'lfst', 'unreleased') ").lower()
    if choice == "2: the album, the movie":
        play(ttatm)
    elif choice == "li":
        play(li)
    elif choice == "lfst":
        play(lfst)
    elif choice == "unreleased":
        play(unreleased)
    else:
        print(f"--> Error: '{choice}' is an invalid prompt answer!")