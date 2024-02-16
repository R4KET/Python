players = ['Karol', 'Martyna', 'Michal' ,'John','Wojciech','Ela']
print(players[4:]) # od 4 do konca
print(players[:4]) # od poczatku do 4
print(players[-3:]) # od 3 od konca do konca

print("Oto pierwszych trzech graczy naszej druzyny:")
for player in players[:3]:
    print(player.title())