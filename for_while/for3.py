classes = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4в', 'scores': [2,3,3,5,4]},
    {'school_class': '4б', 'scores': [3,3,5,5,5]}
]
scores_sum = 0
scores_sum_all=0
lenall=0
for number in range(3):
    classs = (classes[number]['scores'])
    for score in classs:
        scores_sum += score
        print(scores_sum)
    scores_avg = scores_sum / len(classs)
    scores_sum_all +=scores_sum 
    lenall +=len(classs)
    scores_sum = 0
    print(f'класс {classes[number]["school_class"]} средняя оценка {scores_avg}' )
print(scores_sum_all)
print(lenall)
print(f'СРЕДНЯЯ ОЦЕНКА ОП ШКОЛЕ {scores_sum_all/lenall}')