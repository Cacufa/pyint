def run():
    my_list = [1, "Hello", True, 4.5]
    mu_dic = {"firstname":"Carlos", "lastname":"Saborio"}
    
    super_list= [
        {"firstname":"Carlos", "lastname":"Saborio"},
        {"firstname":"Juan", "lastname":"Torres"},
        {"firstname":"Chris", "lastname":"Jones"},
        {"firstname":"Rob", "lastname":"Chat"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 2.2, 3.3]
    }

    for key,value in super_dict.items():
        print(key,":",value)


if __name__ == "__main__":
    run()

