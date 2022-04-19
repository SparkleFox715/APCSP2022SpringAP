#creating wordle
from operator import contains
import random
import pygame
import sys
#init pygame 
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
    global keywordadw
    if(bool):
        stat = "You Won!"
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
            
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([500, 500])
running = True
tries = 8
wordslist = ["guess", "words", "hello", "motel", "india", "china", "grass", "links", "cigar", "rebut", "sissy","humph", "awake", "blush", "focal", "evade", "naval","serve",
            "heath", "dwarf", "model", "karma","stink","grade","quiet","bench","abate","feign","major","death","fresh","crust","stool","color","abase"
            ,"marry","react","batty","pride","floss","helix","croak","staff","paper","unfed","whelp","trawl","outdo","adobe","crazy","sower","repay"
            ,"digit","crate","cluck","spike","mimic","pound","maxim","linen","unmet","flesh","booby","forth","first","stand","belly","ivory","seedy","print","yearn","drain","bribe","stout"
            ,"panel","flume","offal","agree","error","swirl","argue","bleed","delta","flick","totem","wooer","front","shrub","parry","biome","lapel","start","greet","goner","golem","lusty","loopy","round","audit"]
keyword = wordslist[random.randint(0, len(wordslist)-1)]
guess = ""
wordsToPrint = []
wordsToPrintRect = []
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(200, 70, 140, 32)
color = pygame.Color((50,50,50))
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render('Enter a 5 Letter Word', True, pygame.Color((255,255,255)),pygame.Color((0,0,0)))
textRect = text.get_rect()
textRect.center = (500 // 2, 20)

active = False
screen.fill((0, 0, 0))
pygame.display.set_caption('Wordle')
stat = ""
while running:
    status= font.render(stat, True, pygame.Color((255,255,255)),pygame.Color((0,0,0)))
    statusRect = status.get_rect()
    statusRect.center = (500//2, 50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]  
            elif event.key == pygame.K_RETURN:
                guess = user_text
                user_text = ""
                word_submitted(wordChecker(guess.lower(), keyword), guess.lower())
                 
                    
            else:
                user_text += event.unicode
    
    

    screen.fill((0, 0, 0))
  
    
    pygame.draw.rect(screen, color, input_rect)
  
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    screen.blit(text, textRect)
    screen.blit(status, statusRect)
    for i in range(len(wordsToPrintRect)):
        screen.blit(wordsToPrint[i], wordsToPrintRect[i])
    input_rect.w = max(100, text_surface.get_width()+10)
    pygame.display.flip()
    clock.tick(60)


 
