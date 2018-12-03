def get_summ(num_one, num_two):
    try:
        print(int(num_one) + int(num_two))
    except ValueError:
        print('Не получилось :(')
get_summ(3,4)
#get_summ('a',4)        
