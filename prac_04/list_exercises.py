
NUMBER_LENGTH = 5

def main():
    numbers = get_valid_number(NUMBER_LENGTH)
    print_info(numbers)


def get_valid_number(number_length):
    numbers = []
    for i in range(number_length):
        flag = False
        while not flag:
            try:
                number = int(input("Numbers: "))
                numbers.append(number)
                flag = True
            except ValueError:
                print("Invalid number")
    return numbers

def print_info(numbers):
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of number is {sum(numbers)/len(numbers)}")

main()