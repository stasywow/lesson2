marks_by_class = [{'school_class':'1a','scores':[2,3,4,5,2,3,3,4,5,5,5,2]},
                  {'school_class':'2a','scores':[5,4,4,5,3,3,3,4,5,5,5,3]},
                  {'school_class':'3a','scores':[2,3,3,4,2,3,3,4,4,5,3,4]}]
s = []
n = 0
for i in range(len(marks_by_class)):
    s += (marks_by_class[i]['scores'])
    i+=1
for i in range(len(s)):
    n+=s[i]
print('Средний балл по школе: ' + str(n/(len(s))))
for i in range(len(marks_by_class)):
    print((marks_by_class[i]['school_class']),(str(sum(marks_by_class[i]['scores'])/len(marks_by_class[i]['scores']))))
    i+=1
