def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = 0
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
        print("final del programa")
    except ValueError:
        print("Debe ser un numbero natural: ")



if __name__ == '__main__':
    run()