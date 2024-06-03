from tabulate import tabulate

def search_song(data):
    search_theme = input("Enter title of the song: ")
    data["Duration_min"] = data["Duration_ms"].apply(lambda x: '{:02}:{:02}'.format(x // 60000, (x // 1000) % 60))
    result = data[data["Title"].str.contains(search_theme, case=False, na=False)]    
    result = result.sort_values(by="Views", ascending=False)
    
    result_table = tabulate(result[["Artist", "Title", "Duration_min", "Views"]], headers="keys", tablefmt="pretty", showindex=False)
    print(result_table)