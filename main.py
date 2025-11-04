import random
import sys
import os
import time
from colorama import Fore, Style

kartyak = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 8
lap = 0
kez = []
oszto = []
lepszam = 0
cikl = 1
penz = 5000


def zoldpr(text):
    print(Fore.GREEN + text)
    print(Style.RESET_ALL)


def pirospr(text):
    print(Fore.RED + text)
    print(Style.RESET_ALL)


def huzas():
    lap = random.choice(kartyak)
    if str(lap) in 'JQK':
        lap = int(10)
    elif str(lap) == 'A':
        lap = int(11)
    kartyak.pop(lap)
    return lap


def ace():
    if 11 in kez:
        kezertek = sum(kez)
        if kezertek > 21:
            for i, x in enumerate(kez):
                if x == 11:
                    kez[i] = 1


def check():
    global penz, kez, oszto
    kezertek = sum(kez)
    osztoertek = sum(oszto)
    if osztoertek > 21 and kezertek >= 21:
        time.sleep(1)
        os.system('cls')
        penz += tet

        print(f'Nalad: {kez} ({kezertek})\nOsztonal: {oszto} ({osztoertek})')
        print("Oszto besokallt, WIN")
        zoldpr(f'+{tet}Ft')
        time.sleep(2)
    elif osztoertek >= 17:
        if 21 >= osztoertek > kezertek:
            time.sleep(1)
            os.system('cls')

            print(f'Nalad: {kez} ({kezertek})\nOsztonal: {oszto} ({osztoertek})')
            print("Oszto nyert, LOSE")
            penz -= tet
            pirospr(f'-{tet}Ft')
            time.sleep(2)
        elif kezertek == 21 and (kez == [11, 10] or kez == [10, 11]):
            time.sleep(1)
            os.system('cls')
            penz += tet * 1.5

            print(f'Nalad: {kez} ({kezertek})\nOsztonal: {oszto} ({osztoertek})')
            print("Black Jack!!")
            zoldpr(f'+{tet * 1.5}Ft')
            time.sleep(2)
        elif osztoertek == kezertek:
            time.sleep(1)
            os.system('cls')
            penz += tet

            print(f'Nalad: {kez} ({kezertek})\nOsztonal: {oszto} ({osztoertek})')
            print("PUSH")
            time.sleep(2)
        elif osztoertek < kezertek:
            time.sleep(1)
            os.system('cls')
            penz += tet

            print(f'Nalad: {kez} ({kezertek})\nOsztonal: {oszto} ({osztoertek})')
            print("WIN")
            zoldpr(f'+{tet}Ft')
            print(Style.RESET_ALL)
            time.sleep(2)
        elif osztoertek > 21:
            time.sleep(1)
            os.system('cls')
            penz += tet

            print(f'Nalad: {kez} ({kezertek})\nOsztonal: {oszto} ({osztoertek})')
            print("Oszto besokallt, WIN")
            zoldpr(f'+{tet}Ft')
            print(Style.RESET_ALL)
            time.sleep(2)


os.system('cls')
i = int(input("[1] Játék\n[0] Kilepes\nParancs: "))
oszto.clear()
kez.clear()
if i == 1:
    while penz >= 10:
        os.system('cls')
        tet = int(input(f'{penz}Ft-od van.\nMennyi lesz a tet?(min. 10, 10-el oszthato): '))
        oszto.clear()
        kez.clear()
        if tet >= 10 and tet % 10 == 0 and tet <= penz:
            oszto.clear()
            kez.clear()
            huzott = huzas()
            kez.append(huzott)
            huzott = huzas()
            oszto.append(huzott)
            huzott = huzas()
            kez.append(huzott)
            huzott = huzas()
            oszto.append(huzott)
            ace()
            kezertek = sum(kez)
            osztoertek = sum(oszto)
            os.system('cls')

            print(f'Nalad: {kez} ({kezertek})\nOsztonal: {oszto[0]}')

            akciosz = 1

            while True:
                akcio = input("Akcio: ")

                if akcio == 'h':
                    huzott = huzas()
                    kez.append(huzott)
                    ace()
                    kezertek = sum(kez)
                    osztoertek = sum(oszto)
                    os.system('cls')

                    print(f'Nalad: {kez} ({kezertek})\nOsztonal: {oszto[0]}')
                    time.sleep(1)
                    if kezertek > 21:
                        print("Besokalltal. Pancser.")
                        pirospr(f'-{tet}Ft')
                        penz -= tet
                        time.sleep(2)
                        print(Style.RESET_ALL)
                        break

                elif akcio == 's':
                    while osztoertek < 17:
                        kezertek = sum(kez)
                        osztoertek = sum(oszto)
                        os.system('cls')

                        print(f'Nalad: {kez} ({kezertek})')
                        print(f'Osztonal: {oszto} ({osztoertek})')
                        time.sleep(1)
                        huzott = huzas()
                        oszto.append(huzott)
                        osztoertek = sum(oszto)
                    check()
                    break
        elif tet > penz:
            os.system('cls')

            print("Te kis sunyi, nincs ennyi penzed csorikam.")
            time.sleep(2)
            i = 0
        elif tet % 10 != 0:
            os.system('cls')

            print("A tet nem oszthato 10-el!")
            time.sleep(2)
            i = 0
        else:
            i = 0

    if penz < 10:
        os.system('cls')
        print(Fore.RED + "Elfogyott a penzed.\nGAME OVER")
        time.sleep(2)

elif i == 0:
    sys.exit()