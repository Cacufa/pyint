DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    ##list comprehension
    print("list comprehension - Python Workers - Platzi Workers")
    python_workers = [worker['name'] for worker in DATA if worker['language'] == 'python']
    print(python_workers)
    platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    print(platzi_workers)

    ##lambda functions
    print("------------------------------------------")
    print("lambda functions - Adults")
    adults = list(filter(lambda workers:workers['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    print(adults)

    
    print("------------------------------------------")
    print("updating a dic with map lambda Old People ")
    ## updating a dic with map lambda 
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    for i in old_people:
        print(i)
    
    
    ## Reto
    ##hacer lo inverso utilizando list comprenhension
    
    print("------------------------------------------")
    print("Reto Adults")
    adults_reto = [worker['name'] for worker in DATA if worker['age'] > 18]
    for adult in adults_reto:
        print(adult)
    
    print("------------------------------------------")
    print("Reto Old People")
    old_people_reto = [worker | {'old': worker['age'] > 70 } for worker in DATA]
    for old in old_people_reto:
        print(old)





if __name__ == '__main__':
    run()