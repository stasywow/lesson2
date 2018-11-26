def comparison(first,second):
    if type(first)!=str and type(second)!=str:
        return '0'
    elif first==second:
        return '1'
    elif first!=second and len(first)>len(second):
        return '2'
    elif first!=second and second=='learn':
        return '3'    
first = input()
second = input()
print(comparison(first,second))

