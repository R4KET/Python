goscie = ['Jan', 'Anna', 'Wojciech', 'Pawel', 'John'];
print("Zapraszam na obiad, " + goscie[0] + "!");
print("Zapraszam na obiad, " + goscie[1] + "!");
print("Zapraszam na obiad, " + goscie[2] + "!");
print("Zapraszam na obiad, " + goscie[3] + "!");
print("Zapraszam na obiad, " + goscie[4] + "!");

print("Niestety, " + goscie[2] + " nie moze przyjsc na obiad.");

del goscie[2];

goscie.insert(2, 'Marek');

print("Zapraszam na obiad, " + goscie[0] + "!");
print("Zapraszam na obiad, " + goscie[1] + "!");
print("Zapraszam na obiad, " + goscie[2] + "!");
print("Zapraszam na obiad, " + goscie[3] + "!");
print("Zapraszam na obiad, " + goscie[4] + "!");

goscie.insert(0, 'Krzysztof');
goscie.insert(3, 'Mariusz');
goscie.append('Tomasz');

print(len(goscie));

print("Zapraszam na obiad, " + goscie[0] + "!");
print("Zapraszam na obiad, " + goscie[1] + "!");
print("Zapraszam na obiad, " + goscie[2] + "!");
print("Zapraszam na obiad, " + goscie[3] + "!");
print("Zapraszam na obiad, " + goscie[4] + "!");
print("Zapraszam na obiad, " + goscie[5] + "!");
print("Zapraszam na obiad, " + goscie[6] + "!");
print("Zapraszam na obiad, " + goscie[7] + "!");

print(f'Niestety, nie moge Cie zaprosic na obiad, {goscie.pop()}');
print(f'Niestety, nie moge Cie zaprosic na obiad, {goscie.pop()}');
print(f'Niestety, nie moge Cie zaprosic na obiad, {goscie.pop()}');
print(f'Niestety, nie moge Cie zaprosic na obiad, {goscie.pop()}');
print(f'Niestety, nie moge Cie zaprosic na obiad, {goscie.pop()}');
print(f'Niestety, nie moge Cie zaprosic na obiad, {goscie.pop()}');
print(len(goscie));

print("Zapraszam na obiad, " + goscie[0] + "!");
print("Zapraszam na obiad, " + goscie[1] + "!");

del goscie[0];
del goscie[0];

print(len(goscie));