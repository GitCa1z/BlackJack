import pygame, sys #provides various functions and variables that are used to manipulate different parts of the Python runtime environment.
import os # creates files and directories, management of files and directories, input, output, environment variables, process management, etc.
import random #defines a series of functions for generating or manipulating random integers

pygame.init() #initates pygame

screenheight = 720 # Sets the screen height to 720
screenwidth = 1280 # Sets the screen width to 1280
displayScreen = pygame.display.set_mode((screenwidth, screenheight)) #delcare pygame function to variable to display objects on screen

# Loads a picture into a variable which then can be displayed using the displayscreen variable functions
background_ATM = pygame.image.load('Backgrounds/Background - ATM.png').convert()
background_ATMT = pygame.image.load('Tutorial/Background - ATM.png').convert()

# .convert and .convert_alpha changes the pixel format to create a copy that will draw more faster on the screen
# .convert alpha take alpha value for images with alpha values

Background_Menu = pygame.image.load('Tutorial/Background - Game P1.png').convert()
bannerPic = pygame.image.load('UI/Banner.png').convert_alpha()
banner_deal = pygame.image.load('UI/Banner-Dealer.png').convert_alpha()
stats_Surface = pygame.image.load('UI/Stats.png').convert_alpha()
background_Tutorial_1 = pygame.image.load("Tutorial/Background - Game P1.png").convert()
background_Tutorial_2 = pygame.image.load("Tutorial/Background - Game P2.png").convert()
background_Tutorial_3 = pygame.image.load("Tutorial/Background - Game P3.png").convert()
background_Tutorial_4 = pygame.image.load("Tutorial/Background - Game P4.png").convert()
background_Tutorial_5 = pygame.image.load("Tutorial/Background - Game P5.png").convert()
background_Tutorial_6 = pygame.image.load("Tutorial/Background - Game P6.png").convert()
background_Tutorial_7 = pygame.image.load("Tutorial/Background - Game P7.png").convert()
background_Tutorial_8 = pygame.image.load("Tutorial/Background - Game P8.png").convert()
background_Menu = pygame.image.load("Backgrounds/Menu.png").convert()

# rects draw a rectangle around the object/image and can be used for collison and move via its pivot point using the x and y coordinates
# center is telling the rect which pivot point to use when handling movement/transform
banner_deal_Rect = banner_deal.get_rect(center = (640,45))
banner_Rect = bannerPic.get_rect(center = (640,473))
stats_Rect = stats_Surface.get_rect(center = (135, 249))

#loading imaages to be used at different stage in program
stick_hover = pygame.image.load('ButtonPics/Stick_Hover.png').convert_alpha()
hit_hover = pygame.image.load('ButtonPics/Hit_hover.png').convert_alpha()
buttonHit = pygame.image.load('ButtonPics/Hit.png').convert_alpha()
buttonStick = pygame.image.load('ButtonPics/Stick.png').convert_alpha()
GameButton = pygame.image.load('ButtonPics/Game_Button.png').convert_alpha()
GameButton_Hover = pygame.image.load('ButtonPics/Game_Button_Hover.png').convert_alpha()
MenuButton = pygame.image.load('ButtonPics/Menu_Button.png').convert_alpha()
MenuButton_Hover = pygame.image.load('ButtonPics/Menu_Button_Hover.png').convert_alpha()
QuitButton = pygame.image.load('ButtonPics/QUIT_Button.png').convert_alpha()
QuitButton_Hover = pygame.image.load('ButtonPics/QUIT_Button_Hover.png').convert_alpha()
doubleButton = pygame.image.load('ButtonPics/Double.png').convert_alpha()
doubleButton_Hover = pygame.image.load('ButtonPics/Double_Hover.png').convert_alpha()
atm_Button = pygame.image.load('ButtonPics/Atm_Button.png').convert_alpha()
atm_Button_Hover = pygame.image.load('ButtonPics/Atm_Button_Hover.png').convert_alpha()
playMenu = pygame.image.load("ButtonPics/Play.png").convert_alpha()
playMenuHover = pygame.image.load("ButtonPics/Play_Hover.png").convert_alpha()
tutorialButton = pygame.image.load("ButtonPics/Tutorial_Hover.png").convert_alpha()
tutorialButtonHover = pygame.image.load("ButtonPics/Tutorial.png").convert_alpha()
quitMenu = pygame.image.load("ButtonPics/QUT_HOVER.png").convert_alpha()
quitMenuHover = pygame.image.load("ButtonPics/QUIT.png").convert_alpha()

chip_1 = pygame.image.load('ButtonPics/1-chip.png').convert_alpha()
chip_1_Hover = pygame.image.load('ButtonPics/Hover_Buttons/1-chip_Hover.png').convert_alpha()
chip_5 = pygame.image.load('ButtonPics/5-chip.png').convert_alpha()
chip_5_Hover = pygame.image.load('ButtonPics/Hover_Buttons/5-chip_Hover.png').convert_alpha()
chip_10 = pygame.image.load('ButtonPics/10-chip.png').convert_alpha()
chip_10_Hover = pygame.image.load('ButtonPics/Hover_Buttons/10-chip_Hover.png').convert_alpha()
chip_25 = pygame.image.load('ButtonPics/25-chip.png').convert_alpha()
chip_25_Hover = pygame.image.load('ButtonPics/Hover_Buttons/25-chip_Hover.png').convert_alpha()
chip_50 = pygame.image.load('ButtonPics/50-chip.png').convert_alpha()
chip_50_Hover = pygame.image.load('ButtonPics/Hover_Buttons/50-chip_Hover.png').convert_alpha()
deposit_All = pygame.image.load('ButtonPics/Deposit_All.png').convert_alpha()
deposit_All_Hover = pygame.image.load('ButtonPics/Deposit_All_Hover.png').convert_alpha()
withdraw_All = pygame.image.load('ButtonPics/Withdraw_All.png').convert_alpha()
withdraw_All_Hover = pygame.image.load('ButtonPics/Withdraw_All_Hover.png').convert_alpha()
startButton = pygame.image.load('ButtonPics/Start_Button.png').convert_alpha()
startButton_Hover = pygame.image.load('ButtonPics/Start_Button_Hover.png').convert_alpha()

atm1 = pygame.image.load('ButtonPics/Atm buttons/Small_1.png').convert_alpha()
atm1m = pygame.image.load('ButtonPics/Atm buttons/Small_1-.png').convert_alpha()
atm5 = pygame.image.load('ButtonPics/Atm buttons/Small_5.png').convert_alpha()
atm5m = pygame.image.load('ButtonPics/Atm buttons/Small_5-.png').convert_alpha()
atm10 = pygame.image.load('ButtonPics/Atm buttons/Small_10.png').convert_alpha()
atm10m = pygame.image.load('ButtonPics/Atm buttons/Small_10-.png').convert_alpha()
atm25 = pygame.image.load('ButtonPics/Atm buttons/Small_25.png').convert_alpha()
atm25m = pygame.image.load('ButtonPics/Atm buttons/Small_25-.png').convert_alpha()
atm50 = pygame.image.load('ButtonPics/Atm buttons/Small_50.png').convert_alpha()
atm50m = pygame.image.load('ButtonPics/Atm buttons/Small_50-.png').convert_alpha()
atm1h = pygame.image.load('ButtonPics/Atm buttons/Atm hover/Small_1+_hover.png').convert_alpha()
atm1mh = pygame.image.load('ButtonPics/Atm buttons/Atm hover/Small_1_hover.png').convert_alpha()
atm5h = pygame.image.load('ButtonPics/Atm buttons/Atm hover/Small_5+_hover.png').convert_alpha()
atm5mh = pygame.image.load('ButtonPics/Atm buttons/Atm hover/Small_5_hover.png').convert_alpha()
atm10h = pygame.image.load('ButtonPics/Atm buttons/Atm hover/Small_10+_hover.png').convert_alpha()
atm10mh = pygame.image.load('ButtonPics/Atm buttons/Atm hover/Small_10_hover.png').convert_alpha()
atm25h = pygame.image.load('ButtonPics/Atm buttons/Atm hover/Small_25+_hover.png').convert_alpha()
atm25mh = pygame.image.load('ButtonPics/Atm buttons/Atm hover/Small_25_hover.png').convert_alpha()
atm50h = pygame.image.load('ButtonPics/Atm buttons/Atm hover/Small_50+_hover.png').convert_alpha()
atm50mh = pygame.image.load('ButtonPics/Atm buttons/Atm hover/Small_50_hover.png').convert_alpha()

chippyNormal = pygame.image.load('ChippyEmotes/Normal.png').convert_alpha()
chippyConfused = pygame.image.load('ChippyEmotes/Confused.png').convert_alpha()
chippyAngry = pygame.image.load('ChippyEmotes/Angry.png').convert_alpha()
chippyHappy = pygame.image.load('ChippyEmotes/Happy.png').convert_alpha()
chippyATM = pygame.image.load('ChippyEmotes/ATM.png').convert_alpha()
chippyChip = pygame.image.load('ChippyEmotes/Chips.png').convert_alpha()

chippyNormalR = chippyNormal.get_rect(center = (1145, 140))

#inserts music from sound folder that can be used later in code
dealerTalks = pygame.mixer.Sound('Sounds/Text_Fast.wav')
openingATM = pygame.mixer.Sound("Sounds/OpenAtm.wav")
closeATM = pygame.mixer.Sound("Sounds/CloseAtm.wav")
coinsSfx = pygame.mixer.Sound("Sounds/Coin+.wav")
noChips = pygame.mixer.Sound('Sounds/No-coins.wav')
backGround_Song = pygame.mixer.Sound('Sounds/Pixel Perfect.wav')
hoversfx = pygame.mixer.Sound('Sounds/Hover.wav')
backGround_Song2 = pygame.mixer.Sound('Sounds/Pix-Astral_bunny.WAV')
backGround_Song3 = pygame.mixer.Sound('Sounds/Jorge Hernandez - Chopsticks.mp3')
backGround_Song4 = pygame.mixer.Sound('Sounds/Skeletoni.mp3')
drawCard = pygame.mixer.Sound('Sounds/Draw.wav')
placeBet = pygame.mixer.Sound('Sounds/PlaceBet.wav')

songIndex = 0 #interated throught background music set after each background song
currentSong = 0

playlist_Duration = {}  # A set to store background music duration

#sets the sounds volume
backGround_Song.set_volume(0.1)
coinsSfx.set_volume(0.5)
noChips.set_volume(1)
closeATM.set_volume((0.7))

# A set storing the background music
background_Music = {backGround_Song, backGround_Song2, backGround_Song3, backGround_Song4}

for x in background_Music:  # interates each index in background_Music
    playlist_Duration[songIndex] = x.get_length() #get the time length of each background song in Background music and places in playlist_Duration
    songIndex+=1 #Increase the index by +1

#Create a new userevent
musicManager = pygame.USEREVENT + 1

#Creating Buttons
class button():
    def __init__(self,x,y,image,highlight,high):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.clicked = False
        self.highlight = highlight
        self.high = high
        self.playonce = 0
    def draw(self):  #draws button onto screen
        pos = pygame.mouse.get_pos() #Keeps track of mouse postion coordinates
        action = False #Variable to return true if button has been pressed
        if self.rect.collidepoint(pos): #Creates collison size of rect
            self.image = self.highlight #changes image if mouse is hovering over button
            if self.playonce == 0: #Keeps code from repeating once button is hovered over
                hoversfx.play() # plays sounds effect
                self.playonce = 1 # Returns true once hovered
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #Checks to see if player has left clicked button
                action = True #returns true
                self.clicked = True #make sure action doesn't repeat

            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False #checks to see once left click has been realsed
        elif self.rect.collidepoint != True: # checks to see if mouse is not hovering over button
            self.image = self.high #changes the image back to the orginal
            self.playonce = 0

        displayScreen.blit(self.image, (self.rect.x, self.rect.y)) #displays button where specified

        return action #return action to true

class textSurface: # Create text to be displyed on scren
    def __init__(self,variable,antialias,colour,x,y, size = 30):
        score = pygame.font.Font('04B_19__.TTF', size)  #sets the font and size of font
        self.variable = score.render(str(variable), antialias,colour) #Takes veriable and turns it into a string in the case variable is a float or intager
        self.rect = self.variable.get_rect() #creates rect for veriable
        self.rect.center = (x,y) # sets the pivot point and coordinates for rect
        self.size = size # sets size of text
    def draw(self):
        displayScreen.blit(self.variable, (self.rect.x, self.rect.y)) #displays text to screen

class SpeechBubble: #creates speech bubble for AI tutorial
    def __init__(self,text,x,y,text_size = 20):
            self.x = x  #delcares x coordinate
            self.y = y  #delcares y coordinate
            self.text_size = text_size # declares text size
            font = pygame.font.Font('pixelmix.ttf', text_size)
            self.render = font.render(text, 1, 'Black')
            self.text_rect = self.render.get_rect(midright=(self.x, self.y))
            self.inflate = self.text_rect.inflate(10, 10) # .inflate expands the rects dimentions by a declared amount
            self.outline = self.render.get_rect(midright=(self.x, self.y))
            self.outlineinflate = self.outline.inflate(15, 15)

    def drawBubble(self): #creates speech bubbles onto screen
        pygame.draw.rect(displayScreen, (0, 0, 0), self.outlineinflate) #Displays the outline rect
        pygame.draw.rect(displayScreen, (255, 255, 255), self.inflate) #displays the white box rect
        displayScreen.blit(self.render, self.text_rect) #displays string delcared within both rects


def aiupdatespeech(milliseconds): #stops the game for a delcare amount of time for player to read text
    pygame.display.update() #Updates screen with new content which has been rendered
    dealerTalks.play() #plays dealers sound
    pygame.time.wait(milliseconds) #stops the game until specified time is over

#Creates buttons using the Button class
menuPlayButton = button(480,620,playMenu,playMenuHover,playMenu)
menuTutorialButton = button(685, 620, tutorialButton,tutorialButtonHover,tutorialButton)
menuQuitButton = button(880,620,quitMenu,quitMenuHover,quitMenu)
depositButton = button(710,402,deposit_All,deposit_All_Hover,deposit_All)
WithdrawButton = button(574,402,withdraw_All,withdraw_All_Hover,withdraw_All)
menuButton = button(343,515,MenuButton,MenuButton_Hover,MenuButton)
GmenuButton = button(1145,345,MenuButton,MenuButton_Hover,MenuButton)
QuitButtons = button(1145,415,QuitButton,QuitButton_Hover,QuitButton)
gameButton = button(943,515,GameButton,GameButton_Hover,GameButton)
hit_button = button(500,600,buttonHit,hit_hover,buttonHit)
stick_button = button(780,600,buttonStick,stick_hover,buttonStick)
dubButton = button(640,600,doubleButton,doubleButton_Hover,doubleButton)
playButton = button(570,540,startButton,startButton_Hover,startButton)
atmButton = button(720,540, atm_Button,atm_Button_Hover,atm_Button)
chip_1_button = button(472,670,chip_1,chip_1_Hover,chip_1)
chip_5_button = button(558,670,chip_5,chip_5_Hover,chip_5)
chip_10_button = button(642,670,chip_10,chip_10_Hover,chip_10)
chip_25_button = button(722,670,chip_25,chip_25_Hover,chip_25)
chip_50_button = button(802,670,chip_50,chip_50_Hover,chip_50)

at1b = button(458, 478,atm1,atm1h,atm1)
at1mb = button(458, 558,atm1m,atm1mh,atm1m)
at5b = button(548, 478,atm5,atm5h,atm5)
at5mb = button(548, 558,atm5m,atm5mh,atm5m)
at10b = button(640, 478,atm10,atm10h,atm10)
at10mb = button(640, 558,atm10m,atm10mh,atm10m)
at25b = button(730, 478,atm25,atm25h,atm25)
at25mb = button(730, 558,atm25m,atm25mh,atm25m)
at50b = button(820, 478,atm50,atm50h,atm50)
at50mb = button(820, 558,atm50m,atm50mh,atm50m)

#Creates speech bubbles using the speechbubbles class
AiSpeech1 = SpeechBubble("Oh hello!",1000,50)
AiSpeech2 = SpeechBubble("It's a pleasure to meet you, my name is Chippy!",1000,50)
AiSpeech3 = SpeechBubble("I Shall be your dealer for this session.",1000,50)
AiSpeech4 = SpeechBubble("Is this your first time playing?.",1000,50)
AiSpeech5 = SpeechBubble("No worries I will show you the ropes :)",1000,50)
AiSpeech6 = SpeechBubble("The objective of blackjack is to beat the dealer and earning chips",1000,50,)
AiSpeech7 = SpeechBubble("You achieve this by scoring higher than the dealer or the dealer busts",1000,50,18)
AiSpeech8 = SpeechBubble("The dealer will go bust if he scores higher than 21 making you the winner",1000,50,18)
AiSpeech9 = SpeechBubble("You'll bust as well if you score over 21",1000,50)
AiSpeech10 = SpeechBubble("The game will end in a tie if both players bust or score the same score",1000,50,18)
AiSpeech11 = SpeechBubble("The panel on the left displays your board stats",1000,50,18)
AiSpeech12 = SpeechBubble("The chips set will increase depending on how much you will bet on a hand",1000,50,18)
AiSpeech13 = SpeechBubble("you can place chips by clicking on the chips below",1000,50,18)
AiSpeech14 = SpeechBubble("The double button will double you set value but can only draw one card",1000,50,18)
AiSpeech15 = SpeechBubble("for now you have 0 chips to play with indicated by the red zero value",1000,50,18)
AiSpeech16 = SpeechBubble("Lets change that.",1000,50,18)
AiSpeech17 = SpeechBubble("Click the atm button to open your bank",1000,50,)
Aiwin = SpeechBubble("You win! congratulations",1000,50)
Ailost = SpeechBubble("Better luck next time!",1000,50)
Aidraw = SpeechBubble("Draw!",1000,50)

AiSpeech1ATM = SpeechBubble("This is your bank.",1000,50)
AiSpeech2ATM = SpeechBubble("The Display on the left is the chips in your account",1000,50)
AiSpeech3ATM = SpeechBubble("Whilst the display on the right displays the chips you currently have",1000,50, 20)
AiSpeech4ATM = SpeechBubble("The buttons below will withdraw or deposit chips from your bank",1000,50, 20)
AiSpeech5ATM = SpeechBubble("The + button will add chips for you to play with",1000,50)
AiSpeech6ATM = SpeechBubble("Whilst the - button will take chips away and store them into the bank",1000,50,20)
AiSpeech7ATM = SpeechBubble("The home button on the left will take you back to the menu",1000,50,20)
AiSpeech8ATM = SpeechBubble("Whilst the Joycon button on the right will take you back to the game table",1000,50,18)
AiSpeech9ATM = SpeechBubble("Try taking some chips out of the bank and heading back to table.",1000,50,20)


chip_color = 'White' #set the colour of chip balance back to white when not valued at 0
chip_Bank = 250 #players bank with a preset of 250 chips the player can play with
players_chips = 0 #Players balance when playing throughout the game
setting_bet = 0 #Chip bet when playing a game
visiablePlayButton = True #Hides the menus play button during the tutorial
introduciton = True #Plays AI tutorial if true
inGame = True #Checks to see if the player is playing  a round
placed_Bets = True #Checks to see if player has placed any bets before starting a round
endgame = False  #Checks to see if a round has ended
bust = False #Checks to see if the player has bust
aiStick = False #Checks to see if the ai has stuck
aiBust = False #Checks to see if the ai has bust
runonce = True #A run once function that runs if equal to true
p1_x_offset = 0 # delcares player one card offset to 0
p2_x_offset = 0 # delcares player two card offset to 0
new = 0 #Iterates once a new game has started giving both players two cards each exiting loop once achieved
newgame = False # checks to see if a newgame has started
currentPlayer = 1  #set the current player
currentstate = 'Menu' # set the current state
p1_cardScore = 0 #player one total card score when drawing cards
p2_cardScore = 0 #player two total card score when drawing cards
card_images = {} #Delcares a dictionary
suits = ['c', 'd', 'h', 's'] # delcares a tuple with four indexes
ranks = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'] #declares tuple with 13 indexes

set_Bets = textSurface(setting_bet, True, 'White', 140, 375)

for suit in suits: #for loop that interate through suits tuple
    for rank in ranks: #for loop that iterates through ranks tuple
        image_path = os.path.join("cards", f"{suit}{rank}.png") #selects a image withing the cards folder depending on suit and rank and store it into a variable
        original_image = pygame.image.load(image_path) #creates piture into variable
        scaled_image = pygame.transform.scale(original_image, (112, 150))  #scale picture
        card_images[(rank, suit)] = scaled_image #sets the key and value in dictionary

 #seperates key and value inside from a  dictionary and delcares them into two seperate variables randomly
card_key, card_value = random.choice(list(card_images.items()))

def restackCheck(): # checks to see if the deck is at 0 if so then refill the deck
    if len(card_images) == 0:  #checks the lenth of the card_images dictionary
        for suit in suits:
            for rank in ranks:
                image_path = os.path.join("cards", f"{suit}{rank}.png")
                original_image = pygame.image.load(image_path)
                scaled_image = pygame.transform.scale(original_image, (112, 150))
                card_images[(rank, suit)] = scaled_image

def Introduction(): #Plays the AI tutorial
    global runonce #Makes runone global scope instead of local

    if currentstate == "Game": #checks current state = game
        if runonce:
            #Actives events with the song duration as the set timer
            pygame.time.set_timer(musicManager, int(playlist_Duration.get(currentSong)) * 1000, False)
            backGround_Song.play()
            runonce = False
        displayScreen.blit(background_Tutorial_1, (0, 0)) #displays image to screen
        displayScreen.blit(chippyNormal, chippyNormalR)
        AiSpeech1.drawBubble()
        aiupdatespeech(3000) #calls a function with the paramater of delayed time in milliseconds
        displayScreen.blit(background_Tutorial_1, (0, 0))
        displayScreen.blit(chippyHappy, chippyNormalR)
        AiSpeech2.drawBubble()
        aiupdatespeech(3000)
        displayScreen.blit(background_Tutorial_1, (0, 0))
        displayScreen.blit(chippyNormal, chippyNormalR)
        AiSpeech3.drawBubble()
        aiupdatespeech(3000)
        displayScreen.blit(background_Tutorial_1, (0, 0))
        displayScreen.blit(chippyConfused, chippyNormalR)
        AiSpeech4.drawBubble()
        aiupdatespeech(3000)
        displayScreen.blit(background_Tutorial_1, (0, 0))
        displayScreen.blit(chippyHappy, chippyNormalR)
        AiSpeech5.drawBubble()
        aiupdatespeech(3000)
        displayScreen.blit(background_Tutorial_1, (0, 0))
        displayScreen.blit(chippyChip, chippyNormalR)
        AiSpeech6.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_Tutorial_2, (0, 0))
        displayScreen.blit(chippyNormal, chippyNormalR)
        AiSpeech7.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_Tutorial_2, (0, 0))
        displayScreen.blit(chippyNormal, chippyNormalR)
        AiSpeech8.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_Tutorial_3, (0, 0))
        displayScreen.blit(chippyNormal, chippyNormalR)
        AiSpeech9.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_Tutorial_1, (0, 0))
        displayScreen.blit(chippyNormal, chippyNormalR)
        AiSpeech10.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_Tutorial_1, (0, 0))
        displayScreen.blit(chippyNormal, chippyNormalR)
        AiSpeech11.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_Tutorial_4, (0, 0))
        displayScreen.blit(chippyNormal, chippyNormalR)
        AiSpeech12.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_Tutorial_5, (0, 0))
        displayScreen.blit(chippyNormal, chippyNormalR)
        AiSpeech13.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_Tutorial_6, (0, 0))
        displayScreen.blit(chippyNormal, chippyNormalR)
        AiSpeech14.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_Tutorial_7, (0, 0))
        displayScreen.blit(chippyNormal, chippyNormalR)
        AiSpeech15.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_Tutorial_1, (0, 0))
        displayScreen.blit(chippyNormal, chippyNormalR)
        AiSpeech16.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_Tutorial_8, (0, 0))
        displayScreen.blit(chippyATM, chippyNormalR)
        AiSpeech17.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_Tutorial_1, (0, 0))
        displayScreen.blit(chippyATM, chippyNormalR)


    if currentstate == 'ATM':
        global introduciton

        displayScreen.blit(background_ATMT, (0, 0))
        AiSpeech1ATM.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_ATMT, (0, 0))
        AiSpeech2ATM.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_ATMT, (0, 0))
        AiSpeech3ATM.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_ATMT, (0, 0))
        AiSpeech4ATM.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_ATMT, (0, 0))
        AiSpeech5ATM.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_ATMT, (0, 0))
        AiSpeech6ATM.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_ATMT, (0, 0))
        AiSpeech7ATM.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_ATMT, (0, 0))
        AiSpeech8ATM.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_ATMT, (0, 0))
        AiSpeech9ATM.drawBubble()
        aiupdatespeech(4000)
        displayScreen.blit(background_ATM, (0, 0))

        introduciton = False
def textRender():
    playersScoreText = textSurface(p1_cardScore, True, 'White', 645, 480)
    dealerScoreText = textSurface(p2_cardScore,True,"White",645,41)
    players_Bank = textSurface(chip_Bank,True,'White',140,155)
    set_Bets = textSurface(setting_bet,True,'White',140,375)
    player_chip_amount = textSurface(players_chips,True,'White', 820,200)

    if currentstate == 'Game':
        playersScoreText.draw() #draws players score on screen
        dealerScoreText.draw() #draws dealers score on screen
        players_Bank.draw()
        set_Bets.draw()
    elif currentstate == 'ATM':
        players_Bank.rect.x = 440 #changing the text coordinates if state = ATM
        players_Bank.rect.y = 190
        players_Bank.size = 500
        players_Bank.draw()
        player_chip_amount.draw()
def check_Score():
    global aiStick,aiBust,currentPlayer, endgame,bust

    if currentPlayer == 1 and p1_cardScore > 21:  #Check to see if player one has bust
        bust = True
        currentPlayer = 2
        pygame.display.update()
    if currentPlayer == 2:
        if p2_cardScore >= 16 and p2_cardScore <= 21: # checks to see if AI score is between 16 and 21
            aiStick = True
            endgame = True
        elif p2_cardScore > 21:  #checks to see if AI has bust
            aiBust = True
            endgame = True
    if endgame: #Checks to see when the AI has either stuck or bust
        winCondition(p1_cardScore, p2_cardScore) #calls the winCondition fuction passing the players total card score has paramters
def winCondition(p1_cardscore, p2_cardscore): # checks players score against each other
    global p1_cardScore,p2_cardScore,players_chips,setting_bet

    dealerScoreText = textSurface(p2_cardScore, True, "White", 645, 41)
    playersScoreText = textSurface(p1_cardScore, True, 'White', 645, 480)

    if p1_cardscore > p2_cardscore and bust == False: #Checks to see if player score is higher than Ai if not bust
        print("Win") #Debug testing
        displayScreen.blit(banner_deal, banner_deal_Rect)
        displayScreen.blit(bannerPic, banner_Rect)
        dealerScoreText.draw()
        playersScoreText.draw()
        displayScreen.blit(chippyHappy, chippyNormalR)
        Aiwin.drawBubble()
        dealerTalks.play()
        players_chips += setting_bet * 2 # doubles the placed bet and add it to the players balance
        pygame.display.update()
        pygame.time.delay(3000)
        newGame()

    elif p1_cardscore < p2_cardscore and aiBust: #Checks to see if the players score is less than the AI whilst bust
        print("Win")
        displayScreen.blit(banner_deal, banner_deal_Rect)
        displayScreen.blit(bannerPic, banner_Rect)
        dealerScoreText.draw()
        playersScoreText.draw()
        displayScreen.blit(chippyHappy, chippyNormalR)
        Aiwin.drawBubble()
        dealerTalks.play()
        players_chips += setting_bet * 2
        pygame.display.update()
        pygame.time.delay(3000)

        newGame()

    elif p1_cardscore < p2_cardscore and aiBust == False and bust == False: #Checks to see if players score is less than AI
        print("Lost")
        displayScreen.blit(banner_deal, banner_deal_Rect)
        displayScreen.blit(bannerPic, banner_Rect)
        dealerScoreText.draw()
        playersScoreText.draw()
        displayScreen.blit(chippyAngry, chippyNormalR)
        Ailost.drawBubble()
        dealerTalks.play()

        pygame.display.update()
        pygame.time.delay(3000)
        newGame()

    elif p1_cardscore > p2_cardscore and bust and aiBust == False: #Checks to see if players score is higher than AI but bust
        print("Lost")
        displayScreen.blit(banner_deal, banner_deal_Rect)
        displayScreen.blit(bannerPic, banner_Rect)
        dealerScoreText.draw()
        playersScoreText.draw()
        displayScreen.blit(chippyAngry, chippyNormalR)
        Ailost.drawBubble()
        dealerTalks.play()
        pygame.display.update()
        pygame.time.delay(3000)
        newGame()

    elif p1_cardscore == p2_cardscore and bust == False and aiBust == False: #Checks to see if both players havent bust but equal score
        print("Draw")
        displayScreen.blit(banner_deal, banner_deal_Rect)
        displayScreen.blit(bannerPic, banner_Rect)
        dealerScoreText.draw()
        playersScoreText.draw()
        displayScreen.blit(chippyConfused, chippyNormalR)
        Aidraw.drawBubble()
        dealerTalks.play()
        players_chips += setting_bet #Returns setting bet back to player
        pygame.display.update()
        pygame.time.delay(3000)
        newGame()

    elif p1_cardscore > 21 and p2_cardscore > 21 and bust and aiBust: #Check to see if both player and AI have bust
        print("Draw")
        displayScreen.blit(banner_deal, banner_deal_Rect)
        displayScreen.blit(bannerPic, banner_Rect)
        dealerScoreText.draw()
        playersScoreText.draw()
        displayScreen.blit(chippyConfused, chippyNormalR)
        Aidraw.drawBubble()
        dealerTalks.play()
        players_chips += setting_bet
        pygame.display.update()
        pygame.time.delay(3000)
        newGame()
def chip_Calculator(chip_input,player_Chips): #Checks if the player has the currect balance for setting bets
    global players_chips, setting_bet

    match chip_input: #checks value when player hits one of the chips button and compares it against cases
        case 1:
            if players_chips <= 0: # checks if players current balance is less or equal to 0
                print('you dont have enough!')
                noChips.play()

            elif players_chips >= 1:  #Check if players current balance is greater or equal to one

                players_chips -= 1  #Takes one value of players balance
                setting_bet += 1    #Add plus 1 to setting bets value
        case 5:
            if players_chips < 5:
                print('you dont have enough!')
                noChips.play()
            elif players_chips >= 5:
                players_chips -= 5
                setting_bet += 5
        case 10:
            if players_chips < 10:
                print('you dont have enough!')
                noChips.play()
            elif players_chips >= 10:
                players_chips -= 10
                setting_bet += 10
        case 25:
            if players_chips < 25:
                noChips.play()
                print('you dont have enough!')
            elif players_chips >= 25:
                players_chips -= 25
                setting_bet += 25
        case 50:
            if players_chips < 50:
                print('you dont have enough!')
                noChips.play()
            elif players_chips >= 50:
                players_chips -= 50
                setting_bet += 50
def newGame():
    global p1_cardScore,p2_cardScore,setting_bet,new,currentPlayer,newgame,endgame,aiStick,aiBust
    global p1_x_offset,p2_x_offset,bust

    restackCheck()  #Call the restackCheck function

    #Sets all values back to defaults
    endgame = False
    displayScreen.blit(Background_Menu, (0, 0))
    displayScreen.blit(chippyNormal, chippyNormalR)
    p1_x_offset = 0
    p2_x_offset = 0
    p1_cardScore = 0
    p2_cardScore = 0
    setting_bet = 0
    new = 0
    currentPlayer = 1
    aiBust = False
    aiStick = False
    newgame = False
    bust = False

def card_Score(cardscore): #checks the card that has been drawn and adds the value to the players or AI cardscore
    global p1_cardScore, p2_cardScore

    match cardscore:
        case ('01', 'h'):
            if currentPlayer == 1:
                p1_cardScore += 1
            elif currentPlayer == 2:
                p2_cardScore += 1
        case ('02', 'h'):
            if currentPlayer == 1:
                p1_cardScore += 2
            elif currentPlayer == 2:
                p2_cardScore += 2
        case ('03', 'h'):
            if currentPlayer == 1:
                p1_cardScore += 3
            elif currentPlayer == 2:
                p2_cardScore += 3
        case ('04', 'h'):
            if currentPlayer == 1:
                p1_cardScore += 4
            elif currentPlayer == 2:
                p2_cardScore += 4
        case ('05', 'h'):
            if currentPlayer == 1:
                p1_cardScore += 5
            elif currentPlayer == 2:
                p2_cardScore += 5
        case ('06', 'h'):
            if currentPlayer == 1:
                p1_cardScore += 6
            elif currentPlayer == 2:
                p2_cardScore += 6
        case ('07', 'h'):
            if currentPlayer == 1:
                p1_cardScore += 7
            elif currentPlayer == 2:
                p2_cardScore += 7
        case ('08', 'h'):
            if currentPlayer == 1:
                p1_cardScore += 8
            elif currentPlayer == 2:
                p2_cardScore += 8
        case ('09', 'h'):
            if currentPlayer == 1:
                p1_cardScore += 9
            elif currentPlayer == 2:
                p2_cardScore += 9
        case ('10', 'h'):
            if currentPlayer == 1:
                p1_cardScore += 10
            elif currentPlayer == 2:
                p2_cardScore += 10
        case ('11', 'h'):
            if currentPlayer == 1:
                p1_cardScore += 10
            elif currentPlayer == 2:
                p2_cardScore += 10
        case ('12', 'h'):
            if currentPlayer == 1:
                p1_cardScore += 10
            elif currentPlayer == 2:
                p2_cardScore += 10
        case ('13', 'h'):
            if currentPlayer == 1:
                p1_cardScore += 10
            elif currentPlayer == 2:
                p2_cardScore += 10
        case ('01', 'd'):
            if currentPlayer == 1:
                p1_cardScore += 1
            else:
                p2_cardScore += 1
        case ('02', 'd'):
            if currentPlayer == 1:
                p1_cardScore += 2
            else:
                p2_cardScore += 2
        case ('03', 'd'):
            if currentPlayer == 1:
                p1_cardScore += 3
            else:
                p2_cardScore += 3
        case ('04', 'd'):
            if currentPlayer == 1:
                p1_cardScore += 4
            else:
                p2_cardScore += 4
        case ('05', 'd'):
            if currentPlayer == 1:
                p1_cardScore += 5
            else:
                p2_cardScore += 5
        case ('06', 'd'):
            if currentPlayer == 1:
                p1_cardScore += 6
            else:
                p2_cardScore += 6
        case ('07', 'd'):
            if currentPlayer == 1:
                p1_cardScore += 7
            else:
                p2_cardScore += 7
        case ('08', 'd'):
            if currentPlayer == 1:
                p1_cardScore += 8
            else:
                p2_cardScore += 8
        case ('09', 'd'):
            if currentPlayer == 1:
                p1_cardScore += 9
            else:
                p2_cardScore += 9
        case ('10', 'd'):
            if currentPlayer == 1:
                p1_cardScore += 10
            else:
                p2_cardScore += 10
        case ('11', 'd'):
            if currentPlayer == 1:
                p1_cardScore += 10
            else:
                p2_cardScore += 10
        case ('12', 'd'):
            if currentPlayer == 1:
                p1_cardScore += 10
            else:
                p2_cardScore += 10
        case ('13', 'd'):
            if currentPlayer == 1:
                p1_cardScore += 10
            else:
                p2_cardScore += 10
        case ('01', 's'):
            if currentPlayer == 1:
                p1_cardScore += 1
            else:
                p2_cardScore += 1
        case ('02', 's'):
            if currentPlayer == 1:
                p1_cardScore += 2
            else:
                p2_cardScore += 2
        case ('03', 's'):
            if currentPlayer == 1:
                p1_cardScore += 3
            else:
                p2_cardScore += 3
        case ('04', 's'):
            if currentPlayer == 1:
                p1_cardScore += 4
            else:
                p2_cardScore += 4
        case ('05', 's'):
            if currentPlayer == 1:
                p1_cardScore += 5
            else:
                p2_cardScore += 5
        case ('06', 's'):
            if currentPlayer == 1:
                p1_cardScore += 6
            else:
                p2_cardScore += 6
        case ('07', 's'):
            if currentPlayer == 1:
                p1_cardScore += 7
            else:
                p2_cardScore += 7
        case ('08', 's'):
            if currentPlayer == 1:
                p1_cardScore += 8
            else:
                p2_cardScore += 8
        case ('09', 's'):
            if currentPlayer == 1:
                p1_cardScore += 9
            else:
                p2_cardScore += 9
        case ('10', 's'):
            if currentPlayer == 1:
                p1_cardScore += 10
            else:
                p2_cardScore += 10
        case ('11', 's'):
            if currentPlayer == 1:
                p1_cardScore += 10
            else:
                p2_cardScore += 10
        case ('12', 's'):
            if currentPlayer == 1:
                p1_cardScore += 10
            else:
                p2_cardScore += 10
        case ('13', 's'):
            if currentPlayer == 1:
                p1_cardScore += 10
            else:
                p2_cardScore += 10
        case ('01', 'c'):
            if currentPlayer == 1:
                p1_cardScore += 1
            else:
                p2_cardScore += 1
        case ('02', 'c'):
            if currentPlayer == 1:
                p1_cardScore += 2
            else:
                p2_cardScore += 2
        case ('03', 'c'):
            if currentPlayer == 1:
                p1_cardScore += 3
            else:
                p2_cardScore += 3
        case ('04', 'c'):
            if currentPlayer == 1:
                p1_cardScore += 4
            else:
                p2_cardScore += 4
        case ('05', 'c'):
            if currentPlayer == 1:
                p1_cardScore += 5
            else:
                p2_cardScore += 5
        case ('06', 'c'):
            if currentPlayer == 1:
                p1_cardScore += 6
            else:
                p2_cardScore += 6
        case ('07', 'c'):
            if currentPlayer == 1:
                p1_cardScore += 7
            else:
                p2_cardScore += 7
        case ('08', 'c'):
            if currentPlayer == 1:
                p1_cardScore += 8
            else:
                p2_cardScore += 8
        case ('09', 'c'):
            if currentPlayer == 1:
                p1_cardScore += 9
            else:
                p2_cardScore += 9
        case ('10', 'c'):
            if currentPlayer == 1:
                p1_cardScore += 10
            else:
                p2_cardScore += 10
        case ('11', 'c'):
            if currentPlayer == 1:
                p1_cardScore += 10
            else:
                p2_cardScore += 10
        case ('12', 'c'):
            if currentPlayer == 1:
                p1_cardScore += 10
            else:
                p2_cardScore += 10
        case ('13', 'c'):
            if currentPlayer == 1:
                p1_cardScore += 10
            else:
                p2_cardScore += 10
def draw_card(x_offset): # draws a random card from deck with the player or AI offset as an argument
    card_key = random.choice(list(card_images.keys())) #converts the dictionary into a list and takes a random key value from that list
    space_between_cards = 50 # delcares an integer which makes a space between cards so they dont stack
    p1_initial_x = 400 #setting players cards x location
    p1_initial_y = 270 #setting players cards y location
    p2_initial_x = 400
    p2_initial_y = 90

    if currentPlayer == 1:
        displayScreen.blit(card_images[card_key], (p1_initial_x + x_offset, p1_initial_y))
        x_offset = space_between_cards #adding value to x_offset
        card_Score(card_key) #calls the cards score with the key as a paramater
        card_images.pop(card_key)  #deletes card from deck
        print(len(card_images)) #debugging checking length of deck once card has popped

    elif currentPlayer == 2 and aiStick == False and aiBust == False: #Ai taking their turn and drawing cards
        displayScreen.blit(card_images[card_key], (p2_initial_x + x_offset, p2_initial_y))
        x_offset = space_between_cards
        pygame.display.update()
        card_Score(card_key)
        card_images.pop(card_key)
        print(len(card_images))
    return x_offset

while True: #Main game loop
    for event in pygame.event.get(): #interates event functions in event.get
        if event.type == pygame.QUIT: #checks to see if the player clicks the close/quit button on window
            pygame.quit() #exit game
            sys.exit() # terminates the execution of a Python program without error

        if event.type == musicManager: #activates on the user event has been triggered switching indexes once song is finished
            if currentSong == 0:
                backGround_Song2.play()
                currentSong += 1
                print(currentSong)
                print("first song start")
            elif currentSong == 1:
                print(currentSong)
                backGround_Song3.play()
                currentSong += 1
                print("second song finished")
            elif currentSong == 2:
                backGround_Song4.play()
                currentSong += 1
                print("Third song finished")
            elif currentSong == 3:
                backGround_Song.play()
                currentSong = 0
                print("Third song finished")

    if currentstate == 'ATM':
        if introduciton: #checks to see if introduction = True
            Introduction() #calls introduction function

        displayScreen.blit(background_ATM, (0, 0))

        textRender()#renders text to screen

        #Drawing buttons atm buttons onto screen

        if at1b.draw(): #draws atm buttons to screen
            if chip_Bank > 0:
                coinsSfx.play()
                chip_Bank -= 1
                players_chips += 1
            else: #checks to see if players has deposit
                noChips.play()
                print("bank don't have enough")

        if at1mb.draw():
            if players_chips > 0:
                coinsSfx.play()
                chip_Bank += 1
                players_chips -= 1
            else:  #Checks to see if player has enough to withdraw
                noChips.play()
                print("you cant deposit anymore")

        if at5b.draw():
            if chip_Bank >= 5:
                coinsSfx.play()
                chip_Bank -= 5
                players_chips += 5
            else:
                noChips.play()
                print("bank don't have enough")

        if at5mb.draw():
            if players_chips >= 5:
                coinsSfx.play()
                chip_Bank += 5
                players_chips -= 5
            else:
                noChips.play()
                print("you need more deposit!")

        if at10b.draw():
            if chip_Bank >= 10:
                coinsSfx.play()
                chip_Bank -= 10
                players_chips += 10
            else:
                noChips.play()
                print("bank don't have enough")

        if at10mb.draw():
            if players_chips >= 10:
                coinsSfx.play()
                chip_Bank += 10
                players_chips -= 10
            else:
                noChips.play()
                print("you need more to deposit")

        if at25b.draw():
            if chip_Bank >= 25:
                coinsSfx.play()
                chip_Bank -= 25
                players_chips += 25
            else:
                noChips.play()
                print("bank don't have enough")

        if at25mb.draw():
            if players_chips >= 25:
                coinsSfx.play()
                chip_Bank += 25
                players_chips -= 25
            else:
                noChips.play()
                print("you need more deposit")

        if at50b.draw():
            if chip_Bank >= 50:
                coinsSfx.play()
                chip_Bank -= 50
                players_chips += 50
            else:
                noChips.play()
                print("you do not have enough")

        if at50mb.draw():
            if players_chips >= 50:
                coinsSfx.play()
                chip_Bank += 50
                players_chips -= 50
            else:
                noChips.play()
                print("you need more deposit")

        if depositButton.draw():
            chip_Bank += players_chips
            players_chips = 0
            coinsSfx.play()

        if WithdrawButton.draw():
            players_chips += chip_Bank
            chip_Bank = 0
            coinsSfx.play()

        #draws menubutton onto screen
        if menuButton.draw():
            currentstate = "Menu"

        #draws game button onto screen
        if gameButton.draw():
            currentstate = 'Game'
            closeATM.play()
            displayScreen.blit(Background_Menu, (0, 0))
            displayScreen.blit(chippyNormal, chippyNormalR)
            pygame.display.update()



    if currentstate == 'Menu': #checks if current state = Menu
        introduciton = True
        visiablePlayButton = True

        displayScreen.blit(background_Menu, (0, 0))

        #Draws menu,tutorial and play buttons onto screen
        if menuQuitButton.draw():
            sys.exit()

        if menuTutorialButton.draw():
            currentstate = "Game"
            displayScreen.blit(background_Tutorial_1, (0, 0))
            displayScreen.blit(chippyNormal, chippyNormalR)
            visiablePlayButton = False
            if introduciton:
                Introduction()

        if visiablePlayButton:
            if menuPlayButton.draw():
                currentstate = "Game"
                if runonce:
                    pygame.time.set_timer(musicManager, int(playlist_Duration.get(currentSong)) * 1000, False)
                    backGround_Song.play()
                    runonce = False
                displayScreen.blit(background_Tutorial_1, (0, 0))
                displayScreen.blit(chippyNormal, chippyNormalR)
                introduciton = False

    if currentstate == 'Game':

        pygame.display.update()

        if inGame: # checks to see if the player is playing a round of blackjack and displays default scores
            displayScreen.blit(stats_Surface, stats_Rect)
            displayScreen.blit(bannerPic, banner_Rect)
            displayScreen.blit(banner_deal, banner_deal_Rect)

            textRender()

            player_Chips = textSurface(players_chips, True, chip_color, 140, 268)
            player_Chips.draw()

            if players_chips <= 0:  #checks to see if players balance is equal to 0
                chip_color = 'Red'

            else:  # checks to see if players balance is above 0
                chip_color = 'White'

            #draws hit button onto screen
            if hit_button.draw():
                if setting_bet > 0 and newgame: #check to see if the player is playing a round
                    drawCard.play()
                    p1_x_offset += draw_card(p1_x_offset)
                    check_Score()
                else: # if player is not playing a round
                    noChips.play()
                    print("Please place your bets")


            if stick_button.draw():
                if setting_bet > 0 and newgame:
                    currentPlayer = 2
                else:
                    noChips.play()
                    print("Please place your bets")


            if dubButton.draw():
                if newgame:
                    setting_bet = setting_bet * 2
                    displayScreen.blit(stats_Surface, stats_Rect)
                    drawCard.play()
                    p1_x_offset += draw_card(p1_x_offset)
                    displayScreen.blit(bannerPic, banner_Rect)
                    check_Score()
                    set_Bets.draw()
                    pygame.display.update()
                    currentPlayer = 2
                else: noChips.play()


            if playButton.draw():
                if newgame == False and setting_bet > 0:  #checks if player is not currently playing a round and has placed a bet
                    newgame = True
                else:
                    print("in play")
                    noChips.play()

            if placed_Bets and newgame == False: #checks if player is currently in game and if not then they can place bets
                if chip_1_button.draw():
                    chip_Calculator(1, player_Chips)
                    placeBet.play()
                if chip_5_button.draw():
                    chip_Calculator(5, player_Chips)
                    placeBet.play()
                if chip_10_button.draw():
                    chip_Calculator(10, player_Chips)
                    placeBet.play()
                if chip_25_button.draw():
                    chip_Calculator(25, player_Chips)
                    placeBet.play()
                if chip_50_button.draw():
                    chip_Calculator(50, player_Chips)
                    placeBet.play()


                if atmButton.draw(): #Disables during a round
                    currentstate = "ATM"

                if GmenuButton.draw(): #Disables during a round
                    currentstate = "Menu"

                if QuitButtons.draw(): #Disables during a round
                    pygame.quit()
                    sys.exit()


            if newgame: #checks if new game = true
                while new < 2: # repeats block of code until new is equal to 2
                    p1_x_offset += draw_card(p1_x_offset)  #draws a player card
                    restackCheck()
                    currentPlayer = 2
                    p2_x_offset += draw_card(p2_x_offset) #draws the dealer a card
                    restackCheck()
                    currentPlayer = 1
                    new += 1
                    restackCheck()

                if p2_cardScore >= 16 and p2_cardScore <= 21:  #checks if dealers card score is between 16 and 21 at the start of game
                    aiStick = True

            if currentPlayer == 2 and aiBust == False:
                drawCard.play()
                p2_x_offset += draw_card(p2_x_offset)
                pygame.time.wait(550)
                check_Score()

    pygame.display.update()
