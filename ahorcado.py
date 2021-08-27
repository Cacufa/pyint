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
    with open("./archivos/wordsdb.json","r") as f:
        words = json.loads(f.read())
        total_words = int(len(words))
        random_word = random.randint(1, total_words)
    counter = 0
    for word,value in words.items():
        print(random_word)
        print(word,value)
        '''
        if counter == random_word:
            return word
        else:
            return "not found"
        counter += 1
        '''
    print(counter)





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

    pass

def run():
    #words_clasification()
    ##images(1)
    print(random_word())

if __name__ == '__main__':
    run()
