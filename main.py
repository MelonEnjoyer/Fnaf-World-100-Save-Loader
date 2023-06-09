import getpass
import shutil
from tkinter import *
import os
p = 0
def when_clicked():
    global p
    global current_slot
    p = p + 1
    a = True
    while a:
        if p == 4:
            p = 1
            a = False
        if p == 1:
            current_slot = "fnafw1"
            a = False
        if p == 2:
            current_slot = "fnafw2"
            a = False
        if p == 3:
            current_slot = "fnafw3"
            a = False
    print(current_slot)
    return

when_clicked()
username = getpass.getuser()

def full_game_100():
    f = open(f'''C:/Users/{username}/AppData/Roaming/MMFApplications/{current_slot}''', "a")
    f.write(f'''[fnafw]
newgame=0
1have=1
2have=1
3have=1
4have=1
5have=1
6have=1
7have=1
8have=1
9have=1
10have=1
11have=1
12have=1
13have=1
14have=1
15have=1
16have=1
17have=1
18have=1
19have=1
20have=1
21have=1
22have=1
23have=1
24have=1
25have=1
26have=1
27have=1
28have=1
29have=1
30have=1
31have=1
32have=1
33have=1
34have=1
35have=1
36have=1
37have=1
38have=1
39have=1
40have=1
mode=1
diff=2
s1=1
s2=40
s3=30
s4=6
s5=39
s6=32
s7=33
s8=24
started=1
locked=1
cine=9
x=1829
y=1024
area=0
seconds=21
min=17
hour=5
25next=70851
33next=27705
23next=28478
37next=70011
38next=1624
30next=26850
15next=63276
20next=72291
tokens=9999999
5next=47
8next=151
12next=66986
16next=74516
6next=74924
7next=51030
11next=54938
2next=138
31next=36248
36next=17928
29next=17148
35next=103
34next=6418
39next=40327
sw1=1
1lv=200
2lv=200
3lv=200
4lv=200
5lv=200
6lv=200
7lv=200
8lv=200
9lv=200
10lv=200
11lv=200
12lv=200
13lv=200
14lv=200
15lv=200
16lv=200
17lv=200
18lv=200
19lv=200
20lv=200
21lv=200
22lv=200
23lv=200
24lv=200
25lv=200
26lv=200
27lv=200
28lv=200
29lv=200
30lv=200
31lv=200
32lv=200
33lv=200
34lv=200
35lv=200
36lv=200
37lv=200
38lv=200
39lv=200
40lv=200
armor=100
ar2=1
ar1=1
ar3=1
ar4=1
1next=76800
24next=102060
p3=1
active1b=6
p6=1
active1=8
c2=1
active2=9
13next=85846
17next=26440
28next=39440
14next=24070
21next=12864
c1=1
active3=17
c4=1
w3=1
active4=18
p9=1
active3b=21
c5=1
18next=24194
22next=65421
26next=8417
c12=1
sw2=1
p12=1
active4b=18
3next=41140
40next=65591
active2b=12
c21=1
resetpos=0
p15=1
c9=1
c8=1
sw3=1
sw4=1
c13=1
19next=3870
27next=57238
sw5=1
key=1
sw7=1
c3=1
c7=1
sw8=1
sw6=1
c11=1
sw9=1
beatgame1=1
last=1
beatgame2=1
32next=79170
4next=2370
fish=1
p21=1
c14=1
c15=1
c19=1
c20=1
c18=1
c16=1
c6=1
c17=1
c10=1
p1=1
p2=1
p7=1
p8=1
p18=1
p17=1
p16=1
p19=1
p20=1
p14=1
p13=1
p11=1
p10=1
p5=1
p4=1
''')
    f.close()
    return


def replace_line(filename, line_number, text):
    with open(filename) as file:
        lines = file.readlines()
    if line_number <= len(lines):
        lines[line_number - 1] = text + "\n"
        with open(filename, "w") as file:
            for line in lines:
                file.write(line)


def token_999():
    word = 'tokens='
    with open(f'''C:/Users/{username}/AppData/Roaming/MMFApplications/{current_slot}''', 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            if line.find(word) != -1:
                with open(f'''C:/Users/{username}/AppData/Roaming/MMFApplications/{current_slot}''', "r+") as f:
                    d = f.readlines()
                    f.seek(0)
                    for i in d:
                        if i != lines.index(line):
                            f.write(i)
                    f.truncate()
                replace_line(f'''C:/Users/{username}/AppData/Roaming/MMFApplications/{current_slot}''', lines.index(line),"tokens=9999999999")


def backup():
    directory = "BackupSaves"
    parent_dir = f'''C:/Users/{username}/AppData/Roaming/MMFApplications'''
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    if os.path.exists(f'''C:/Users/{username}/AppData/Roaming/MMFApplications/BackupSaves'''):
        shutil.move(f'''C:/Users/{username}/AppData/Roaming/MMFApplications/{current_slot}''',
                    f'''C:/Users/{username}/AppData/Roaming/MMFApplications/BackupSaves''')
    return


def remove_current_and_replace_with_backup():
    os.remove(f'''C:/Users/{username}/AppData/Roaming/MMFApplications/{current_slot}''')
    shutil.move(f'''C:/Users/{username}/AppData/Roaming/MMFApplications/BackupSaves/{current_slot}''',
                f'''C:/Users/{username}/AppData/Roaming/MMFApplications/''')

def tk_gui():
    root = Tk()
    root.geometry('250x150')
    label = Label(root, text="FNAF WORLD SAVE 100%", font='Helvetica 14 bold', foreground="red", bg='black')
    label.pack()
    label2 = Label(root, text="Warning:Backup before loading", font='Helvetica 10 bold', foreground="red", bg='black')
    label2.pack()
    root.configure(bg='black')
    btn1 = Button(root, text='100% Save     ', bd='5', fg='white', bg='red', command=lambda: full_game_100())
    btn2 = Button(root, text='Backup          ', bd='5', fg='white', bg='red', command=lambda: backup())
    btn3 = Button(root, text='Load Backup', bd='5', fg='white', bg='red',command=lambda: remove_current_and_replace_with_backup())
    btn4 = Button(root, text='Infinite Tokens', bd='5', fg='white', bg='red', command=lambda: token_999())
    root.update_idletasks()
    btn5 = Button(root, text='Change Slot    ', bd='5', fg='white', bg='red', command=lambda: when_clicked())
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()
    btn5.pack()
    btn1.place(y=50, x=10)
    btn2.place(y=80, x=10)
    btn3.place(y=110, x=10)
    btn4.place(y=50, x=111)
    btn5.place(y=80, x=111)
    root.mainloop()
tk_gui()
