#list of songs
songs = ["ROCKSTAR", "Do It", "For The Night"]
#prints songs from index 0 up to 2 not including 2
print(songs[0:2])

#changes the item in list at index 0
songs[0] = "Dynamite"

#prints list
print(songs)

#changes the item in list at inedex 2
songs[2] = "Circles"

#prints list
print(songs)

#adding 3 different songs in 3 different ways
songs.append("2009")
songs.extend(["Blinding Lights"])
songs.insert(0, "4k")

# deletes item from list at index 1
del songs[1]

#prints songs
print(songs)

#list of animals
animals = ["Cat", "Dog", "Bird"]

#adding an item to the animals list
animals.append("Chicken")

#print item from animals list at index 2
print(animals[2])

#deleting item from list at index 0
del animals[0]

#displaying all items from the list
for animal in animals:
    print(animal)