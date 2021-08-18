from os import name


def run()   :
    print("started run")
    #squares =  [i**2 for i in range(1, 100) if i % 3 != 0]
    #print(squares)

    reto1 =  [i for i in range(1, 9999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(reto1)

if __name__ == '__main__':
    run()