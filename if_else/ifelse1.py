def study(age):
    age= int(age)
    if age <= 5:
        return('детский сад')
    elif 6 <= age <= 17:
        return('школа')
    elif 18 <= age <= 23:
        return('ВУЗ')
    else:
        return('Работа')         

user_age = input ('возрост?')
print(study(user_age))
