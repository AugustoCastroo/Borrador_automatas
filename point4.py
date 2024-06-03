import pandas as pd
from tabulate import tabulate

# def top_artists(data: pd.DataFrame) -> None:
#     artist_name = input("Enter the name of the artist: ")
#     albums = {}
#     for song in songs:
#         if artist.lower() in song.artist.lower():
#             artist = song.artist
#             if song.album in albums:
#                 albums[song.album] = (albums[song.album][0] + 1, albums[song.album][1] + float(song.duration))
#             else:
#                 albums[song.album] = (1, float(song.duration))
#     print(f"{artist} have {len(albums.keys())} albums:")
#     for album, songs_duration in albums.items():
#         print("\u2022", f"{album} have {songs_duration[0]} songs & time {time.strftime('%H:%M:%S', time.gmtime(songs_duration[1]/1000))}")


def top_artists(data):
    result = search_artist(data)

    top_10 = result.head(10)
    top_10["Duration"] = top_10["Duration_ms"].apply(lambda x: '{:02}:{:02}:{:02}'.format(x // 3600000, (x // 60000) % 60, (x // 1000) % 60))
    top_10["Views (millions)"] = top_10["Views"] / 1_000_000
    result_table = top_10[["Artist", "Title", "Duration", "Views (millions)"]]

    print(tabulate(result_table, headers="keys", tablefmt="pretty", showindex=False))

    albums_info = find_albums(result)
    print(albums_info)

def find_albums(data):
    albums = {}
    for index, song in data.iterrows():
        if song["Album"] in albums:
            albums[song["Album"]]["number_of_songs"] += 1
            albums[song["Album"]]["duration_ms"] += song["Duration_ms"]
        else:
            albums[song["Album"]] = {
                "number_of_songs": 1,
                "duration_ms": song["Duration_ms"]
            }
    albums_info = f"{data['Artist'].iloc[0]} has {len(albums)} albums:\n"
    for album, info in albums.items():
        album_duration = '{:02}:{:02}:{:02}'.format(info["duration_ms"] // 3600000, (info["duration_ms"] // 60000) % 60, (info["duration_ms"] // 1000) % 60)
        albums_info += f"\u2022 {album} has {info['number_of_songs']} songs & total duration {album_duration}\n"
    return albums_info

if __name__ == "__main__":
    display_top_artists(df)
