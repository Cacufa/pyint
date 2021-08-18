def run():
    print("Run Started")
    my_dict = {}

    my_dict = {i:i**3 for i in range(1, 100) if i % 3 !=0}
    print(my_dict)

if __name__ == '__main__':
    run()