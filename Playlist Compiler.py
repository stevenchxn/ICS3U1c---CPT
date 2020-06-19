print ("Welcome to Steven's music compiler!")
print("")
primary_genres = {
    'hiphop':['Drake', 'Travis Scott', 'Post Malone', 'Kendrick Lamar', 'Lil Uzi Vert', 'Logic'], 
    'pop':['Justin Bieber', 'Ariana Grande', 'Ed Sheeran', 'Khalid'],
    'rock':['Led Zeppelin', 'AC/DC', 'The Beatles', 'Queen'],
    'rnb':['The Weeknd', 'Don Toliver', 'Bryson Tiller']
}

moods = ['happy', 'energetic', 'sad', 'calm']
songs_hiphop = {
    'happy':['iSpy(feat. Lil Yachty)', 'Broccoli(feat. Lil Yachty', 'Candy Paint', 'Lust'],
    'energetic':['$$$ (with Matt Ox)', 'Congratulations', 'Sanguine Paradise', 'New Patek', 'Black Spiderman'],
    'sad':['The Way Life Goes', 'Fake Love', 'Impossible', 'Jocelyn Flores', 'Never Been'],
    'calm':["Maria I'm drunk", 'Owe Me', 'Deja Vu', 'Myself']
}
songs_pop = {
    'happy':['Jackie Chan', 'Sunflower', "Can't Feel My Face", 'Everyday', 'Happy'],
    'energetic':['How Long', "Ain't No Mountain High Enough", 'Love Me Again', "I Don't Care"],
    'sad':['Perfect', 'Circles', 'everything i wanted'],
    'calm':['Signs', 'Japanese Denim', 'Time in a Bottle', 'thank u, next', 'Passionfruit']
}
songs_rock = {
    'happy':['Come Together', "Don't Stop Me Now", 'Walking on Sunshine'],
    'energetic':['Highway to Hell', 'Back in Black', 'Thunderstruck', 'Immigrant Song', 'Paint It Black'],
    'sad':['Let It Be', 'Yesterday', 'Hey Jude'],
    'calm':['Here Comes The Sun', 'Stairway to Heaven', 'Take It Easy']
}
songs_rnb = {
    'happy':['So High', "I Don't Want Your Love", 'Far From You'],
    'energetic':['THRU THE NIGHT', 'Crew', 'Coming Out Strong (feat. The Weeknd)'],
    'sad':['Halfway Off The Balcony', 'LOVE.FEAT.ZACARI', 'Nothings Into Somethings'],
    'calm':["Don't", 'Exchange', 'Best You Had', 'No Guidance', 'December (feat. Luca)']
}
artists = []
playlist = []
genre = []
def remove(string):
    return string.replace(" ", "")

def artist_compiler():
    print("    Genres: hiphop, pop, rock, rnb")
    print("")
    search1 = input("Enter a single music genre: ")
    print("")
    for i in primary_genres:
        if search1 == i:
            genre.append(i)
            for j in primary_genres[str(i)]:
                artists.append(j)
    if len(artists) > 0:
        print('Your recommended artists: ' + (str(', '.join(artists))))
        print("")
        song_compiler()
    else:
        print('Please enter a different genre')
        print("")
        artist_compiler()
    
def song_compiler():
    print("    Moods: happy, energetic, sad, calm")
    print("")
    search2 = input("Enter desired mood(s), seperate with commas: ")
    searchList = []
    search2 = remove(search2).split(",")
    searchList.extend(search2)
    for k in searchList:
        if genre == ['hiphop']:
            for i in songs_hiphop:
                if k == i:
                    for j in songs_hiphop[str(i)]:
                        playlist.append(j)
        elif genre == ['pop']:
            for i in songs_pop:
                if k == i:
                    for j in songs_pop[str(i)]:
                        playlist.append(j)
        elif genre == ['rock']:
            for i in songs_rock:
                if k == i:
                    for j in songs_rock[str(i)]:
                        playlist.append(j)
        elif genre == ['rnb']:
            for i in songs_rnb:
                if k == i:
                    for j in songs_rnb[str(i)]:
                        playlist.append(j)
    recommendations()

def recommendations():
    if len(playlist) > 0:
        print("")
        print('Your recommended songs: ' + (str(', '.join(playlist))))
    else:
        print("")
        print('Please enter a different mood')
        print("")
        song_compiler()
artist_compiler()