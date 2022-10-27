#vlozenie modulu
import tkinter 

#nastavenie platna a jeho rozmerov
canvas = tkinter.Canvas(width=500, height=570, background="white") 
canvas.pack()

#zoznamy
suradnice_x = []
suradnice_y = []
farbicky = []
listik_x = [50,100,150,200,250,300,350,400,450,500]
listik_y = [50,100,150,200,250,300,350,400,450,500]

def mreze(): #funkcia na vykreslenie mriezky
    x1 = 50
    y1 = 50
    for i in range(10):
        canvas.create_line(x1,0,x1,500)
        canvas.create_line(0,y1,500,y1)
        x1 += 50
        y1 += 50

def klik_blik(suradnice): #funkcia na zistenie suradnic, farby a vykreslenie
    #zistenie zadanej farby a suradnic kliku mysky
    farba = entry1.get()
    x = suradnice.x
    y = suradnice.y

    #zistenie na ktoru kocku bolo kliknute
    for i in listik_x:
        if x < i:
            suradnicka = i
            break
    for ii in listik_y:
        if y < ii:
            suradnicka1 = ii
            break

    #ukladanie udajov do zoznamov
    suradnice_x.append(suradnicka)
    suradnice_y.append(suradnicka1)
    farbicky.append(farba)

    #vyfarbenie kliknuteho stvorceka
    canvas.create_rectangle(suradnicka-49,suradnicka1-49,suradnicka-1,suradnicka1-1,fill=farba)

def disketka(): #funkcia na zapisanie udajov zo zoznamov do .txt suboru 
    subor = open("kockove_hry_suradnice.txt","w")
    for i in suradnice_x:
        subor.write(str(i)+" ")
    subor.write("\n")
    for ii in suradnice_y:
        subor.write(str(ii)+" ")
    subor.write("\n")
    for iii in farbicky:
        subor.write(str(iii)+" ")
    subor.close()

#privolanie funkcie
mreze()

#vytvorenie vstupu
entry1 = tkinter.Entry()
entry1.pack()

#vytvorenie tlacidla
carovne_tlacitko = tkinter.Button(text='Uložiť',command=disketka)
carovne_tlacitko.pack()

#nastavenie tlacidla mysky
canvas.bind('<Button-1>',klik_blik)
