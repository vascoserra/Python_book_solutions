def make_album(artist, album_title, number_songs=None):
    album = {'musician': artist, 'title': album_title}
    if number_songs:
        album['number of songs:'] = number_songs
    return album


while True:
    musician = input("\nName a musician: ")
    album = input("Name of the album: ")
    final = make_album(musician, album)
    print(f"{final}")
    break
