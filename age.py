def routine(age):    
    if age<7:
        return 'Вы должны ходить в детский сад.'
    elif age>=7 and age<18:
        return 'Вы должны ходить в школу.'
    elif age>=18 and age<=24:
        return 'Вы должны ходить в ВУЗ.'
    else:
        return 'Вы должны работать.'
age = int(input('Сколько вам лет?'))
print(routine(age))   
