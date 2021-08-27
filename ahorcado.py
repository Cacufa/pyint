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
            if len(i) < 6:
                difficulty = "Easy"
            elif len(i) > 6 and len(i) < 10:
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



def images(status):
    '''Print different images for hangman based on options'''
    if status == 1:
        print("="*35)
        print("||"," "*32,"|")
        print("||"," "*31,"___")
        print("||"," "*29,"/ -- |")
        print("||"," "*29,"\  ` |")
        print("||"," "*16,"You are dead  +___+")
        print("||"," "*28,"+  ___  +")
        print("||"," "*27,"+   ___   +")
        print("||"," "*31,"||")
        print("||"," "*31,"||")
        print("||"," "*29,"__  __")
        print("="*40)
    else:
        print("="*35)
        print("||"," "*32,"|")
        print("||")
        print("||")
        print("||")
        print("||"," "*10,"Still Alive")
        print("||")
        print("||")
        print("||")
        print("||")
        print("||")
        print("="*40)


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
    pass

def menu():
    '''Menu options -  print initial image'''
    option = ""
    while True:
        print("Please select one option: \n\nPlay: (1)\nProcess new words from txt file: (2)\nExit (3)")
        try:
            option = int(input(">>"))
            if option == 1:
                print("play")
            elif option == 2:
                words_clasification()
            elif option == 3:
                break
        except ValueError:
                print("The selection is not correct or is not a number.. ")



def run():
    #words_clasification()
    ##images(1)
    ##print(random_word())
    menu()

if __name__ == '__main__':
    run()
