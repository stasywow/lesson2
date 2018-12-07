

def main(first, second):
    if type(first) != str and type(second) != str:
        return '0'
    elif first == second:
        return '1'
    elif first != second and len(first) > len(second):
        return '2'
    elif first != second and second == 'learn':
        return '3'


if __name__ == '__main__':
    first = input("Enter first string")
    second = input("Enter second string")
    print(main(first, second))
