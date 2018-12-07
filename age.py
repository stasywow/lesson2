def main():
    user_age = int(input('Сколько вам лет? '))

    if user_age < 7:
        print('Вы должны ходить в детский сад.')
    elif 7 <= user_age < 18:
        print('Вы должны ходить в школу.')
    elif 18 <= user_age < 24:
        print('Вы должны ходить в ВУЗ.')
    elif 24 <= user_age < 65:
        print('Вы должны работать.')
    else:
        print('Вы на пенсии и уже никому ничего не должны.')


if __name__ == '__main__':
    main()
