import os
#from gtts import gTTS
from random import *

#def heli(text:str,keel:str):
   # obj=gTTS(text=text,lang=keel;slow=False).save("heli.mp3")
    #os.system("heli.mp3")

def failist_lugemine(f:str,l:list)->list:
    """Информация из файла f в список l
    :param str f: файл с информацией
    :param list l: список, в который добавляется информация
    :rtype: list
    """
    fail = open(f,"r",encoding="utf-8-sig")
    for rida in fail:
        l.append(rida.strip())
    fail.close()
    return l

def failisse_salvestamine(f:str,l:list):
    """Сохраняем списки в файл
    :param str f: файл, куда сохраняем
    :param list l: список, в который добавляется информация
    """
    fail = open(f,"w")
    for el in l:
        fail.write(el + "\n")
    fail.close()

def rida_salvestamine(f:str,rida:str):
    """Сохранение слова или фразы (строки) в файл
    :param str f: файл, куда сохраняем
    :param str rida: слово, которое нужно сохранить
    """
    fail = open(f,"a")
    fail.write(rida + "\n")
    fail.close()

def uus_sona(f:str,rida:str)->list:
    """
    :param str f:
    :param str rida:
    :rtype: list
    """
    with open(f,"a",encoding="utf-8-sig") as fail:
         fail.write(slovo + "\n")
         l.append(slovo)
    return l

def translate(slovo:str)->str:
    """
    :param str slovo:
    :rtype:
    """
def correction(slovo:str,l:list):
    """Заменим старое слово с ошибкой новым
    :param str slovo: слово которое нужно изменить
    :param list l: список где оно находится
    """
    for i in range(len(l)):
        if l[i] == slovo:
            uus_slovo = slovo.replace(slovo,input("Новое слово >>> "))
            l.insert(i,uus_slovo)
            l.remove(slovo)
            print(f"Слово >>> {slovo} было изменено на >>> {uus_slovo}!")

def test(result:int,l:list,l2:list)->int:
    """Слово выбирается случайным образом из списка, а затем проверяется
    :param int result: число правильных ответов
    :param list l: русский словарь
    :param list l2: английский словарь
    :rtype: int
    """
    slovo = choice(l)
    otvet = input(f"{slovo} >>> ")
    if otvet in l2: 
        if l2.index(otvet) == l.index(slovo):
            result += 1
            print("Õige")
    else:
        print("Vale")
    return result