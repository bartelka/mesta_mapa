import math
import time

fr_1 = open("vrcholy.txt", "r", encoding="utf-8")
vrcholy = [i.strip().split(";") for i in fr_1]

fr_2 = open("hrany.txt", "r", encoding="utf-8")
hrany = [i.strip().split(";") for i in fr_2]

def kresli_mesto(vrcholy):
    global mestecka, mesta_bodky
    for i in vrcholy:
        bodka = canvas.create_oval(int(i[1]) - 4, int(i[2]) - 4, int(i[1]) + 4, int(i[2]) + 4, fill="hotpink")
        mesta_bodky[i[0]] = mesta_bodky.get(i[0], bodka)
        canvas.create_text(int(i[1]), int(i[2]) + 8, fill="black", text=i[0])
        mestecka[i[0]] = mestecka.get(i[0], (int(i[1]), int(i[2])))

def kresli_hrany():
    for mesto, susedia in mesta.items():
        for i in range(len(susedia)):
            canvas.create_line(mestecka[mesto][0], mestecka[mesto][1], mestecka[susedia[i]][0], mestecka[susedia[i]][1], fill="magenta")
def priradenie_miest(hrany):
    global mesta, mesta_hodnoty
    for i in hrany:
        mesta[i[0]] = mesta.get(i[0], [])
        mesta_hodnoty[i[0]] = mesta_hodnoty.get(i[0], {})
    for i in hrany:
        m_1 = i[0]
        m_2 = i[1]

        x_1, y_1 = mestecka[m_1][0], mestecka[m_1][1]
        x_2, y_2 = mestecka[m_2][0], mestecka[m_2][1]

        vzdialenost = (x_2 - x_1) ** 2 + (y_2 - y_1) ** 2
        vzdialenost = round(math.sqrt(vzdialenost), 2)

        mesta[m_1].append(m_2)
        mesta_hodnoty[m_1][m_2] = vzdialenost
        if m_2 not in mesta_hodnoty:
            mesta_hodnoty[m_2] = mesta_hodnoty.get(m_2, {})
        mesta_hodnoty[m_2][m_1] = vzdialenost

def into_the_deep(mesto):
    global navstivene_1
    navstivene_1.append(mesto)
    canvas.itemconfig(mesta_bodky[mesto], fill="blue")
    canvas.update()
    time.sleep(0.1)
    for mestecko, vzdialenost in mesta_hodnoty[mesto].items():
        if mestecko not in navstivene_1:
            into_the_deep(mestecko)

def into_the_width(mesto):
    global navstivene_2
    zoznamik = []
    navstivene_2.append(mesto)
    zoznamik.append(mesto)
    while zoznamik != []:
        print(zoznamik)
        for mesto, hod in mesta_hodnoty[zoznamik[0]].items():
            if mesto not in navstivene_2:
                zoznamik.append(mesto)
                navstivene_2.append(mesto)
        if len(zoznamik) != 0:
            zoznamik.remove(zoznamik[0])


import tkinter as tk

win = tk.Tk()

w = 1000
h = 900

mesta_bodky = {}
#mestecka = mesta so suradnicami
mestecka = {}
#mesta = k mestam su priradene susedne mesta
mesta = {}
#mesta so vzdialenostami medzi sebou
mesta_hodnoty = {}
#navstivene mesta
navstivene_1 = []
navstivene_2 = []

ciary = []

canvas = tk.Canvas(width=w, height=h, bg="white")
canvas.pack()

kresli_mesto(vrcholy)
priradenie_miest(hrany)
kresli_hrany()

into_the_deep("Martin")
into_the_width("Bratislava")

print(mesta_hodnoty)
print(mesta_bodky)
win.mainloop()
#dudo.gvpt.sk zadanie -> grafy(hrany.txt, vrcholy.txt)
