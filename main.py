import pandas as pd, os, time, pathlib, csv, re
from point1 import search_song
from point2 import search_artist
from point3 import add_new_song
from point4 import top_artists
import options

os.system('cls')
print(f"{options.BLUE}Reading File...")
# Ruta Augusto
data = pd.read_csv("spotify_and_youtube 2024.csv")

def parse_csv() -> list:
    songs = []
    try:
        with open(f"{pathlib.Path(__file__).parent.absolute()}/spotify_and_youtube 2024.csv", 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            for row in csv_reader:
                song = SongDto(
                    row['Index'],
                    row['Artist'],
                    row['Url_spotify'],
                    row['Track'],
                    row['Album'],
                    row['Album_type'],
                    row['Uri'],
                    row['Danceability'],
                    row['Energy'],
                    row['Key'],
                    row['Loudness'],
                    row['Speechiness'],
                    row['Acousticness'],
                    row['Instrumentalness'],
                    row['Liveness'],
                    row['Valence'],
                    row['Tempo'],
                    row['Duration_ms'],
                    row['Url_youtube'],
                    row['Title'],
                    row['Channel'],
                    row['Views'],
                    row['Likes'],
                    row['Comments'],
                    row['Licensed'],
                    row['official_video'],
                    row['Stream'],
                )
                songs.append(song)
        return songs
    except (FileNotFoundError):
        print('File not found')
        exit(1)

while True:
    print(f"{options.BLUE}")
    print("Options Menu:")
    print("1. Search Song")
    print("2. Search Artist")
    print("3. Add New Song")
    print("4. Top 10 artists with most views")
    print("5. Exit")
    print(f"{options.RESET}")

    option = input("Select an option: ")

    if option == "1":
        print(f"{options.GREEN}")
        search_song(data)
        print(f"{options.RESET}")
        time.sleep(3)
    elif option == "2":
        print(f"{options.GREEN}")
        search_artist(data)
        print(f"{options.RESET}")
        time.sleep(3)
    elif option == "3":
        print(f"{options.GREEN}")
        add_new_song(data)
        print(f"{options.RESET}")
        time.sleep(3)
    elif option == "4":
        print(f"{options.GREEN}")
        top_artists(data)
        print(f"{options.RESET}")
        time.sleep(3)
    elif option == "5":
        break
    else:
        print("Invalid Option. Try Again")
        time.sleep(3)