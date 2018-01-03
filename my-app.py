# Template for Processing sketches.
scene = 1
guess = 0
restart = 1
percentage = guess/restart * 100
def setup():
    size(600, 600)
    
def draw():
    if scene == 1:
        background(255)
        textSize(48)
        text("The Impossible Trivia: ", 50, 200)
        fill(0)
        textSize(40)
        text("Slang, Food, and Music", 80, 300)
        fill(30)
        textSize(16)
        text("Click anywhere to start",211,500)
def mousePressed():
    global scene
    scene += 1
    if scene == 2:
        background(255)
        textSize(30)
        fill(172, 83, 83)
        text("How many Grammys did Kanye earn? ", 50, 200)
        fill(0, 0, 255)
        textSize(50)
        text("24", 68, 300)
        fill(0, 0, 255)
        textSize(50)
        text("13", 190, 300)
        fill(0, 0, 255)
        textSize(50)
        text("15", 330, 300)
        fill(0, 0, 255)
        textSize(50)
        text("21", 465, 300)
        rect(330, 305, 60, 80)
        rect(193, 305, 60, 80)
        rect(66, 305, 60, 80)
        rect(462, 305, 60, 80)
        
    if mouseButton == rect(66, 305, 60, 80):
        guess += 1

    
    if scene == 3:
        fill(255, 77, 77)
        textSize(16)
        text("The correct answer is.... 21!", 50, 500)
    
    if scene == 4:
        background(255)
        textSize(30)
        fill(172, 83, 83)
        text("What's The Weeknd's last name? ", 50, 200)
        fill(0, 0, 255)
        textSize(30)
        text("Tisfaye", 50, 300)
        fill(0, 0, 255)
        textSize(30)
        text("Tesfaye", 177, 300)
        fill(0, 0, 255)
        textSize(30)
        text("Sunday", 314, 300)
        fill(0, 0, 255)
        textSize(30)
        text("Abel", 460, 300)
        rect(330, 305, 60, 80)
        rect(193, 305, 60, 80)
        rect(66, 305, 60, 80)
        rect(462, 305, 60, 80)
    
    if scene == 5:
        fill(255, 77, 77)
        textSize(16)
        text("The correct answer is...Tesfaye!", 190, 500)

     
    
