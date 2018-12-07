import random


def get_random_schools_scores(default_scores_range=6):
    return [random.randrange(1, default_scores_range) for _ in range(13)]

marks_by_class = [
    {'school_class': '1a', 'scores': get_random_schools_scores()},
    {'school_class': '2a', 'scores': get_random_schools_scores()},
    {'school_class': '3a', 'scores': get_random_schools_scores()}
]

def count_marks(marks_list):

    classes = dict()
    total_av_scores = list()
    # n = 0

    # for i in range(len(marks_by_class)): #  Такой for loop характерен для Python 2.5, забудь про него.
    #     s += (marks_by_class[i]['scores'])
    #     i+=1

    # for i in range(len(s)):
    #     n+=s[i]

    # print('Средний балл по школе: ' + str(n/(len(s))))

    # for i in range(len(marks_by_class)):
    #     print((marks_by_class[i]['school_class']),(str(sum(marks_by_class[i]['scores'])/len(marks_by_class[i]['scores']))))
    #     i+=1

    for school_class in marks_by_class:
        cls_avg_score = sum(school_class["scores"])/len(school_class["scores"])
        classes[school_class["school_class"]] = cls_avg_score
        total_av_scores.append(cls_avg_score)

    return classes, sum(total_av_scores)/len(total_av_scores)


def main():

    classes, total_av_scores = count_marks(marks_by_class)

    for school_class in classes.items():
        print(f"В классе {school_class[0]} средний балл {school_class[1]:.2f}")

    print(f"Средний балл по школе {total_av_scores:.2f}")


if __name__ == '__main__':
    main()
