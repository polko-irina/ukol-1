baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

balik = input(" Zadej kód balíku : ")

if balik in baliky:
    if baliky[balik]:
        print("Balík byl doručen")
    else :
        print ("Balík zatím nebyl doručen")
else:
    print (" Balik neexistuje ")



a = input("Jaky region tě zajima? ")
for stat in staty:
    if stat['region'] == a:
         print(stat['name'])
else:
    print("Neznámý region")
