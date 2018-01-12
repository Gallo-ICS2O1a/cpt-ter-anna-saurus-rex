# Template for Processing sketches.
scene = 1
guess = 0
box1_loc = PVector(66, 305)
box1_size = PVector(60, 80)
box2_loc = PVector(193, 305)
box2_size = PVector(60, 80)
box3_loc = PVector(330, 305)
box3_size = PVector(60, 80)
box4_loc = PVector(462, 305)
box4_size = PVector(60, 80)
def setup():
    size(600, 600)
    
def draw():
    if scene == 1:
        background(255)
        beginning = color(0, 0, 204)
        ending = color(153, 153, 255)
        for i in range(600):
            stroke(lerpColor(beginning, ending, i/600.0))
            line(0, i, width, i)
            
        title = createFont("monospace", 48)
        textFont(title)
        fill(0)
        text("The Impossible Trivia: ", 50, 200)
        subtitle = createFont("Calibri-BoldItalic", 40)
        textFont(subtitle)
        fill(0)
        text("Slang, Food, and Music", 80, 300)
        fill(30)
        textSize(20)
        text("Click anywhere to start",200,500)
        fill(0)
        textSize(15)
        text("How well do you know these impossible questions?", 50, 100)
        fill(0)
        textSize(15)
        text("Will you beat your friends?", 350, 425)
def mousePressed():
    global guess
    global scene
    global box4_loc
    global box4_size
    global box1_loc
    global box1_size
    global box2_loc
    global box2_size 
    global box3_loc
    global box3_size
    
    scene += 1
    if scene == 2:
        background(255)
        fill(0)
        textSize(30)
        text("How to Play:", 200, 100)
        fill(226,90,97)
        textSize(25)
        text("Click on the box that you think is correct.",50,200)
        fill(226,90,97)
        textSize(25)
        text("Points will be revealed at the end as well",50,225)
        fill(226,90,97)
        textSize(25)
        text("as your ranking.",50,250)
        fill(229,188,64)
        textSize(60)
        text("HAVE FUN!!!!!",75,350)
    
    if scene == 3:
        background(255)
        textSize(30)
        fill(172, 83, 83)
        text("How many Grammys did Kanye earn?", 45, 200)
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
    if scene == 4:
        if mouseX >= box4_loc.x and mouseX <= box4_loc.x + box4_size.x:
            if mouseY >= box4_loc.y and mouseY <= box4_loc.y + box4_size.y:
                fill(50, 205, 50)
                rect(462, 305, 60, 80)
                fill(50, 205, 50)
                textSize(50)
                text("21", 465, 300)
                guess += 1
        elif mouseX >= box1_loc.x and mouseX <= box1_loc.x + box1_size.x:
            if mouseY >= box1_loc.y and mouseY <= box1_loc.y + box1_size.y:
                fill(255, 0, 0)
                rect(66, 305, 60, 80)
                fill(255, 0, 0)
                textSize(50)
                text("24", 68, 300)
                guess -= 1 
        elif mouseX >= box2_loc.x and mouseX <= box2_loc.x + box2_size.x:
            if mouseY >= box2_loc.y and mouseY <= box2_loc.y + box2_size.y:
                fill(255, 0, 0)
                rect(193, 305, 60, 80)
                fill(255, 0, 0)
                textSize(50)
                text("13", 190, 300)
                guess -= 1 
        elif mouseX >= box3_loc.x and mouseX <= box3_loc.x + box3_size.x:
            if mouseY >= box3_loc.y and mouseY <= box3_loc.y + box3_size.y:
                fill(255, 0, 0)
                rect(330, 305, 60, 80)
                fill(255, 0, 0)
                textSize(50)
                text("15", 330, 300)
                guess -= 1 
                
    if scene == 5:
            fill(255, 77, 77)
            textSize(20)
            text("The correct answer is.... 21!", 150, 500)
    
    if scene == 6:
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
        
    if scene == 7:
        if mouseX >= box2_loc.x and mouseX <= box2_loc.x + box2_size.x:
            if mouseY >= box2_loc.y and mouseY <= box2_loc.y + box2_size.y:
                fill(50, 205, 50)
                rect(193, 305, 60, 80)
                fill(50, 205, 50)
                textSize(30)
                text("Tesfaye", 177, 300)
                guess += 1
        elif mouseX >= box1_loc.x and mouseX <= box1_loc.x + box1_size.x:
            if mouseY >= box1_loc.y and mouseY <= box1_loc.y + box1_size.y:
                fill(255, 0, 0)
                rect(66, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Tisfaye", 50, 300)
                guess -= 1 
        elif mouseX >= box4_loc.x and mouseX <= box4_loc.x + box4_size.x:
            if mouseY >= box4_loc.y and mouseY <= box4_loc.y + box4_size.y:
                fill(255, 0, 0)
                rect(462, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Abel", 460, 300)
                guess -= 1 
        elif mouseX >= box3_loc.x and mouseX <= box3_loc.x + box3_size.x:
            if mouseY >= box3_loc.y and mouseY <= box3_loc.y + box3_size.y:
                fill(255, 0, 0)
                rect(330, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Sunday", 314, 300)
                guess -= 1 
    
    if scene == 8:
        fill(255, 77, 77)
        textSize(20)
        text("The correct answer is...Tesfaye!", 150, 500)
        
    if scene == 9:
        background(255)
        textSize(18)
        fill(172, 83, 83)
        text("How many McDonald's are there in Canada as of 2014?", 50, 200)
        fill(0, 0, 255)
        textSize(30)
        text("5000", 63, 300)
        fill(0, 0, 255)
        textSize(30)
        text("1400", 190, 300)
        fill(0, 0, 255)
        textSize(30)
        text("2400", 327, 300)
        fill(0, 0, 255)
        textSize(30)
        text("2500", 459, 300)
        rect(330, 305, 60, 80)
        rect(193, 305, 60, 80)
        rect(66, 305, 60, 80)
        rect(462, 305, 60, 80)
        
    if scene == 10:
        if mouseX >= box2_loc.x and mouseX <= box2_loc.x + box2_size.x:
            if mouseY >= box2_loc.y and mouseY <= box2_loc.y + box2_size.y:
                fill(50, 205, 50)
                rect(193, 305, 60, 80)
                fill(50, 205, 50)
                textSize(30)
                text("1400", 190, 300)
                guess += 1
        elif mouseX >= box1_loc.x and mouseX <= box1_loc.x + box1_size.x:
            if mouseY >= box1_loc.y and mouseY <= box1_loc.y + box1_size.y:
                fill(255, 0, 0)
                rect(66, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("5000", 63, 300)
                guess -= 1 
        elif mouseX >= box4_loc.x and mouseX <= box4_loc.x + box4_size.x:
            if mouseY >= box4_loc.y and mouseY <= box4_loc.y + box4_size.y:
                fill(255, 0, 0)
                rect(462, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("2500", 459, 300)
                guess -= 1 
        elif mouseX >= box3_loc.x and mouseX <= box3_loc.x + box3_size.x:
            if mouseY >= box3_loc.y and mouseY <= box3_loc.y + box3_size.y:
                fill(255, 0, 0)
                rect(330, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("2400", 327, 300)
                guess -= 1 
        
    if scene == 11:
        fill(255, 77, 77)
        textSize(20)
        text("The correct answer is...1400!", 150, 500)
        
    if scene == 12:
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
        text("1375", 187, 300)
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
    if scene == 13:
        if mouseX >= box1_loc.x and mouseX <= box1_loc.x + box1_size.x:
            if mouseY >= box1_loc.y and mouseY <= box1_loc.y + box1_size.y:
                fill(50, 205, 50)
                rect(66, 305, 60, 80)
                fill(50, 205, 50)
                textSize(30)
                text("8000", 60, 275)
                fill(50, 205, 50)
                textSize(30)
                text("BCE", 70, 300)
                guess += 1
        elif mouseX >= box2_loc.x and mouseX <= box2_loc.x + box2_size.x:
            if mouseY >= box2_loc.y and mouseY <= box2_loc.y + box2_size.y:
                fill(255, 0, 0)
                rect(193, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("1375", 187, 300)
                guess -= 1 
        elif mouseX >= box4_loc.x and mouseX <= box4_loc.x + box4_size.x:
            if mouseY >= box4_loc.y and mouseY <= box4_loc.y + box4_size.y:
                fill(255, 0, 0)
                rect(462, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("1928", 455, 300)
                guess -= 1 
        elif mouseX >= box3_loc.x and mouseX <= box3_loc.x + box3_size.x:
            if mouseY >= box3_loc.y and mouseY <= box3_loc.y + box3_size.y:
                fill(255, 0, 0)
                rect(330, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("7000", 324, 275)
                fill(255, 0, 0)
                textSize(30)
                text("BCE", 334, 300)
                guess -= 1 
    if scene == 14:
        fill(255, 77, 77)
        textSize(20)
        text("The correct answer is...8000 BCE!", 150, 500)
       
    if scene == 15:
        background(255)
        textSize(24)
        fill(172, 83, 83)
        text("What does durry mean in Australian slang?", 50, 200)
        fill(0, 0, 255)
        textSize(30)
        text("Toilet", 55, 300)
        fill(0, 0, 255)
        textSize(30)
        fill(0, 0, 255)
        textSize(30)
        text("Friend", 180, 300)
        fill(0, 0, 255)
        textSize(25)
        fill(0, 0, 255)
        textSize(26)
        text("Cigarette", 310, 300)
        fill(0, 0, 255)
        textSize(30)
        fill(0, 0, 255)
        textSize(30)
        text("Bomb", 455, 300)
        rect(330, 305, 60, 80)
        rect(193, 305, 60, 80)
        rect(66, 305, 60, 80)
        rect(462, 305, 60, 80)
        
    if scene == 16:
        if mouseX >= box3_loc.x and mouseX <= box3_loc.x + box3_size.x:
            if mouseY >= box3_loc.y and mouseY <= box3_loc.y + box3_size.y:
                fill(50, 205, 50)
                rect(330, 305, 60, 80)
                fill(50, 205, 50)
                textSize(26)
                text("Cigarette", 310, 300)
                guess += 1
        elif mouseX >= box2_loc.x and mouseX <= box2_loc.x + box2_size.x:
            if mouseY >= box2_loc.y and mouseY <= box2_loc.y + box2_size.y:
                fill(255, 0, 0)
                rect(193, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Friend", 180, 300)
                guess -= 1 
        elif mouseX >= box4_loc.x and mouseX <= box4_loc.x + box4_size.x:
            if mouseY >= box4_loc.y and mouseY <= box4_loc.y + box4_size.y:
                fill(255, 0, 0)
                rect(462, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Bomb", 455, 300)
                guess -= 1 
        elif mouseX >= box1_loc.x and mouseX <= box1_loc.x + box1_size.x:
            if mouseY >= box1_loc.y and mouseY <= box1_loc.y + box1_size.y:
                fill(255, 0, 0)
                rect(66, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Toilet", 55, 300)
                guess -= 1 
                
    if scene == 17:
        fill(255, 77, 77)
        textSize(20)
        text("The correct answer is...Cigarette!", 150, 500)
