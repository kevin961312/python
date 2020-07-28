song_library = [("Phantom of The Opera", "Sarah Brightman"),
("Knocking On Heaven's Door", "Guns N' Roses"),
 ("Captain Nemo", "Sarah Brightman"),
 ("Patterns In The Ivy", "Opeth"),
 ("November Rain", "Guns N' Roses"),
 ("Beautiful", "Sarah Brightman"),
 ("Mal's Song", "Vixy and Tony")]
artists = set()
for song, artist in  song_library:
    artists.add(artist) 

print(artists)
print('Opeth' in artists)
for artist in artists:
    print("{} plays good music".format(artist))

alphabetical = list(artists)
alphabetical.sort()
print(alphabetical)

my_artists = {"Sarah Brightman", "Guns N' Roses","Opeth", "Vixy and Tony"}
auburns_artists = {"Nickelback", "Guns N' Roses","Savage Garden"}

print("All: {}".format(my_artists.union(auburns_artists)))
print("Both: {}".format(auburns_artists.intersection(my_artists)))
print("Either but not both: {}".format( my_artists.symmetric_difference(auburns_artists)))

my_artists = {"Sarah Brightman", "Guns N' Roses","Opeth", "Vixy and Tony"}
bands = {"Guns N' Roses", "Opeth"}
print("my_artists is to bands:")
print("issuperset: {}".format(my_artists.issuperset(bands)))
print("issubset: {}".format(my_artists.issubset(bands)))
print("difference: {}".format(my_artists.difference(bands)))
print("*"*20)
print("bands is to my_artists:")
print("issuperset: {}".format(bands.issuperset(my_artists)))
print("issubset: {}".format(bands.issubset(my_artists)))
print("difference: {}".format(bands.difference(my_artists)))