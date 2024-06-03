import pandas as pd
from tabulate import tabulate

def search_artist(data):
    search_artist = input("Enter the name of the artist: ")
    result = data[data["Artist"].str.contains(search_artist, case=False, na=False)]
    result = result.sort_values(by="Views", ascending=False)
    top_10 = result.head(10)
    top_10["Duration"] = top_10["Duration_ms"].apply(lambda x: '{:02}:{:02}:{:02}'.format(x // 3600000, (x // 60000) % 60, (x // 1000) % 60))
    top_10["Views (millions)"] = top_10["Views"] / 1_000_000

    result_table = top_10[["Artist", "Title", "Duration", "Views (millions)"]]
    print(tabulate(result_table, headers="keys", tablefmt="pretty", showindex=False))


