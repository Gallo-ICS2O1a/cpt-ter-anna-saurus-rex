# Template for Processing sketches.
scene = 1
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
        text("24    13     15     21", 80, 300)
        fill(255, 77, 77)
        textSize(16)
        rect(352,305,55,55)
        rect(217,305,55,55)
        rect(83,305,55,55)
        rect(500,305,55,55)
def mousePressed():
    global scene
    scene += 1 
    if scene == 3:
        text("The correct answer is.... 21!")
    
def mousePressed():
    global scene 
    scene += 1 
    if scene == 4:
        background(255)
        textSize(30)
        fill(172, 83, 83)
        text("What's The Weeknd's last name? ", 50, 200)
        fill(0, 0, 255)
        textSize(30)
        text("Tisfaye  Tesfaye  Sunday      Abel", 80, 300)
        fill(255, 77, 77)
        textSize(16)
        text("The correct answer is...Tesfaye!",211,500)
        rect(352,305,55,55)
        rect(217,305,55,55)
        rect(83,305,55,55)
        rect(500,305,55,55)

     
    
