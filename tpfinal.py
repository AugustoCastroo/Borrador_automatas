import pandas as pd, os, time
import constants as const
from option1 import search_song
# from option2 import search_artist
# from option3 import add_song
# from option4 import top_artists

os.system('cls')
print(f"{const.BLUE}Reading File...")

data = pd.read_csv("C:/Users/acast/OneDrive/Documents/UM/2024/Automátas y Gramáticas/Borradores/spotify_and_youtube 2024.csv")

os.system('cls')
        
while True:
    print(f"{const.BLUE}")
    print("Options Menu:")
    print("1. Search Song")
    print("2. Search Artist")
    print("3. Add New Song")
    print("4. Top 10 artists with most views")
    print("5. Exit")
    print(f"{const.RESET}")

    option = input("Select an option: ")

    if option == "1":
        print(f"{const.GREEN}")
        search_song(data)
        print(f"{const.RESET}")
        time.sleep(3)
    elif option == "2":
        print(f"{const.GREEN}")
        search_artist(data)
        print(f"{const.RESET}")
        time.sleep(3)
    elif option == "3":
        print(f"{const.GREEN}")
        add_song(data)
        print(f"{const.RESET}")
        time.sleep(3)
    elif option == "4":
        print(f"{const.GREEN}")
        top_artists(data)
        print(f"{const.RESET}")
        time.sleep(3)
    elif option == "5":
        break
    else:
        print("Invalid Option. Try Again")
        time.sleep(3)
