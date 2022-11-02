import tkinter, random
canvas = tkinter.Canvas(width = 800, height = 800, bg='white')
canvas.pack()

def zmrzlina():
    canvas.create_oval(120, 30, 180, 90, fill='red')
    canvas.create_oval(100, 60, 160, 120, fill='yellow')
    canvas.create_oval(140, 60, 200, 120, fill='green')
    canvas.create_rectangle(100, 100, 200, 130, fill='white')
    canvas.create_line(100, 130, 150, 250, 200, 130)

def strom():
    canvas.create_rectangle(100, 100, 130, 200, fill='black')
    canvas.create_oval(80, 50, 150, 120, fill='green')
    canvas.create_line(100, 100, 120, 70, 140, 100, width=5)
    canvas.create_oval(90, 90, 110, 110, fill='red')
    canvas.create_oval(130, 90, 150, 110, fill='red')

def vzdusny_balon():
    canvas.create_oval(100, 100, 150, 150, fill='blue')
    canvas.create_rectangle(110, 200, 140, 220, fill='red')
    canvas.create_line(100, 125, 125, 200, 150, 125)

def ciarovy_kod():
    x = 100
    for i in range(30):
        sirka = random.randint(1, 10)
        canvas.create_line(x, 100, x, 400, width=sirka)
        x += 8
        print('Sirka danej ciary je: '+str(sirka))

def obrazok():
    canvas.create_rectangle(0, 0, 800, 800, fill='aqua')
    canvas.create_oval(300, 150, 800, 500, fill='yellow')
    canvas.create_rectangle(0, 300, 800, 800, fill='lime')
    canvas.create_rectangle(100, 250, 150, 400, fill='brown')
    canvas.create_oval(60, 180, 190, 310, fill='green')
    canvas.create_line(300, 250, 300, 350, width=5)
    canvas.create_line(280, 290, 320, 290, width=5)
    canvas.create_line(300, 350, 320, 380, width=5)
    canvas.create_line(300, 350, 280, 380, width=5)
    canvas.create_oval(280, 230, 320, 270, fill='black')

def baloniky():
    x = 100
    for i in range(8):
        canvas.create_oval(x, 100, x+50, 150, fill=random.choice(('yellow', 'red', 'blue', 'green', 'pink')))
        canvas.create_line(x+25, 150, 275, 250)
        x += 40

def kolotoc():
    x = 100
    for i in range(8):
        canvas.create_oval(x, 100, x+50, 150, fill=random.choice(('yellow', 'red', 'blue', 'green', 'pink')))
        canvas.create_line(x+25, 100, 275, 20)
        x += 40

def ciary_1():
    for i in range(80):
        y = random.randint(1, 799)
        nahoda = random.randint(-300, 300)
        canvas.create_line(0, y, 800, y+nahoda, fill=random.choice(('yellow', 'pink', 'red', 'blue', 'green', 'purple', 'black')), width = random.randint(1, 8))

def ciary_2():
    for i in range(80):
        x = random.randint(1, 799)
        nahoda = random.randint(-300, 300)
        canvas.create_line(x, 0, x+nahoda, 800, fill=random.choice(('yellow', 'pink', 'red', 'blue', 'green', 'purple', 'black')), width = random.randint(1, 8))

def ciary_3():
    for i in range(80):
        x = random.randint(1, 799)
        y = random.randint(1, 799)
        canvas.create_line(400, 400, x, y, fill=random.choice(('yellow', 'pink', 'red', 'blue', 'green', 'purple', 'black')), width = random.randint(1, 8))

def ostrov_s_lodkou():
    vyska = random.randint(1, 300)
    canvas.create_oval(50, 500, 250, 700, fill='brown')
    canvas.create_rectangle(0, 600, 800, 800, fill='blue')
    canvas.create_rectangle(150, 300, 300, 400, fill='lime')
    canvas.create_line(150, 500, 150, 300, 300, 300, 300, 400, 150, 400, width=6)
    canvas.create_oval(200, 325, 250, 375, fill='yellow', outline='')
    canvas.create_oval(220, 325, 270, 375, fill='lime', outline='')
    canvas.create_line(400, 550, 650, 550, 630, 620, 420, 620, 400, 550, width=5)
    canvas.create_line(525, 550, 525, 400, 580, 500, 525, 520, width=5)
    canvas.create_oval(650, 600-vyska, 750, 600-vyska+100, fill='yellow', outline='')
    canvas.create_oval(680, 600-vyska, 780, 600-vyska+100, fill='white', outline='')
    canvas.create_oval(650, 600+vyska-100, 750, 600+vyska, fill='yellow', outline='')
    canvas.create_oval(680, 600+vyska-100, 780, 600+vyska, fill='blue', outline='')

def rebrik_1():
    x = 25
    y = 0
    canvas.create_line(50, 0, 250, 800)
    canvas.create_line(150, 0, 350, 800)
    for i in range(40):
        canvas.create_line(x, y, x+150, y)
        x += 5
        y += 20

def rebrik_2():
    x = 375
    y = 0
    canvas.create_line(250, 0, 50, 800)
    canvas.create_line(350, 0, 150, 800)
    for i in range(40):
        canvas.create_line(x, y, x-150, y)
        x -= 5
        y += 20
    
def priklad10_ciary1():
    x = 0
    for i in range(41):
        canvas.create_line(x, 0, 400, 400)
        x += 20
        
def priklad10_ciary2():
    x = 0
    for i in range(41):
        canvas.create_line(0, 0, x, 400)
        x += 20

def priklad10_ciary3():
    x = 0
    for i in range(41):
        canvas.create_line(x, 0, 800, 800)
        x += 20
    
def kruzky_v_rovine():
    for i in range(20):
        x = random.randint(100, 500)
        priemer = random.randint(50, 100)
        canvas.create_oval(x-priemer/2, 200-priemer/2, x+priemer/2, 200+priemer/2, outline=random.choice(('yellow', 'blue', 'red', 'green', 'pink')), width=3)

def stvorcekovy_papier():
    for i in range(80):
        canvas.create_line(10*i, 0, 10*i, 800)
        canvas.create_line(0, 10*i, 800, 10*i)
    
def kvaple():
    for i in range(800):
        y = random.randint(20, 70)
        canvas.create_line(1*i, 0, 1*i, y, fill='green')
        canvas.create_line(1*i, 800, 1*i, 800-y, fill='green')

def kvaple_upgraded():
    for i in range(800):
        y = random.randint(20, 70)
        canvas.create_line(1*i, 0, 1*i, y, fill='green')
        canvas.create_line(1*i, 800, 1*i, 800-y, fill='green')
    def voda():
        nahoda = random.randint(5, 20)
        for i in range(nahoda):
            x = random.randint(30, 750)
            y = random.randint(200, 600)
            priemer = random.randint(50, 200)
            canvas.create_oval(x-priemer/2, y-priemer/2, x+priemer/2, y+priemer/2, fill='blue')
    def rebrik():
        canvas.create_line(0, 600, 800, 600, fill='brown', width=5)
        canvas.create_line(0, 750, 800, 750, fill='brown', width=5)
        for i in range(10):
            canvas.create_line(80*i, 600, 80*i, 750, fill='brown', width=5)
    voda()
    rebrik()

def zahrada():
    def muchotravka():
        canvas.create_oval(200, 600, 300, 700, fill='red', outline='')
        canvas.create_rectangle(200, 650, 301, 701, fill='white', outline='')
        canvas.create_oval(220, 610, 240, 630, fill='white', outline='')
        canvas.create_oval(260, 610, 280, 630, fill='white', outline='')
        canvas.create_oval(230, 640, 250, 660, fill='white', outline='')
        canvas.create_oval(270, 640, 290, 660, fill='white', outline='')
        canvas.create_rectangle(235, 650, 265, 700, fill='brown', outline='')
        canvas.create_oval(235, 680, 264, 710, fill='brown', outline='')
    def travnik():
        canvas.create_rectangle(0, 780, 800, 800, fill='green', outline='')
        for i in range(80):
            canvas.create_line(10*i, 750, 10*i, 800, fill='green', width=3)
    def slnko():
        for i in range(40):
            x = random.randint(20, 200)
            y = random.randint(20, 200)
            canvas.create_line(0, 0, x, y, fill='yellow', width = 4)
    def pozemky():
        for i in range(5):
            priemer = random.randint(30, 50)
            priemer1 = random.randint(30, 50)
            priemer2 = random.randint(30, 50)
            canvas.create_rectangle(400+(52*i), 100, 400+priemer+(52*i), 100+priemer)
            canvas.create_rectangle(400+(52*i), 152, 400+priemer1+(52*i), 152+priemer1)
            canvas.create_rectangle(400+(52*i), 204, 400+priemer2+(52*i), 204+priemer2)
            
    def jazierko():
        for i in range(20):
            canvas.create_oval(600-10*i, 500-10*i, 600+10*i, 500+10*i, outline='blue')
    muchotravka()
    travnik()
    slnko()
    pozemky()
    jazierko()
