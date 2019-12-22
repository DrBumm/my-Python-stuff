# Buchstaben sortier algorithmus
# Zu erst machen wir es umständlich
random_buchstaben = ['h', 's', 'u', 'v', 'y', 'm', 'j', 't']
alphabet = {'a' : 1, 'b' : 2, 'c' : 3, 'd': 4, 'e' : 5, 'f' : 6, 'g' : 7,
            'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12,'m' : 13,'n' : 14,
            'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20,
            'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26}
temp_array = []

# Hier wird es dann in eine zahlen liste umgewandelt die wir dann sortieren
# werden mit einem inefizienten aber leicht schreib barem bubble sort und danach
# wieder zurück in buchstaben umwandeln die dann dem alphabet geordnet sind

# Unwandeln
for i in random_buchstaben:
    i.lower()
    key_pos = alphabet[i]
    temp_array.append(key_pos)
print(temp_array)


# Bubble sort
def sort(new_list, a=0):
        while len(new_list) > a:
                for i in range(len(new_list)-1):
                    if new_list[i] > new_list[i+1]:
                        new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
                a+=1

# Sortieren
sort(temp_array)
print(temp_array)

# Löschen des inhaltes von random_buchstaben
random_buchstaben.clear()

# Zurück umwandeln
i2 = 0
print('sorting ', i2, '%')
for i in range(len(temp_array)):
    for key, value in alphabet.items():
        if value == temp_array[i2]:
            random_buchstaben.append(key)
    i2 += 1
    print('sorting ', i2*10+20, '%')

print("Input: ['h', 's', 'u', 'v', 'y', 'm', 'j', 't']",
      '\nOutput: ' + str(random_buchstaben))




print('\n\n')
# Und jetzt machen wir es mal kurz
random_buchstaben = ['h', 's', 'u', 'v', 'y', 'm', 'j', 't']
temp_array = []

# Umwandeln
for i in range(len(random_buchstaben)):
    temp_array.append(ord(random_buchstaben[i]))

# Sortieren
temp_array = sorted(temp_array)

# Löschen des inhaltes von random_buchstaben
random_buchstaben.clear()

# Zurück umwandeln
print('sorting ', 0, '%')
for i in range(len(temp_array)):
    print('sorting ', i*10+30, '%')
    random_buchstaben.append(chr(temp_array[i]))

print("Input: ['h', 's', 'u', 'v', 'y', 'm', 'j', 't']\n" +
      'Output: ' + str(random_buchstaben))
