import pyautogui as pg;from time import sleep
from  random import randint
import json
from os import system, popen, _exit, remove
drop_time=4
data={}
def get_exact_path(old_path):return popen("echo " + old_path).read().split("\n")[0]
installpath=get_exact_path('%appdata%\\bmts_macro')
def change_settings():
    data["time_for_row"]=float(input("Wie viele sekunden brauchst du für eine Reihe?\n"))
    data["row_amount"]=int(input("Wie viele rows? (MUSS EINE GRADE ZAHL SEIN WEIL JA)\n"))
    data["respawn_method"]=int(input("""Wähle eine option aus mit der du an den Anfang der farm kommst!
    1 - Lobbyhop (Am Ende der Farm ein mal auf das private island und wieder zurück, der start der Farm muss mit /setspawn festgelegt sein) [Könnte bei lags verkacken - Server restart juckt nicht]
    2 - Respawn (Am Ende der Farm runterfallen und mit /setspawn an den Anfang der Farm gelangen) [sehr sicher - server restart fickt aber]
    3 - PlotTP NICHT EMPFOHLEN (Am Ende der Farm mit /plottp <plot> an den Anfang der Farm gelangen)
    4 - GardenTP (Am Ende der Farm /warp garden um wieder an Anfang der Farm zu gelangen - mit /setspawn Anfang der Farm festlegen!) [ziemlich cool auch bei lags - server restart fickt aber]\n"""))
    if data["respawn_method"] == 3:
        data["plot_number"]=int(input("Welcher plot ist der startpunkt?\n"))
    else:
        data["plot_number"]=0
    if input("Muss shift durchgehend gedrückt sein? [Ja/Nein]\n").lower() == "ja": data["option_shift"]=True
    else: data["option_shift"]=False
    open(installpath+"\\config.txt","w").write(json.dumps(data))
    print("Schließe dieses fenster und starte das Porgramm neu wenn du bereit bist mein süßer! (Schließt sich auch in 10 sekunden weil geil)")
    print("(du kannst das später in config.txt ändern.)")
    sleep(10)
    _exit(0)
try:
    file = open(installpath+"\\config.txt").read()
except:#settings holen
    change_settings()
data=json.loads(file)
extra_shit=input("Drücke ENTER um den macro zu starten, wenn du die Einstellungen ändern möchtest schreibe 1!\n")
if extra_shit=="1": change_settings()
elif extra_shit=="2": remove(installpath+"\\version");print("Starte jetzt neu auf süß dann sollte wieder gehen")
print("Macro started in 5 Sekunden")
sleep(5)
pg.keyDown("W")
if data["option_shift"]: pg.keyDown("SHIFT")
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
        pg.keyUp("W")
        pg.mouseUp(button='left')
        pg.press("T")
        pg.write("/is")
        pg.press("ENTER")
        sleep(2)
        pg.press("T")
        pg.write("/warp garden")
        pg.press("ENTER")
        sleep(2.2)
        pg.keyDown("SHIFT")
        sleep(0.5)
        if not data["option_shift"]: pg.keyDown("SHIFT")
        pg.keyDown("W")
        pg.mouseDown(button='left')
    elif data["respawn_method"]==2: sleep(drop_time)
    elif data["respawn_method"]==3:
        pg.press("T")
        pg.write(f'/plottp {data["plot_number"]}')
        pg.press("ENTER")
        sleep(.75)
        if data["option_shift"]: pg.keyDown("SHIFT")
        pg.keyDown("W")
        pg.mouseDown(button='left')
    elif data["respawn_method"]==4:
        pg.press("T")
        pg.write("/warp garden")
        pg.press("ENTER")
        if data["option_shift"]: pg.keyDown("SHIFT")
        pg.keyDown("W")
        pg.mouseDown(button='left')