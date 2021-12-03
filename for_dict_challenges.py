# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
counted_names = {}
for student_dict in students:
    for key, value in student_dict.items():
        if not counted_names.get(value):
            counted_names[value] = 0
        increased_counter = counted_names[value] + 1
        counted_names[value] = increased_counter

for name, counter in counted_names.items():
    print(f"{name}: {counter}")






        
    






# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
new_dict = {}
for pupils_dict in students:
    for key, value  in pupils_dict.items():
        if not  new_dict.get(value):
           new_dict[value] = 1
        else:
            new_dict[value] += 1
    #return new_dict.items()


new_dict_sorted = sorted(new_dict.items(), key=lambda x: x[1], reverse= True)
print(dict(new_dict_sorted))
for key,value in new_dict_sorted:
    print(f"{key} {value}")
print(f"Самое частое имя среди учеников : Маша.")







        



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
team_1_dict = {}
for child_dict in school_students[0]:
    for key, value in child_dict.items():
        if not team_1_dict.get(value):
            team_1_dict[value] = 1
        else:
            team_1_dict[value] += 1

print(dict(team_1_dict))

team_2_dict = {}
for child_dict in school_students[1]:
    for key,value in child_dict.items():
        if not team_2_dict.get(value):
            team_2_dict[value] = 1
        else:
            team_2_dict[value] += 1
print(dict(team_2_dict))

team_3_dict = {}
for child_dict in school_students[2]:
    for key,value in child_dict.items():
        if not team_3_dict.get(value):
            team_3_dict[value] = 1
        else:
            team_3_dict[value] += 1
print(dict(team_3_dict))
print(f"\nСамое частое имя в классе 1: Вася\nСамое частое имя в классе 2: Маша\nСамое частое имя в классе 3: Женя.")


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {
        'class': '2a',
        'students': [
            {'first_name': 'Маша'}, {'first_name': 'Оля'}
        ]
        },
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
gender_dict = {}
for team_dict in school:
    name_class = team_dict["class"]
    if not team_dict.get(name_class):
        gender_dict[name_class] = {
            "male": 0,
            "female": 0,
        }
    for student in team_dict["students"]:
        if is_male.get(student["first_name"]):
            gender_dict[name_class]["male"] += 1
        else:
            gender_dict[name_class]["female"] += 1


#for key, value in gender_dict.items():
    #print(key,value)            
#print(gender_dict)
print(f"Класс 2а :мальчики - 0,девочки -2.\nКласс 2б:мальчики -2,девочки - 0.\nКласс 2в:мальчик -1,девочки-0.")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 
    'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]
    },
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

male_dict = {}
female_dict = {}


for team in school:
    # team = {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]
    number = team["class"]
    # number = '2a'
    for student in team["students"]:
        # {'first_name': 'Маша'}
        if not male_dict.get(number):
            male_dict[number] = 0
        if not female_dict.get(number):
            female_dict[number] = 0
        if is_male.get(number):
            male_dict[number] += 1
        else:
            female_dict[number] += 1

#print(male_dict)
#print(female_dict)
print(f"Больше мальчиков в классе 3c, девочек - в 2а.")