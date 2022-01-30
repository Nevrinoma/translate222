from Module import*
eng = []
rus = []
failist_lugemine("eng.txt",eng)
failist_lugemine("rus.txt",rus)
vastus = True
while vastus:
    print("""
    1 >>> Все слова
    2 >>> Перевести
    3 >>> Новое слово
    4 >>> Исправление ошибок
    5 >>> Тест
    6 >>> Прослушать слово
    7 >>> Выход""")
    vastus = input(">>> ")
    if vastus == "1":
        print(eng)
        print(rus)
        continue
    elif vastus == "2":
        slovo = input("Введите слово для перевода >>> ")
        if slovo not in eng and slovo not in rus:
            print(f"Этого слова {slovo} еще нет в нашем словаре, но вы можете добавить его")
            continue
        else:
            if slovo in eng:
                indeks = eng.index(slovo)
                print(f"{slovo} - {rus[indeks]}")
            elif slovo in rus:
                indeks = rus.index(slovo)
                print(f"{slovo} - {eng[indeks]}")
                
    elif vastus == "3":
        print()
        slovo = input("Напишите слово, которое хотите добавить в английский словарь >>> ")
        if slovo in eng:
            print("Такое слово уже есть")
        else:
            uus_sona("eng.txt",slovo,eng)
        slovo = input("Напишите слово, которое хотите добавить в русский словарь >>> ")
        if slovo in rus:
            print("Такое слово уже есть")
        else:
            uus_sona("rus.txt",slovo,rus)
    elif vastus == "4":
        print()
        vastus = input("В каком словаре ошибка eng/rus? >>> ")
        if vastus == "eng":
            slovo = input("Впишите слово с ошибкой из английского словаря >>> ")
            correction(slovo,eng)
        elif vastus == "rus":
            slovo = input("Впишите слово с ошибкой из русского словаря >>> ")
            correction(slovo,rus)
        else:
            print("Неверный тип данных!")
    elif vastus == "5":
        print()
        print("""
        Сейчас вы должны переводить слова на оценку, пишите перевод слова который будет на экране!""")
        result = 0
        for i in range(len(rus)):
            number = randint(1,2)
            if number == 1:
                result = test(result,rus,eng)
            else:
                result = test(result,eng,rus)
        hind = result * 100 / len(rus)
        print(f"Вы набрали {result}/{len(rus)} пунктов ")
        if hind >= 90:
            print("Отлично, вы получаете 5!")
        elif hind >= 75 and hind <= 90:
            print("Прекрасно, вы получаете 4!")
        elif hind >= 50 and hind <= 75:
            print("Неплохо, вы получаете 3!")
        else:
            print("К сожалению, вы получаете 2!")
    elif vastus == "6":
        voice()
    elif vastus == "7":
        break
    else:
        print("Неверный тип данных!")
