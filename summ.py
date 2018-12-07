

def get_summ(num_one, num_two):
    try:
        print(int(num_one) + int(num_two))
    except ValueError:
        print('Не получилось :(')


first = float(input("Enter first number"))
second = float(input("Enter second number"))
print(get_summ(first, second))
