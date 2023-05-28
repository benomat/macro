import pyautogui as pg;from time import sleep
from  random import randint
import json
from os import system
system("title bnmt's farming macro V2.0")
drop_time=4
data={}
try:
    file = open("config.txt").read()
except:#settings holen
    data["time_for_row"]=float(input("Wie viele sekunden brauchst du für eine Reihe?\n"))
    data["row_amount"]=int(input("Wie viele rows? (MUSS EINE GRADE ZAHL SEIN WEIL JA)\n"))
    data["respawn_method"]=int(input("""Wähle eine option aus mit der du an den Anfang der farm kommst!
    1 - Respawn (Am Ende der Farm runterfallen und mit /setspawn an den Anfang der Farm gelangen)
    2 - Lobbyhop (Am Ende der Farm ein mal auf das private island und wieder zurück, der start der Farm muss mit /setspawn festgelegt sein)
    3 - PlotTP NICHT EMPFOHLEN (Am Ende der Farm mit /plottp <plot> an den Anfang der Farm gelangen)\n"""))
    if data["respawn_method"] == 3:
        data["plot_number"]=int(input("Welcher plot ist der startpunkt?\n"))
    else:
        data["plot_number"]=0
    open("config.txt","w").write(json.dumps(data))
    print("Schließe dieses fenster und führe starte es neu wenn du bereit bist mein süßer! (Schließt sich auch in 10 sekunden weil geil)")
    print("(du kannst das später in config.txt ändern.)")
    sleep(10)
    exit(0)
data=json.loads(file)
sleep(5)
pg.keyDown("W")
pg.mouseDown(button='left')
print("Wenn fertig: str+c in diesem fenster drücken <33")
while True:
    for i in range(int(data["row_amount"]/2)):
        pg.keyDown("A")
        sleep(data["time_for_row"]+(randint(0,5)/10+randint(0,10)/100))
        pg.keyUp("A")
        sleep(.2)
        pg.keyDown("D")
        sleep(data["time_for_row"]+(randint(0,5)/10+randint(0,10)/100))
        pg.keyUp("D")
    if data["respawn_method"]==1:
        pg.press("T")
        pg.write("/is")
        pg.press("ENTER")
        sleep(1.2)
        pg.press("T")
        pg.write("/warp garden")
        pg.press("ENTER")
        sleep(.75)
    elif data["respawn_method"]==2: sleep(drop_time)
    elif data["respawn_method"]==3:
        pg.press("T")
        pg.write(f'/plottp {data["respawn_method"]}')
        pg.press("ENTER")
        sleep(.75)