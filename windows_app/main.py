import requests
import json

def isExtra(type):
    print(type)
    if type == "xyz" or "synchro" or "fusion" or "link":
        return True
    else:
        return False

def getId(name):
    url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php?name=' + name
    try:
        response = requests.get(url)
        # Verifica se la richiesta ha avuto successo (codice di stato 200)
        if response.status_code == 200:
            data = json.loads(response.text)
            print(data["data"][0]['id'])
            # Apre il file in modalità scrittura
            # with open('response.json', 'a') as file:
            #     # Scrive i dati JSON nel file mantenendo la formattazione corretta
            #     json.dump(data, file, indent=4)
            # print("Dati scritti correttamente nel file 'response.json'")
        else:
            print('Errore nella richiesta:', response.status_code)
    except requests.RequestException as e:
        print('Errore durante la richiesta:', e)
    return [data["data"][0]['id'], isExtra(data["data"][0]['frameType'])]

def fill(id):
    str_id = str(id)
    while len(str_id) != 8:
        str_id = '0' + str_id
        print(str_id)
    return str_id

def getDecks(deck_list):
    main_list = []
    extra_list = []

    for elem in deck_list:
        card = getId(elem[1])
        if card[1]:
            id = fill(card[0])
            if elem[0] == "1x":
                main_list.append(id)

            elif elem[0] == "2x":
                main_list.append(id)
                main_list.append(id)

            elif elem[0] == "3x":
                main_list.append(id)
                main_list.append(id)
                main_list.append(id)

            else:
                print("problems with the card multiplier")
        else:
            id = fill(card[0])
            if elem[0] == "1x":
                extra_list.append(id)

            elif elem[0] == "2x":
                extra_list.append(id)
                extra_list.append(id)

            elif elem[0] == "3x":
                extra_list.append(id)
                extra_list.append(id)
                extra_list.append(id)

            else:
                print("problems with the card multiplier")

    return [main_list, extra_list]

def writeDeck(decks):
    output_file.write("#created by me\n")
    output_file.write("#main\n")

    for elem in decks[0]:
        output_file.write(elem + "\n")
        
    output_file.write("#extra\n")

    for elem in decks[1]:
        output_file.write(elem + "\n")

    output_file.write("!side\n")


input_file = open("C:/Users/nicoc/Projects/yu-gi-oh-deck-formatter/windows_app/input.txt", "r")
output_file = open("deck.ydk", "w")

deck_list = []
for line in input_file:
    line = line.strip()
    deck_list.append(line.split(" ", 1))

print(deck_list)

decks = getDecks(deck_list)
writeDeck(decks)
