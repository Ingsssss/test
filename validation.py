def valid_number(message):
    not_valid = True
    while not_valid:
        print(message)
        try:
            number = int(input())
            not_valid= False
        except ValueError:
            print("Please enter a number")
    return number