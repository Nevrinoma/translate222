import os
from random import *
from typing import List
import gtts 
from playsound import playsound

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

def uus_sona(f:str,slovo:str,l:list)->list:
    """
    :param str f:
    :param str slovo:
    :rtype: list
    """
    with open(f,"a",encoding="utf-8-sig") as fail:
         fail.write(slovo + "\n")
         l.append(slovo)
    return l


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

def test(result:int,l:list,l2:list):
    """Слово выбирается случайным образом из списка, а затем проверяется
    :param int result: число правильных ответов
    :param list l: русский словарь
    :param list l2: английский словарь
    :rtype: int
    """
    
    result = 0
    for i in range(len(l)):
        slovo = choice(l)
        otvet = input(f"{slovo} >>> ")
        if otvet in l2: 
            if l2.index(otvet) == l.index(slovo):
                result += 1
                print("Правильно")
            else:
                print("Неправильно")
    
    hind = result * 100 / len(l2)
    print(f"Вы набрали {result}/{len(l)} пунктов ")
    if hind >= 90:
        return result, "Отлично, вы получаете 5!"
    elif hind >= 75 and hind <= 90:
        return result, "Прекрасно, вы получаете 4!"
    elif hind >= 50 and hind <= 75:
        return result, "Неплохо, вы получаете 3!"
    else:
        return result, "К сожалению, вы получаете 2!"


def voice():
    lang = input("Какоя язык прослушать eng/rus >>> ")
    if lang=="rus":
        text=input("Введите слово для озвучки на русском: ")
        tts=gtts.gTTS(text, lang="ru")
        tts.save("sound.mp3")
        playsound("sound.mp3")
        #os.remove("sound.mp3")
    elif lang=="eng":
        text=input("Введите слово для озвучки на английском: ")
        tts=gtts.gTTS(text, lang="en")
        tts.save("wordsound.mp3")
        playsound("wordsound.mp3")
        #close("wordsound.mp3")
        #os.remove("wordsound.mp3")
    else:
        print("Ошибка ввода, попробуйте еще раз")