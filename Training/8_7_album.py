def make_album(artist_name, album_title, number_of_songs=''):
    if number_of_songs:
        album = f"Artist: {artist_name.title()} \nAlbum: {album_title.title()} \nNumber of songs: {number_of_songs}\n"
    else:
        album = f"Artist: {artist_name.title()} \nAlbum: {album_title.title()}\n"
    return album


full_album = make_album('lady gaga', 'poker face', '13')
print(full_album)

full_album = make_album('metallica', 'ride the lightening')
print(full_album)