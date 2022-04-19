from operator import contains
import random
import pygame
import sys

def wordChecker(word1, word2):
    if(word1 ==word2):
        return True;
    return False;

def word_submitted(bool, word):
    global stat
    global tries
    global wordsToPrint
    global wordsToPrintRect
    global font
    global keyword
    
    if(bool):
        stat = "You Won!"
        tries-=1
        currentWords = 8-tries
        text = font.render(word, True, pygame.Color((0,255,0)),pygame.Color((0,0,0)))
        textRect = text.get_rect()
        textRect.center = (250, 110+(currentWords*40))
        wordsToPrint.append(text)
        wordsToPrintRect.append(textRect)
    else:
        tries-=1
        if tries<0:
            stat = "You Lost. The word was ".__add__(keyword)
        else:
            currentWords = 8-tries
            for i in range(5):
                character = word[i]
                if character ==keyword[i] :
                    text = font.render(character, True, pygame.Color((0,255,0)),pygame.Color((0,0,0)))
                    textRect = text.get_rect()
                    textRect.center = (225+(i*12), 110+(currentWords*40))
                    wordsToPrint.append(text)
                    wordsToPrintRect.append(textRect)
                elif character in keyword:
                    text = font.render(character, True, pygame.Color((255,255,0)),pygame.Color((0,0,0)))
                    textRect = text.get_rect()
                    textRect.center = (225+(i*12), 110+(currentWords*40))
                    wordsToPrint.append(text)
                    wordsToPrintRect.append(textRect)
                else:
                    text = font.render(character, True, pygame.Color((255,0,0)),pygame.Color((0,0,0)))
                    textRect = text.get_rect()
                    textRect.center = (225+(i*12), 110+(currentWords*40))
                    wordsToPrint.append(text)
                    wordsToPrintRect.append(textRect)
#init pygame            
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([500, 500])
running = True  #true while game is running
tries = 8       #total amount of tries to guess words 
#word bank
wordslist = ["guess", "words", "hello", "motel", "india", "china", "grass", "links", "cigar", "rebut", "sissy","humph", "awake", "blush", "focal", "evade", "naval","serve",
            "heath", "dwarf", "model", "karma","stink","grade","quiet","bench","abate","feign","major","death","fresh","crust","stool","color","abase"
            ,"marry","react","batty","pride","floss","helix","croak","staff","paper","unfed","whelp","trawl","outdo","adobe","crazy","sower","repay"
            ,"digit","crate","cluck","spike","mimic","pound","maxim","linen","unmet","flesh","forth","first","stand","belly","ivory","seedy","print","yearn","drain","bribe","stout"
            ,"panel","flume","offal","agree","error","swirl","argue","bleed","delta","flick","totem","wooer","front","shrub","parry","biome","lapel","start","greet","goner","golem","lusty","loopy","round","audit"]
#chosen words for each game
keyword = wordslist[random.randint(0, len(wordslist)-1)]
guess = ""
#contains list of characters to print of their associated colors
wordsToPrint = []
wordsToPrintRect = []

basefont = pygame.font.Font(None, 32)
usertext = ''
input_rect = pygame.Rect(200, 70, 140, 32)
color = pygame.Color((50,50,50))
#header 
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render('Enter a 5 Letter Word', True, pygame.Color((255,255,255)),pygame.Color((0,0,0)))
textRect = text.get_rect()
textRect.center = (500 // 2, 20)

active = False
screen.fill((0, 0, 0))
#pygame display name
pygame.display.set_caption('Wordle')
stat = ""
while running:
    status= font.render(stat, True, pygame.Color((255,255,255)),pygame.Color((0,0,0)))
    statusRect = status.get_rect()
    statusRect.center = (500//2, 50)
    #keystrokes that are binded to actions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: #exit application
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE: #deleting characters
                usertext = usertext[:-1]  
            elif event.key == pygame.K_RETURN:  #confirming the entered word
                guess = usertext
                usertext = ""
                #checks if the words match and appends to list
                word_submitted(wordChecker(guess.lower(), keyword), guess.lower())
            else:
                usertext += event.unicode
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, input_rect)
    text_surface = basefont.render(usertext, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) #painting user input box
    screen.blit(text, textRect)                                 #painting header box
    screen.blit(status, statusRect)                             #painting status box of whether won or lost
    for i in range(len(wordsToPrintRect)):                      #paints the past words and allows for multicolored words
        screen.blit(wordsToPrint[i], wordsToPrintRect[i])
    input_rect.w = max(100, text_surface.get_width()+10)
    pygame.display.flip()
    clock.tick(60)


 
