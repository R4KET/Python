albums = {}

def make_album(artist_name, album_title, number_of_songs=''):
    if number_of_songs:
        album = f"Album: {album_title.title()} \nNumber of songs: {number_of_songs}\n"
    else:
        album = f"Album: {album_title.title()}\n"
    return album

polling_active = True

while polling_active:
    artist_name = input("\nWhat's the artist's name? ")
    album_title = input("What's the album's name? ")
    number_of_songs = input("How many songs are in the album? ")

    album_info = make_album(artist_name, album_title, number_of_songs)
    albums[artist_name] = album_info

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for artist, album_info in albums.items():
    print(f"Artist: {artist.title()}\n{album_info}")
