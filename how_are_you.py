
def ask_user():
    q = input('Как дела?')
    while q != 'Хорошо':
        q = input('Как дела?')


if __name__ == '__main__':
    ask_user()
