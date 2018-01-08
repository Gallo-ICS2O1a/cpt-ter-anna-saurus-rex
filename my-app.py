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
        
    if scene == 6:
        background(255)
        textSize(18)
        fill(172, 83, 83)
        text("How many McDonald's are there in Canada as of 2014?", 50, 200)
        fill(0, 0, 255)
        textSize(30)
        text("5000      1400       2400       2500", 80, 300)
        rect(352, 305, 60, 80)
        rect(217, 305, 60, 80)
        rect(83, 305, 60, 80)
        rect(500, 305, 60, 80)
        
    if scene == 7:
        fill(255, 77, 77)
        textSize(16)
        text("The correct answer is...1400!", 211, 500)
        
    if scene == 8:
        background(255)
        textSize(30)
        fill(172, 83, 83)
        text("What year was bread invented?", 50, 200)
        fill(0, 0, 255)
        textSize(30)
        text("8000", 60, 275)
        fill(0, 0, 255)
        textSize(30)
        text("BCE", 70, 300)
        fill(0, 0, 255)
        textSize(30)
        text("8500", 187, 275)
        fill(0, 0, 255)
        textSize(30)
        text("BCE", 197, 300)
        fill(0, 0, 255)
        textSize(30)
        text("7000", 324, 275)
        fill(0, 0, 255)
        textSize(30)
        text("BCE", 334, 300)
        fill(0, 0, 255)
        textSize(30)
        text("1928", 455, 300)
        rect(330, 305, 60, 80)
        rect(193, 305, 60, 80)
        rect(66, 305, 60, 80)
        rect(462, 305, 60, 80)
    
    if scene == 9:
        fill(255, 77, 77)
        textSize(16)
        text("The correct answer is...8000 BCE!", 175, 500)
        rect(217, 305, 60, 80)
        rect(83, 305, 60, 80)
        rect(500, 305, 60, 80)
        
    if scene == 7:
        fill(255, 77, 77)
        textSize(16)
        text("The correct answer is...1400!", 211, 500)

     
    
