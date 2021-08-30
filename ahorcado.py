from io import FileIO
import json
import random
from os import system

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
            if len(word) < 6:
                difficulty = "Easy"
            elif len(word) > 6 and len(word) < 10:
                difficulty = "Medium"
            else:
                difficulty = "Hard"
            word_dict = {'chars':chars,'difficulty':difficulty} 
            words[word]=word_dict
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
    try:
        print(pics[pic])
    except IndexError:
        print(pics[6])


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
    with open("./archivos/leader_board.json",'w') as f:
        leaders = json.load(f.read())
        for key, value in leaders.items:
            print(f"Usuario {key} puntos {value}")

def points(name,points):
    '''assign points based on attempts and word difficulty'''
    leaders_temp = {}
    leaders_temp[name] = int(points)

    with open("./archivos/leader_board.json",'r') as f:
        leaders = json.loads(f.read())

        if name in leaders:
            leaders[name] += points
        else:
            leaders[name] = points

    with open("./archivos/leader_board.json",'w') as f:
        leaders = json.dump(leaders, f)


def normalize(letter):
    replacements = {"á":"a","é":"e","í": "i","ó": "o","ú": "u"}
    try: 
        return replacements[letter]
    except:
        return letter



def game():
    '''Game logic'''
    tries = 0
    word_dict = random_word()
    word = word_dict[0]
    letters = []
    letter = ""

    while tries < len(word):
        system("cls")
        images(tries)
        print(word)
        print("Tries: ", tries)
        print(f"Total Letters:{word_dict[1]['chars']} - Difficulty:{word_dict[1]['difficulty']}")
        temp_word = word_logic(word, letters)
        if temp_word.count("_") != 0:
            print(" ".join(temp_word))
            if len(letter) > 2 or letter.isnumeric():## only accept one letter digit
                print("You can only insert one letter")
            else:
                letter = input("Enter the letter: ")
                if letter not in letters: #only add words if they are new
                    letter = letter.lower()
                    letters.append(letter)
                else:
                    tries += 1 # only sum tries if the user fail
        else:
            print("You won Congratulations! ")
            name = input("please enter your name in order to add the points!: ")
            points(name,13)
            leaders()
            input("Press enter to continue.")
            break
        
        


    
def word_logic(word, letters):
    '''gets the word, the word_list(the word in list format) and letters, a list conaining all 
    letters that the users provided returns the list with the letters already guessed'''
    word_list = [normalize(letter) for letter in word]
    temp_word_list = []
    for i in range(0, len(word_list)):
        if (word_list[i]).lower() in letters:
            temp_word_list.append(word_list[i])
        else:
            temp_word_list.append("_")
    return (temp_word_list)



def menu():
    '''Menu options -  print initial image'''
    system("cls")
    option = ""
    print("Welcome to the hangman grame! ")
    while True:
        print("Please select one option: \n\n(1) Play: \n(2) Process new words from txt file: \n(3) Exit ")
        print("")
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
        system("cls")



def run():
    #words_clasification()
    ##images(0)
    ##print(random_word())
    menu()




if __name__ == '__main__':
    run()
