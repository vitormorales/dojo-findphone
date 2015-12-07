from phone_converter import PhoneConverter

__author__ = 'vitor'


def main():
    with open('input.txt', 'r') as file:
        for line in file.read().splitlines():
            print("\nInput: " + line)
            print("Output: " + PhoneConverter().convert(line))
    file.close()


if __name__ == '__main__':
    main()






