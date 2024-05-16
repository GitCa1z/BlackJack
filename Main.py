import pygame, sys
import os
import random

pygame.init()

screenheight = 720
screenwidth = 1280
displayscreen = pygame.display.set_mode((screenwidth, screenheight))

Background_ATM = pygame.image.load('Backgrounds/Background - ATM.png').convert()
Background_ATMT = pygame.image.load('Tutorial/Background - ATM.png').convert()

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
banner_deal_Rect = banner_deal.get_rect(center = (640,45))
banner_Rect = bannerPic.get_rect(center = (640,473))
stats_Rect = stats_Surface.get_rect(center = (135, 249))

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

ChippyNormal = pygame.image.load('ChippyEmotes/Normal.png').convert_alpha()
ChippyConfused = pygame.image.load('ChippyEmotes/Confused.png').convert_alpha()
ChippyAngry = pygame.image.load('ChippyEmotes/Angry.png').convert_alpha()
ChippyHappy = pygame.image.load('ChippyEmotes/Happy.png').convert_alpha()
ChippyATM = pygame.image.load('ChippyEmotes/ATM.png').convert_alpha()
ChippyChip = pygame.image.load('ChippyEmotes/Chips.png').convert_alpha()

ChippyNormalR = ChippyNormal.get_rect(center = (1145,140))

dealerTalks = pygame.mixer.Sound('Sounds/Text_Fast.wav')
openingATM = pygame.mixer.Sound("Sounds/OpenAtm.wav")
closeATM = pygame.mixer.Sound("Sounds/CloseAtm.wav")
coinssfx = pygame.mixer.Sound("Sounds/Coin+.wav")
noChips = pygame.mixer.Sound('Sounds/No-coins.wav')
backsong = pygame.mixer.Sound('Sounds/Pixel Perfect.wav')
hoversfx = pygame.mixer.Sound('Sounds/Hover.wav')
backsong2 = pygame.mixer.Sound('Sounds/Pix-Astral_bunny.WAV')
backsong3 = pygame.mixer.Sound('Sounds/Jorge Hernandez - Chopsticks.mp3')
backsong4 = pygame.mixer.Sound('Sounds/Skeletoni.mp3')
drawCard = pygame.mixer.Sound('Sounds/Draw.wav')

z = 0
currentSong = 0



playlist_Duration = {}
backsong.set_volume(0.1)
coinssfx.set_volume(0.5)
noChips.set_volume(1)
closeATM.set_volume((0.7))


background_music = {backsong, backsong2, backsong3,backsong4}

for x in background_music:
    playlist_Duration[z] = x.get_length()
    z+=1

Test = pygame.USEREVENT + 1

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
    def draw(self):
        pos = pygame.mouse.get_pos()
        action = False
        if self.rect.collidepoint(pos):
            self.image = self.highlight
            if self.playonce == 0:
                hoversfx.play()
                self.playonce = 1
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        elif self.rect.collidepoint != True:
            self.image = self.high
            self.playonce = 0

        displayscreen.blit(self.image,(self.rect.x,self.rect.y))

        return action

class textSurface:
    def __init__(self,variable,antialias,colour,x,y, size = 30):
        score = pygame.font.Font('04B_19__.TTF', size)
        self.variable = score.render(str(variable), antialias,colour)
        self.rect = self.variable.get_rect()
        self.rect.center = (x,y)
        self.size = size
    def draw(self):
        displayscreen.blit(self.variable,(self.rect.x,self.rect.y))

class SpeechBubble:
    def __init__(self,text,x,y,text_size = 20):
            self.x = x
            self.y = y
            self.text_size = text_size
            font = pygame.font.Font('pixelmix.ttf', text_size)
            self.render = font.render(text, 1, 'Black')
            self.text_rect = self.render.get_rect(midright=(self.x, self.y))
            self.inflate = self.text_rect.inflate(10, 10)
            self.outline = self.render.get_rect(midright=(self.x, self.y))
            self.outlineinflate = self.outline.inflate(15, 15)

    def drawBubble(self):
        pygame.draw.rect(displayscreen, (0, 0, 0), self.outlineinflate)
        pygame.draw.rect(displayscreen, (255, 255, 255), self.inflate)
        displayscreen.blit(self.render, self.text_rect)


def aiupdatespeech(milliseconds):
    pygame.display.update()
    dealerTalks.play()
    pygame.time.wait(milliseconds)

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

Test_button = button(150,550,buttonHit,hit_hover,buttonHit)

chip_color = 'White'
chip_Bank = 250
players_chips = 0
setting_bet = 0
introduciton = True
inGame = True
placed_Bets = True
endgame = False
bust = False
aiStick = False
aiBust = False
runonce = True
p1_x_offset = 0
p2_x_offset = 0
new = 0
newgame = False
currentPlayer = 1
currentstate = 'Menu'
p1_cardScore = 0
p2_cardScore = 0
card_images = {}
suits = ['c', 'd', 'h', 's']
ranks = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']

set_Bets = textSurface(setting_bet, True, 'White', 140, 375)

for suit in suits:
    for rank in ranks:
        image_path = os.path.join("cards", f"{suit}{rank}.png")
        original_image = pygame.image.load(image_path)
        scaled_image = pygame.transform.scale(original_image, (112, 150))
        card_images[(rank, suit)] = scaled_image


card_key, card_value = random.choice(list(card_images.items()))

def restackCheck():
    if len(card_images) == 0:
        for suit in suits:
            for rank in ranks:
                image_path = os.path.join("cards", f"{suit}{rank}.png")
                original_image = pygame.image.load(image_path)
                scaled_image = pygame.transform.scale(original_image, (112, 150))
                card_images[(rank, suit)] = scaled_image

def Introduction():

    if currentstate == "Game":
        pygame.time.set_timer(Test, int(playlist_Duration.get(currentSong)) * 1000, False)
        backsong.play()
        displayscreen.blit(background_Tutorial_1,(0,0))
        displayscreen.blit(ChippyNormal,ChippyNormalR)
        AiSpeech1.drawBubble()
        aiupdatespeech(3000)
        displayscreen.blit(background_Tutorial_1,(0,0))
        displayscreen.blit(ChippyHappy,ChippyNormalR)
        AiSpeech2.drawBubble()
        aiupdatespeech(3000)
        displayscreen.blit(background_Tutorial_1,(0,0))
        displayscreen.blit(ChippyNormal,ChippyNormalR)
        AiSpeech3.drawBubble()
        aiupdatespeech(3000)
        displayscreen.blit(background_Tutorial_1,(0,0))
        displayscreen.blit(ChippyConfused,ChippyNormalR)
        AiSpeech4.drawBubble()
        aiupdatespeech(3000)
        displayscreen.blit(background_Tutorial_1,(0,0))
        displayscreen.blit(ChippyHappy,ChippyNormalR)
        AiSpeech5.drawBubble()
        aiupdatespeech(3000)
        displayscreen.blit(background_Tutorial_1,(0,0))
        displayscreen.blit(ChippyChip,ChippyNormalR)
        AiSpeech6.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(background_Tutorial_2,(0,0))
        displayscreen.blit(ChippyNormal,ChippyNormalR)
        AiSpeech7.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(background_Tutorial_2,(0,0))
        displayscreen.blit(ChippyNormal,ChippyNormalR)
        AiSpeech8.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(background_Tutorial_3, (0, 0))
        displayscreen.blit(ChippyNormal,ChippyNormalR)
        AiSpeech9.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(background_Tutorial_1, (0, 0))
        displayscreen.blit(ChippyNormal,ChippyNormalR)
        AiSpeech10.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(background_Tutorial_1, (0, 0))
        displayscreen.blit(ChippyNormal,ChippyNormalR)
        AiSpeech11.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(background_Tutorial_4, (0, 0))
        displayscreen.blit(ChippyNormal,ChippyNormalR)
        AiSpeech12.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(background_Tutorial_5, (0, 0))
        displayscreen.blit(ChippyNormal,ChippyNormalR)
        AiSpeech13.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(background_Tutorial_6, (0, 0))
        displayscreen.blit(ChippyNormal,ChippyNormalR)
        AiSpeech14.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(background_Tutorial_7, (0, 0))
        displayscreen.blit(ChippyNormal,ChippyNormalR)
        AiSpeech15.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(background_Tutorial_1, (0, 0))
        displayscreen.blit(ChippyNormal,ChippyNormalR)
        AiSpeech16.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(background_Tutorial_8, (0, 0))
        displayscreen.blit(ChippyATM,ChippyNormalR)
        AiSpeech17.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(background_Tutorial_1, (0, 0))
        displayscreen.blit(ChippyATM,ChippyNormalR)


    if currentstate == 'ATM':
        global introduciton

        displayscreen.blit(Background_ATMT,(0,0))
        AiSpeech1ATM.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(Background_ATMT, (0, 0))
        AiSpeech2ATM.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(Background_ATMT, (0, 0))
        AiSpeech3ATM.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(Background_ATMT, (0, 0))
        AiSpeech4ATM.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(Background_ATMT, (0, 0))
        AiSpeech5ATM.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(Background_ATMT, (0, 0))
        AiSpeech6ATM.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(Background_ATMT, (0, 0))
        AiSpeech7ATM.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(Background_ATMT, (0, 0))
        AiSpeech8ATM.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(Background_ATMT, (0, 0))
        AiSpeech9ATM.drawBubble()
        aiupdatespeech(4000)
        displayscreen.blit(Background_ATM, (0, 0))

        introduciton = False
def textRender():
    playersScoreText = textSurface(p1_cardScore, True, 'White', 645, 480)
    dealerScoreText = textSurface(p2_cardScore,True,"White",645,41)
    players_Bank = textSurface(chip_Bank,True,'White',140,155)
    set_Bets = textSurface(setting_bet,True,'White',140,375)
    player_chip_amount = textSurface(players_chips,True,'White', 820,200)

    if currentstate == 'Game':
        playersScoreText.draw()
        dealerScoreText.draw()
        players_Bank.draw()
        set_Bets.draw()
    elif currentstate == 'ATM':
        players_Bank.rect.x = 440
        players_Bank.rect.y = 190
        players_Bank.size = 500
        players_Bank.draw()
        player_chip_amount.draw()
def check_Score():
    global aiStick
    global aiBust
    global currentPlayer
    global endgame
    global bust


    if currentPlayer == 1 and p1_cardScore > 21:
        bust = True
        currentPlayer = 2
        pygame.display.update()
    if currentPlayer == 2:
        if p2_cardScore >= 16 and p2_cardScore <= 21:
            aiStick = True
            endgame = True
        elif p2_cardScore > 21:
            aiBust = True
            endgame = True
    if endgame:
        winCondition(p1_cardScore, p2_cardScore)
def winCondition(p1_cardscore, p2_cardscore):
    global p1_cardScore
    global p2_cardScore
    global players_chips
    global setting_bet
    dealerScoreText = textSurface(p2_cardScore, True, "White", 645, 41)
    playersScoreText = textSurface(p1_cardScore, True, 'White', 645, 480)

    if p1_cardscore > p2_cardscore and bust == False:
        print("Win")
        displayscreen.blit(banner_deal,banner_deal_Rect)
        displayscreen.blit(bannerPic,banner_Rect)
        dealerScoreText.draw()
        playersScoreText.draw()
        displayscreen.blit(ChippyHappy,ChippyNormalR)
        Aiwin.drawBubble()
        dealerTalks.play()
        players_chips += setting_bet * 2
        pygame.display.update()
        pygame.time.delay(3000)
        newGame()

    elif p1_cardscore < p2_cardscore and aiBust:
        print("Win")
        displayscreen.blit(banner_deal, banner_deal_Rect)
        displayscreen.blit(bannerPic,banner_Rect)
        dealerScoreText.draw()
        playersScoreText.draw()
        displayscreen.blit(ChippyHappy, ChippyNormalR)
        Aiwin.drawBubble()
        dealerTalks.play()
        players_chips += setting_bet * 2
        pygame.display.update()
        pygame.time.delay(3000)

        newGame()

    elif p1_cardscore < p2_cardscore and aiBust == False and bust == False:
        print("Lost")
        displayscreen.blit(banner_deal, banner_deal_Rect)
        displayscreen.blit(bannerPic,banner_Rect)
        dealerScoreText.draw()
        playersScoreText.draw()
        displayscreen.blit(ChippyAngry, ChippyNormalR)
        Ailost.drawBubble()
        dealerTalks.play()

        pygame.display.update()
        pygame.time.delay(3000)
        newGame()

    elif p1_cardscore > p2_cardscore and bust and aiBust == False:
        print("Lost")
        displayscreen.blit(banner_deal, banner_deal_Rect)
        displayscreen.blit(bannerPic,banner_Rect)
        dealerScoreText.draw()
        playersScoreText.draw()
        displayscreen.blit(ChippyAngry, ChippyNormalR)
        Ailost.drawBubble()
        dealerTalks.play()
        pygame.display.update()
        pygame.time.delay(3000)
        newGame()

    elif p1_cardscore == p2_cardscore and bust == False and aiBust == False:
        print("Draw")
        displayscreen.blit(banner_deal, banner_deal_Rect)
        displayscreen.blit(bannerPic,banner_Rect)
        dealerScoreText.draw()
        playersScoreText.draw()
        displayscreen.blit(ChippyConfused, ChippyNormalR)
        Aidraw.drawBubble()
        dealerTalks.play()
        players_chips += setting_bet
        pygame.display.update()
        pygame.time.delay(3000)
        newGame()

    elif p1_cardscore > 21 and p2_cardscore > 21 and bust and aiBust:
        print("Draw")
        displayscreen.blit(banner_deal, banner_deal_Rect)
        displayscreen.blit(bannerPic,banner_Rect)
        dealerScoreText.draw()
        playersScoreText.draw()
        displayscreen.blit(ChippyConfused, ChippyNormalR)
        Aidraw.drawBubble()
        dealerTalks.play()
        players_chips += setting_bet
        pygame.display.update()
        pygame.time.delay(3000)
        newGame()
def chip_Calculator(chip_input,player_Chips):
    global players_chips
    global setting_bet
    match chip_input:
        case 1:
            if players_chips <= 0:
                print('you dont have enough!')
                noChips.play()

            elif players_chips >= 1:

                players_chips -= 1
                setting_bet += 1
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
    os.system('cls')
    global p1_cardScore
    global p2_cardScore
    global setting_bet
    global new
    global currentPlayer
    global newgame
    global endgame
    global aiStick
    global aiBust
    global p1_x_offset
    global p2_x_offset
    global bust

    restackCheck()
    endgame = False
    displayscreen.blit(Background_Menu, (0, 0))
    displayscreen.blit(ChippyNormal,ChippyNormalR)
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

def card_Score(cardscore):
    global p1_cardScore
    global p2_cardScore

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
def draw_card(x_offset):
    card_key = random.choice(list(card_images.keys()))
    space_between_cards = 50
    p1_initial_x = 400
    p1_initial_y = 270
    p2_initial_x = 400
    p2_initial_y = 90

    if currentPlayer == 1:
        displayscreen.blit(card_images[card_key], (p1_initial_x + x_offset, p1_initial_y))
        x_offset = space_between_cards
        card_Score(card_key)
        card_images.pop(card_key)
        print(len(card_images))

    elif currentPlayer == 2 and aiStick == False and aiBust == False:
        displayscreen.blit(card_images[card_key], (p2_initial_x + x_offset, p2_initial_y))
        x_offset = space_between_cards
        pygame.display.update()
        card_Score(card_key)
        card_images.pop(card_key)
        print(len(card_images))
    return x_offset

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == Test:
            if currentSong == 0:
                backsong2.play()
                currentSong += 1
                print(currentSong)
                print("first song start")
            elif currentSong == 1:
                print(currentSong)
                backsong3.play()
                currentSong += 1
                print("second song finished")
            elif currentSong == 2:
                backsong4.play()
                currentSong += 1
                print("Third song finished")
            elif currentSong == 3:
                backsong.play()
                currentSong = 0
                print("Third song finished")

    if currentstate == 'ATM':
        if introduciton:
            Introduction()

        displayscreen.blit(Background_ATM, (0, 0))

        textRender()

        if at1b.draw():
            if chip_Bank > 0:
                coinssfx.play()
                chip_Bank -= 1
                players_chips += 1
            else:
                noChips.play()
                print("bank don't have enough")

        if at1mb.draw():
            if players_chips > 0:
                coinssfx.play()
                chip_Bank += 1
                players_chips -= 1
            else:
                noChips.play()
                print("you cant deposit anymore")

        if at5b.draw():
            if chip_Bank >= 5:
                coinssfx.play()
                chip_Bank -= 5
                players_chips += 5
            else:
                noChips.play()
                print("bank don't have enough")

        if at5mb.draw():
            if players_chips >= 5:
                coinssfx.play()
                chip_Bank += 5
                players_chips -= 5
            else:
                noChips.play()
                print("you need more deposit!")

        if at10b.draw():
            if chip_Bank >= 10:
                coinssfx.play()
                chip_Bank -= 10
                players_chips += 10
            else:
                noChips.play()
                print("bank don't have enough")

        if at10mb.draw():
            if players_chips >= 10:
                coinssfx.play()
                chip_Bank += 10
                players_chips -= 10
            else:
                noChips.play()
                print("you need more to deposit")

        if at25b.draw():
            if chip_Bank >= 25:
                coinssfx.play()
                chip_Bank -= 25
                players_chips += 25
            else:
                noChips.play()
                print("bank don't have enough")

        if at25mb.draw():
            if players_chips >= 25:
                coinssfx.play()
                chip_Bank += 25
                players_chips -= 25
            else:
                noChips.play()
                print("you need more deposit")

        if at50b.draw():
            if chip_Bank >= 50:
                coinssfx.play()
                chip_Bank -= 50
                players_chips += 50
            else:
                noChips.play()
                print("you do not have enough")

        if at50mb.draw():
            if players_chips >= 50:
                coinssfx.play()
                chip_Bank += 50
                players_chips -= 50
            else:
                noChips.play()
                print("you need more deposit")

        if depositButton.draw():
            chip_Bank += players_chips
            players_chips = 0

        if WithdrawButton.draw():
            players_chips += chip_Bank
            chip_Bank = 0

        if menuButton.draw():
            currentstate = "Menu"

        if gameButton.draw():
            currentstate = 'Game'
            closeATM.play()
            displayscreen.blit(Background_Menu, (0, 0))
            displayscreen.blit(ChippyNormal,ChippyNormalR)
            pygame.display.update()



    if currentstate == 'Menu':

        displayscreen.blit(background_Menu, (0, 0))
        if menuButton.draw():
            currentstate = "Game"
            displayscreen.blit(background_Tutorial_1,(0,0))
            displayscreen.blit(ChippyNormal,ChippyNormalR)
            if introduciton:
                Introduction()

    if currentstate == 'Game':

        pygame.display.update()

        if inGame:
            displayscreen.blit(stats_Surface, stats_Rect)
            displayscreen.blit(bannerPic, banner_Rect)
            displayscreen.blit(banner_deal, banner_deal_Rect)

            textRender()

            player_Chips = textSurface(players_chips, True, chip_color, 140, 268)
            player_Chips.draw()

            if players_chips <= 0:
                chip_color = 'Red'

            else:
                chip_color = 'White'

            if hit_button.draw():
                if setting_bet > 0 and newgame:
                    drawCard.play()
                    p1_x_offset += draw_card(p1_x_offset)
                    check_Score()
                else:
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
                    drawCard.play()
                    p1_x_offset += draw_card(p1_x_offset)
                    displayscreen.blit(bannerPic,banner_Rect)
                    check_Score()
                    set_Bets.draw()
                    pygame.display.update()
                    currentPlayer = 2
                else: noChips.play()


            if playButton.draw():
                if newgame == False and setting_bet > 0:
                    newgame = True
                else:
                    print("in play")
                    noChips.play()

            if placed_Bets and newgame == False:
                if chip_1_button.draw():
                    chip_Calculator(1, player_Chips)
                if chip_5_button.draw():
                    chip_Calculator(5, player_Chips)
                if chip_10_button.draw():
                    chip_Calculator(10, player_Chips)
                if chip_25_button.draw():
                    chip_Calculator(25, player_Chips)
                if chip_50_button.draw():
                    chip_Calculator(50, player_Chips)

                if atmButton.draw():
                    currentstate = "ATM"

                if GmenuButton.draw():
                    currentstate = "Menu"

                if QuitButtons.draw():
                    pygame.quit()
                    sys.exit()

            # ======================================================================================================================

            if newgame:
                while new < 2:
                    p1_x_offset += draw_card(p1_x_offset)
                    restackCheck()
                    currentPlayer = 2
                    p2_x_offset += draw_card(p2_x_offset)
                    restackCheck()
                    currentPlayer = 1
                    new += 1
                    restackCheck()

                if p2_cardScore >= 16 and p2_cardScore <= 21:
                    aiStick = True

            if currentPlayer == 2 and aiBust == False:
                drawCard.play()
                p2_x_offset += draw_card(p2_x_offset)
                pygame.time.wait(550)
                check_Score()

    pygame.display.update()
