words = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}
while True:
    user_say = input()
    if user_say == "Как дела":
        print(words["Как дела"])
    elif user_say == "Что делаешь?":
        print(words["Что делаешь?"])
    
