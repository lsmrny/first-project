fav_songs = []
print("Alright give me your favourite songs :), type 'done' when you are finished")
while True:
    song = input(f"Song #{len(fav_songs) + 1} : ")
    if song.lower() == "done":
        break
    fav_songs.append(song)

for song in fav_songs:
    print(f"{song} is playing on repeat right now")

#for replaying
replay = input("Wanna replay all of it again? (yes/no) ")
if replay.lower() == "yes":
    for song in fav_songs:
        print(f"{song} is still stuck inside ur head lmao")