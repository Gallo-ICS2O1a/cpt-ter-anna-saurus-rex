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
    global title
    size(600, 600)
    title = createFont("Serif.bold", 50)
def draw():
    if scene == 1:
        background(255)
        beginning = color(178, 102, 255)
        ending = color(102, 102, 255)
        
        for i in range(600):
            stroke(lerpColor(beginning, ending, i/600.0))
            line(0, i, width, i)
        textFont(title, 50)
        fill(51, 0, 51)
        text("The Impossible", 100, 200)
        fill(0)
        textSize(50)
        text("Trivia", 220, 300)
        fill(30)
        textSize(20)
        text("Click anywhere to start", 200, 500)
        fill(255, 255, 102)
        textSize(15)
        text("How well do you know these impossible questions?", 50, 100)
        fill(255, 255, 102)
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
        fill(226, 90, 97)
        textSize(25)
        text("Click on the box that you think is correct.",50, 150)
        fill(226, 90, 97)
        textSize(25)
        text("Points will be revealed at the end as well",50, 175)
        fill(226, 90, 97)
        textSize(25)
        text("as your ranking.",50, 200)
        fill(226, 90, 97)
        textSize(25)
        text("Each correct answer is worth 25 points", 50, 250)
        fill(266, 90, 97)
        textSize(25)
        text("Each incorrect answer is worth 20 points", 50, 300)
        fill(229, 188, 64)
        textSize(60)
        text("HAVE FUN!!!!!", 75, 400)
    
    if scene == 3:
        background(255)
        textSize(30)
        fill(172, 83, 83)
        text("How many Grammys did", 115, 150)
        fill(172, 83, 83)
        textSize(30)
        text("Kanye West earn?", 175, 190)
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
        fill(0, 0, 255)
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
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess += 25
        elif mouseX >= box1_loc.x and mouseX <= box1_loc.x + box1_size.x:
            if mouseY >= box1_loc.y and mouseY <= box1_loc.y + box1_size.y:
                fill(255, 0, 0)
                rect(66, 305, 60, 80)
                fill(255, 0, 0)
                textSize(50)
                text("24", 68, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        elif mouseX >= box2_loc.x and mouseX <= box2_loc.x + box2_size.x:
            if mouseY >= box2_loc.y and mouseY <= box2_loc.y + box2_size.y:
                fill(255, 0, 0)
                rect(193, 305, 60, 80)
                fill(255, 0, 0)
                textSize(50)
                text("13", 190, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        elif mouseX >= box3_loc.x and mouseX <= box3_loc.x + box3_size.x:
            if mouseY >= box3_loc.y and mouseY <= box3_loc.y + box3_size.y:
                fill(255, 0, 0)
                rect(330, 305, 60, 80)
                fill(255, 0, 0)
                textSize(50)
                text("15", 330, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
                
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
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess += 25
        elif mouseX >= box1_loc.x and mouseX <= box1_loc.x + box1_size.x:
            if mouseY >= box1_loc.y and mouseY <= box1_loc.y + box1_size.y:
                fill(255, 0, 0)
                rect(66, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Tisfaye", 50, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        elif mouseX >= box4_loc.x and mouseX <= box4_loc.x + box4_size.x:
            if mouseY >= box4_loc.y and mouseY <= box4_loc.y + box4_size.y:
                fill(255, 0, 0)
                rect(462, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Abel", 460, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        elif mouseX >= box3_loc.x and mouseX <= box3_loc.x + box3_size.x:
            if mouseY >= box3_loc.y and mouseY <= box3_loc.y + box3_size.y:
                fill(255, 0, 0)
                rect(330, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Sunday", 314, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
    
    if scene == 8:
        fill(255, 77, 77)
        textSize(20)
        text("The correct answer is...Tesfaye!", 150, 500)
        
    if scene == 9:
        background(255)
        textSize(23)
        fill(172, 83, 83)
        text("Which star made an appearance in La La Land?", 50, 200)
        fill(0, 0, 255)
        textSize(30)
        text("Will", 70, 275)
        fill(0, 0, 255)
        textSize(30)
        text("Smith", 60, 300)
        fill(0, 0, 255)
        textSize(30)
        text("Chris", 187, 275)
        fill(0, 0, 255)
        textSize(30)
        text("Pine", 192, 300)
        fill(0, 0, 255)
        textSize(30)
        text("John ", 324, 275)
        fill(0, 0, 255)
        textSize(30)
        text("Legend", 306, 300)
        fill(0, 0, 255)
        textSize(30)
        text("Taryn", 455, 275)
        fill(0, 0, 255)
        textSize(30)
        text("Manning", 440, 300)
        rect(330, 305, 60, 80)
        rect(193, 305, 60, 80)
        rect(66, 305, 60, 80)
        rect(462, 305, 60, 80)
    if scene == 10:
        if mouseX >= box3_loc.x and mouseX <= box3_loc.x + box3_size.x:
            if mouseY >= box3_loc.y and mouseY <= box3_loc.y + box3_size.y:
                fill(50, 205, 50)
                rect(330, 305, 60, 80)
                fill(50, 205, 50)
                textSize(30)
                text("John ", 324, 275)
                fill(50, 205, 50)
                textSize(30)
                text("Legend", 306, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess += 25
        elif mouseX >= box2_loc.x and mouseX <= box2_loc.x + box2_size.x:
            if mouseY >= box2_loc.y and mouseY <= box2_loc.y + box2_size.y:
                fill(255, 0, 0)
                rect(193, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Chris", 187, 275)
                fill(255, 0, 0)
                textSize(30)
                text("Pine", 192, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        elif mouseX >= box4_loc.x and mouseX <= box4_loc.x + box4_size.x:
            if mouseY >= box4_loc.y and mouseY <= box4_loc.y + box4_size.y:
                fill(255, 0, 0)
                rect(462, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Taryn", 455, 275)
                fill(255, 0, 0)
                textSize(30)
                text("Manning", 440, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        elif mouseX >= box1_loc.x and mouseX <= box1_loc.x + box1_size.x:
            if mouseY >= box1_loc.y and mouseY <= box1_loc.y + box1_size.y:
                fill(255, 0, 0)
                rect(66, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Will", 70, 275)
                fill(255, 0, 0)
                textSize(30)
                text("Smith", 60, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
    if scene == 11:
        fill(255, 77, 77)
        textSize(20)
        text("The correct answer is...John Legend!", 150, 500)
        
    if scene == 12:
        background(255)
        textSize(25)
        fill(172, 83, 83)
        text("How many weeks was 'Despacito' #1", 65, 150)
        fill(172, 83, 83)
        textSize(25)
        text("on the billboard top 100 chart?", 110, 190)
        fill(0, 0, 255)
        textSize(50)
        text("21", 68, 300)
        fill(0, 0, 255)
        textSize(50)
        text("18", 190, 300)
        fill(0, 0, 255)
        textSize(50)
        text("16", 330, 300)
        fill(0, 0, 255)
        textSize(50)
        text("14", 465, 300)
        fill(0, 0, 255)
        rect(330, 305, 60, 80)
        rect(193, 305, 60, 80)
        rect(66, 305, 60, 80)
        rect(462, 305, 60, 80)
    if scene == 13:
        if mouseX >= box3_loc.x and mouseX <= box3_loc.x + box3_size.x:
            if mouseY >= box3_loc.y and mouseY <= box3_loc.y + box3_size.y:
                fill(50, 205, 50)
                rect(330, 305, 60, 80)
                fill(50, 205, 50)
                textSize(50)
                text("16", 330, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess += 25
        elif mouseX >= box1_loc.x and mouseX <= box1_loc.x + box1_size.x:
            if mouseY >= box1_loc.y and mouseY <= box1_loc.y + box1_size.y:
                fill(255, 0, 0)
                rect(66, 305, 60, 80)
                fill(255, 0, 0)
                textSize(50)
                text("21", 68, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        elif mouseX >= box2_loc.x and mouseX <= box2_loc.x + box2_size.x:
            if mouseY >= box2_loc.y and mouseY <= box2_loc.y + box2_size.y:
                fill(255, 0, 0)
                rect(193, 305, 60, 80)
                fill(255, 0, 0)
                textSize(50)
                text("18", 190, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        elif mouseX >= box4_loc.x and mouseX <= box4_loc.x + box4_size.x:
            if mouseY >= box4_loc.y and mouseY <= box4_loc.y + box4_size.y:
                fill(255, 0, 0)
                rect(462, 305, 60, 80)
                fill(255, 0, 0)
                textSize(50)
                text("14", 465, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
                
    if scene == 14:
        fill(255, 77, 77)
        textSize(20)
        text("The correct answer is... 16!", 150, 500)
                
    if scene == 15:
        background(255)
        textSize(19)
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
        
    if scene == 16:
        if mouseX >= box2_loc.x and mouseX <= box2_loc.x + box2_size.x:
            if mouseY >= box2_loc.y and mouseY <= box2_loc.y + box2_size.y:
                fill(50, 205, 50)
                rect(193, 305, 60, 80)
                fill(50, 205, 50)
                textSize(30)
                text("1400", 190, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess += 25
        elif mouseX >= box1_loc.x and mouseX <= box1_loc.x + box1_size.x:
            if mouseY >= box1_loc.y and mouseY <= box1_loc.y + box1_size.y:
                fill(255, 0, 0)
                rect(66, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("5000", 63, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        elif mouseX >= box4_loc.x and mouseX <= box4_loc.x + box4_size.x:
            if mouseY >= box4_loc.y and mouseY <= box4_loc.y + box4_size.y:
                fill(255, 0, 0)
                rect(462, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("2500", 459, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        elif mouseX >= box3_loc.x and mouseX <= box3_loc.x + box3_size.x:
            if mouseY >= box3_loc.y and mouseY <= box3_loc.y + box3_size.y:
                fill(255, 0, 0)
                rect(330, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("2400", 327, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        
    if scene == 17:
        fill(255, 77, 77)
        textSize(20)
        text("The correct answer is...1400!", 150, 500)
        
    if scene == 18:
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
    if scene == 19:
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
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess += 25
        elif mouseX >= box2_loc.x and mouseX <= box2_loc.x + box2_size.x:
            if mouseY >= box2_loc.y and mouseY <= box2_loc.y + box2_size.y:
                fill(255, 0, 0)
                rect(193, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("1375", 187, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        elif mouseX >= box4_loc.x and mouseX <= box4_loc.x + box4_size.x:
            if mouseY >= box4_loc.y and mouseY <= box4_loc.y + box4_size.y:
                fill(255, 0, 0)
                rect(462, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("1928", 455, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
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
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
    if scene == 20:
        fill(255, 77, 77)
        textSize(20)
        text("The correct answer is...8000 BCE!", 150, 500)
       
    if scene == 21:
        background(255)
        textSize(24)
        fill(172, 83, 83)
        text("What does 'Durry' mean in Australian slang?", 50, 200)
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
        
    if scene == 22:
        if mouseX >= box3_loc.x and mouseX <= box3_loc.x + box3_size.x:
            if mouseY >= box3_loc.y and mouseY <= box3_loc.y + box3_size.y:
                fill(50, 205, 50)
                rect(330, 305, 60, 80)
                fill(50, 205, 50)
                textSize(26)
                text("Cigarette", 310, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess += 25
        elif mouseX >= box2_loc.x and mouseX <= box2_loc.x + box2_size.x:
            if mouseY >= box2_loc.y and mouseY <= box2_loc.y + box2_size.y:
                fill(255, 0, 0)
                rect(193, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Friend", 180, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        elif mouseX >= box4_loc.x and mouseX <= box4_loc.x + box4_size.x:
            if mouseY >= box4_loc.y and mouseY <= box4_loc.y + box4_size.y:
                fill(255, 0, 0)
                rect(462, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Bomb", 455, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        elif mouseX >= box1_loc.x and mouseX <= box1_loc.x + box1_size.x:
            if mouseY >= box1_loc.y and mouseY <= box1_loc.y + box1_size.y:
                fill(255, 0, 0)
                rect(66, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Toilet", 55, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
                
    if scene == 23:
        fill(255, 77, 77)
        textSize(20)
        text("The correct answer is...Cigarette!", 150, 500)
        
    if scene == 24:
        background(255)
        textSize(30)
        fill(172, 83, 83)
        text("What does 'Bob's your uncle!'", 100, 150)
        textSize(30)
        fill(172, 83, 83)
        text("mean in British slang?", 145, 185)
        fill(0, 0, 255)
        textSize(25)
        text("Sucks to ", 40, 275)
        fill(0, 0, 255)
        textSize(25)
        text("be you!", 50, 300)
        fill(0, 0, 255)
        textSize(30)
        text("Cannon-", 170, 275)
        fill(0, 0, 255)
        textSize(30)
        text("ball!", 200, 300)
        fill(0, 0, 255)
        textSize(30)
        text("No way!", 310, 300)
        fill(0, 0, 255)
        textSize(30)
        text("There you ", 430, 275)
        fill(0, 0, 255)
        textSize(30)
        text("go!", 475, 300)
        rect(330, 305, 60, 80)
        rect(193, 305, 60, 80)
        rect(66, 305, 60, 80)
        rect(462, 305, 60, 80)
        
    if scene == 25:
        if mouseX >= box4_loc.x and mouseX <= box4_loc.x + box4_size.x:
            if mouseY >= box4_loc.y and mouseY <= box4_loc.y + box4_size.y:
                fill(50, 205, 50)
                rect(462, 305, 60, 80)
                fill(50, 205, 50)
                textSize(30)
                text("There you ", 430, 275)
                fill(50, 205, 50)
                textSize(30)
                text("go!", 475, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess += 25
        elif mouseX >= box2_loc.x and mouseX <= box2_loc.x + box2_size.x:
            if mouseY >= box2_loc.y and mouseY <= box2_loc.y + box2_size.y:
                fill(255, 0, 0)
                rect(193, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("Cannon-", 170, 275)
                fill(255, 0, 0)
                textSize(30)
                text("ball!", 200, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        elif mouseX >= box3_loc.x and mouseX <= box3_loc.x + box3_size.x:
            if mouseY >= box3_loc.y and mouseY <= box3_loc.y + box3_size.y:
                fill(255, 0, 0)
                rect(330, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("No way!", 310, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
        elif mouseX >= box1_loc.x and mouseX <= box1_loc.x + box1_size.x:
            if mouseY >= box1_loc.y and mouseY <= box1_loc.y + box1_size.y:
                fill(255, 0, 0)
                rect(66, 305, 60, 80)
                fill(255, 0, 0)
                textSize(25)
                text("Sucks to ", 40, 275)
                fill(255, 0, 0)
                textSize(25)
                text("be you!", 50, 300)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20
    if scene == 25:
        background(255)
        textSize(23)
        fill(172, 83, 83)
        text("When hippos are upset,their sweat turn grey", 50, 150)
        textSize(30)
        fill(0, 0, 255)
        text("TRUE", 172, 275)
        fill(0, 0, 255)
        textSize(30)
        text("FALSE", 308, 275)
        rect(330, 305, 60, 80)
        rect(193, 305, 60, 80)
        
    if scene == 25:
        if mouseX >= box3_loc.x and mouseX <= box3_loc.x + box3_size.x:
            if mouseY >= box3_loc.y and mouseY <= box3_loc.y + box3_size.y:
                fill(50, 205, 50)
                rect(330, 305, 60, 80)
                fill(50, 205, 50)
                textSize(30)
                text("FALSE", 308, 275)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess += 25
        elif mouseX >= box2_loc.x and mouseX <= box2_loc.x + box2_size.x:
            if mouseY >= box2_loc.y and mouseY <= box2_loc.y + box2_size.y:
                fill(255, 0, 0)
                rect(193, 305, 60, 80)
                fill(255, 0, 0)
                textSize(30)
                text("TRUE", 157, 275)
                fill(30)
                textSize(18)
                text("Click to continue", 430, 575)
                guess -= 20

    if scene == 26:
        fill(255, 77, 77)
        textSize(18)
        text("The correct answer is... False. Their blood turns red!", 87, 500)
    if scene == 26:
        fill(255, 77, 77)
        textSize(20)
        text("The correct answer is... There you go!", 150, 500)
        
    if scene == 27:
        score = abs(guess)
        background(0, 128, 255)
        if score >= 0 and score <= 70:
            nextstage = 71 - score
            fill(255)
            textSize(30)
            text("Congradulations!", 195, 150)
            text("You have a score of", 120, 185)
            fill(255, 255, 51)
            text(score, 420, 185)
            fill(255)
            text("and a ranking of a", 175, 220)
            fill(255, 255, 51)
            text("Beginner with training wheels", 120, 255) 
            fill(255)
            textSize(25)
            text("Only", 60, 320)
            fill(255, 255, 51)
            text(nextstage, 130, 320)
            fill(255)
            text("more points until you upgrade to", 170, 320) 
            fill(255, 255, 51)
            textSize(30)
            text("Middle-class Einstein", 170, 360)
            fill(255, 153, 153)
            textSize(40)
            text("Better Luck Next Time!!!", 90, 440)
        
        elif score >= 71 and score <= 140:
            nextstage = 140 - score
            fill(255)
            textSize(30)
            text("Congradulations!", 195, 150)
            text("You have a score of", 120, 185)
            fill(255, 255, 51)
            text(score, 420, 185)
            fill(255)
            text("and a ranking of an", 175, 220)
            fill(255, 255, 51)
            text("Middle-class Einstein", 170, 255) 
            fill(255)
            textSize(25)
            text("Only", 60, 320)
            fill(255, 255, 51)
            text(nextstage, 130, 320)
            fill(255)
            text("more points until you upgrade to", 170, 320) 
            fill(255, 255, 51)
            textSize(30)
            text("Know-It-All Wizard", 170, 360)
            fill(255, 153, 153)
            textSize(40)
            text("Better Luck Next Time!!!", 90, 440)
            
        elif score >= 141 and score <= 200:
            nextstage = 200 - score
            fill(255)
            textSize(30)
            text("Congratulations!", 195, 150)
            text("You have a score of", 120, 185)
            fill(255, 255, 51)
            text(score, 420, 185)
            fill(255)
            text("and a ranking of a", 175, 220)
            fill(255, 255, 51)
            text("Know-It-All Wizard", 170, 255) 
            fill(255)
            textSize(30)
            text("You have reached the FINAL ranking!", 50, 320)
            fill(255, 153, 153)
            textSize(40)
            text("Amazing Job!!!", 170, 440)

