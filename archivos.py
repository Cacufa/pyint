def read():
    numbers = []
    with open('./archivos/numbers.txt', 'r', encoding="utf-8") as f:
        numbers = [int(line) for line in f]
        print(numbers)



def write():
    names = ["Carlos","Juan","Pablo","Camilo","Cristina","Julia","Marta"]
    with open('./archivos/names.txt', 'a', encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")



def run():
    read()
    write()



if __name__ == '__main__':
    run()