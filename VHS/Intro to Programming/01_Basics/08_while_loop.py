user_input = 1
zahlen_all = "Alle Zahlen sind:"
zahlen_gerade = "Alle geraden Zahlen sind:"
zahlen_ungerade = "Alle ungeraden Zahlen sind:"

while user_input:
    user_input = int(input('Gib eine ganze Zahl oder "0" zum Beenden ein: '))
    if user_input:
        zahlen_all += f' {user_input}'
        if user_input % 2:
            zahlen_gerade += f' {user_input}'
        else:
            zahlen_ungerade += f' {user_input}'

print(zahlen_all)
print(zahlen_ungerade)
print(zahlen_gerade)

temperature = 40
while True:
    print(temperature)
    temperature -= 1
    if temperature == 25:
        break  # exits the loop

print('Ende')

while True:
    user_input = input("PLZ: ")
    if len(user_input) != 5:
        print('Du must genau 5 Zeichen eingeben!')
        continue  # jumps to next iteration
    break
