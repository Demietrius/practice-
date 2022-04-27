def start(int):
    if int > 1:
        print("hello world")


def complex(number):
    index = 2
    dividerNumber = 1
    prime_number = 1
    while index < number:
        while dividerNumber < index:
            if index % dividerNumber == 0:
                break
            dividerNumber += 1
        else:
            prime_number = index

        index += 1
    return prime_number
