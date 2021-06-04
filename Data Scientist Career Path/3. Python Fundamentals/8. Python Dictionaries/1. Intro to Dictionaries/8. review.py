songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for song,playcount in zip(songs, playcounts)}

print(plays)

plays.update({"Purple Haze":1})

plays.update({"Respect":94})

library = {"The Best Songs":plays, "Sunday Feelings":{}}

print(library)