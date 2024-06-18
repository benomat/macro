import pyautogui as pg;from time import sleep
from  random import randint
import json
from os import system, popen, _exit, remove,mkdir,path,listdir
import keyboard
woohoo=False
drop_time=4
data={}
def selector(items):
    done = False
    selected = 0
    while not done:
        system("cls")
        txt = ""
        for index, item in enumerate(items):
            if index == selected:
                txt += f"(X) | {item}\n"
            else:
                txt += f"( ) | {item}\n"
        print(txt)
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name in ['nach-unten','down']:
                selected = (selected + 1) % len(items)
                while True:
                    event = keyboard.read_event()
                    if event.event_type == keyboard.KEY_UP:
                        break
            elif event.name in ['nach-oben','up']:
                selected = (selected - 1) % len(items)
                while True:
                    event = keyboard.read_event()
                    if event.event_type == keyboard.KEY_UP:
                        break
            elif event.name == 'enter':
                done = True
                break
    system("cls")
    return selected


def get_exact_path(old_path):return popen("echo " + old_path).read().split("\n")[0]
installpath=get_exact_path('%appdata%\\macro')
def change_settings():
    global selectedcfg
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
    if input("Muss W durchgehend gedrückt sein? [Ja/Nein]\n").lower() == "ja": data["press_w"]=True; data["w_time"]=float(input("wie lange bei w geradeaus laufen?\n"))
    else: data["press_w"]=False;data["w_time"]=1.4
    cfgname=input("Wie soll die config heißen?\n")
    open(installpath+"\\configs\\"+cfgname+".txt","w").write(json.dumps(data))
    print("(du kannst das später im config ordner ändern.)")
    change_selected(cfgname)
def change_selected(name):
    global selectedcfg
    with open(installpath+"\\selected.txt","w") as f:
        f.write(name)
        f.close()
    selectedcfg=name
def select_config():
    list= [config.split(".")[0] for config in listdir(installpath+"\\configs")] 
    change_selected(list[selector(list)])
while not woohoo:
    if not path.isdir(installpath+"\\configs"):
        mkdir(installpath+"\\configs")
        change_settings()
    else: 
        extra_shit=input("Drücke ENTER um den macro zu starten, wenn du die config ändern möchtest schreibe select. Wenn du eine neue erstellen möchtest schreibe new!\n")
        if extra_shit.lower().startswith("n"): change_settings()
        elif extra_shit.lower().startswith("s"): select_config();sleep(.5)
        elif extra_shit=="2": remove(installpath+"\\version");print("Starte jetzt neu auf süß dann sollte wieder gehen")
        else:
            try: selectedcfg
            except: selectedcfg=open(installpath+"\\selected.txt").read()
            woohoo=True
file = open(installpath+"\\configs\\"+selectedcfg+".txt").read()
data=json.loads(file)
print("Macro started in 5 Sekunden")
sleep(5)
if data["press_w"]: pg.keyDown("W")
if data["option_shift"]: pg.keyDown("SHIFT")
pg.mouseDown(button='left')
print("Wenn fertig: str+c in diesem fenster drücken <33")
while True:
    for i in range(int(data["row_amount"]/2)):
        pg.keyDown("A")
        sleep(data["time_for_row"]+(randint(0,5)/10+randint(0,10)/100))
        pg.keyUp("A")
        if not data["press_w"]:
            pg.keyDown("W")
            sleep(data["w_time"])
            pg.keyUp("W")
        else: sleep(.2)
        pg.keyDown("D")
        sleep(data["time_for_row"]+(randint(0,5)/10+randint(0,10)/100))
        pg.keyUp("D")
        if not data["press_w"]:
            pg.keyDown("W")
            sleep(data["w_time"])
            pg.keyUp("W")
        else: sleep(.2)
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
        if data["press_w"]:pg.keyDown("W")
        pg.mouseDown(button='left')
    elif data["respawn_method"]==2: sleep(drop_time)
    elif data["respawn_method"]==3:
        pg.press("T")
        pg.write(f'/plottp {data["plot_number"]}')
        pg.press("ENTER")
        sleep(.75)
        if data["option_shift"]: pg.keyDown("SHIFT")
        if data["press_w"]:pg.keyDown("W")
        pg.mouseDown(button='left')
    elif data["respawn_method"]==4:
        pg.press("T")
        pg.write("/warp garden")
        pg.press("ENTER")
        if data["option_shift"]: pg.keyDown("SHIFT")
        if data["press_w"]:pg.keyDown("W")
        pg.mouseDown(button='left')
