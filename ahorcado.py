from io import FileIO
import json
import random

def words_clasification():
    '''
    Clasify the words based on dificulty (Len)
    assign the number of hidden letters based on the word len
    data must be saved in a json file with key:value data.
    '''
    words = {}
    with open("./archivos/palabras.txt","r", encoding="utf-8") as f:
        for i in f:
            word = i.strip()
            chars = len(word)
            hidden = int(chars/2)
            if len(word) < 6:
                difficulty = "Easy"
            elif len(word) > 6 and len(word) < 10:
                difficulty = "Medium"
            else:
                difficulty = "Hard"
            word_dict = {'chars':chars,'hidden':hidden,'difficulty':difficulty}
            words[word]=word_dict
            #for key,value in words.items():
            #    print(key,value)

    try:
        with open("./archivos/wordsdb.json", "w", encoding="utf-8") as f:
            words_json = json.dump(words,f)
        print("File Saved..")
    except IOError as e:
        print("File not saved..",e)



def images(pic):
    '''Print different images for hangman based on options
        Reference github chrishorton/hangmanwordbank.py'''
    pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 
    print(pics[pic])


def random_word():
    '''This method renerates a ramdom word from a json db and return a tuble with the word information'''
    with open("./archivos/wordsdb.json","r", encoding="utf-8") as f:
        words = json.loads(f.read())

    with open("./archivos/palabras.txt","r", encoding="utf-8") as f:
        words_list = [palabra.strip() for palabra in f]
    
    random_word_number = random.randint(0, len(words_list))
    random_word = words_list[random_word_number]

    return random_word, words[random_word]


def leaders():
    '''keep record or leaders and points'''
    pass

def points():
    '''assign points based on attempts and word difficulty'''
    pass

def game():
    '''Game logic'''
    images(0)
    word = random_word()
    print(f"Total Letters:{word[1]['chars']} - Hidden Letters:{word[1]['hidden']} - Difficulty:{word[1]['difficulty']}")
    word_in_list = [letter for letter in word[0]]
    print(word_in_list[5])
    '''----------------
    mostrar la palabra con letras faltantes index mod 0 hide
    poner en lista las respuesta del usuario para mapearlas y poneras en la palabra
    buscar en palabra lista si la letra existe i retornar los indices y actualizarla
    '''
    
def word_logic(word, word_list, letters):
    ##combierte la palabra en list, returna con espacios vacios si no pasa letra, 
    # de lo contrario coloca las letras y devuelve la palabra
    temp_word_list = []
    for letter in word_list:
        if letter in letters:
            temp_word_list.append(letter)
        else:
            if int(word_list.index(letter)) % 2 == 0:
                print(word_list.index(letter))
                print(int(word_list.index(letter)) % 2 == 0)
                temp_word_list.append("_")
                input("enter")
            else:
                temp_word_list.append(letter)
    print(temp_word_list)



def menu():
    '''Menu options -  print initial image'''
    option = ""
    while True:
        print("Please select one option: \n\nPlay: (1)\nProcess new words from txt file: (2)\nExit (3)")
        try:
            option = int(input(">>"))
            if option == 1:
                game()
            elif option == 2:
                words_clasification()
            elif option == 3:
                break
        except ValueError:
                print("The selection is not correct or is not a number.. ")



def run():
    #words_clasification()
    ##images(0)
    ##print(random_word())
    ##menu()
    letters = []
    word_list = ['a','h','o','r','c','a','d','o']
    word = "ahorcado"
    word_logic(word,word_list,letters)

if __name__ == '__main__':
    run()
