import pygame
import random
import math


pygame.init()

#creating game window
screen = pygame.display.set_mode((800, 600))

#TITLE & icon
title = "space shooter"
#icon = pygame.image.load('data/logo.png')
pygame.display.set_caption('space shooter')
#pygame.display.set_icon(icon)


#Background image
bg = pygame.image.load('background1.jpg')

pygame.mixer.music.load('d:\python project 5\data\high-energy.mp3')
pygame.mixer_music.play(-1)

bullet_sound = pygame.mixer.Sound('GUNSHOT.wav')
explosion_sound = pygame.mixer.Sound('a-bomb-.mp3')

#player
player_img = pygame.image.load('player1.png')
playerX = 368
playerY = 516
playerX_moving = 0

#enemy
num_of_enemies = 7


enemy_img = []
enemyX = []
enemyY = []
enemyX_moving = []
enemyY_moving = []


for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('alien. (2).png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(20, 120))
    enemyX_moving.append(0.4)
    enemyY_moving.append(40)
    

#Bullet
bullet_img = pygame.image.load('Bullit (2).png')
bulletX = 0
bulletY = 516
bulletY_moving = -1
bullet_state = 'ready'

score = 0

score_font = pygame.font.Font('batmfa__.ttf', 32)
scoreX = 10
scoreY = 10

game_over_font = pygame.font.Font('batmfa__.ttf', 64)
game_overX = 200
game_overY = 250 



restart_font = pygame.font.Font('Paintingwithchocolate-K5mo.ttf', 28)
restartX = 250
restartY = 400


game_status = 'running'


def show_restart(x, y):
    restart_img = restart_font.render('To restart press R', True,(0, 255, 0))
    screen.blit(restart_img, (x, y))
    


def show_game_over(x, y):
    global game_status
    game_over_img = game_over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(game_over_img, (x, y))
    pygame.mixer.music.stop()
    game_status = 'end'


def show_score(x, y):
    score_img = score_font.render('score: ' + str(score) , True, (255, 255, 255))
    screen.blit(score_img,(x, y))


def iscollistion(x1, y1, x2, y2):
     distance = math.sqrt(math.pow((x2 - x1), 2)  +  math.pow((y2 -y1), 2))
     if distance < 25:
         return  True
     else:
         return  False

def bullet(x, y):
    screen.blit(bullet_img, (x + 15, y + 10 ))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def player(x, y):
    screen.blit(player_img, (x, y))



game_on = True
while game_on:
    #Background
    screen.fill((255, 0, 0))
    screen.blit(bg,(0, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_moving = -0.7
            if event.key == pygame.K_RIGHT:
                playerX_moving = 0.7
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_state = 'fire'
                    bulletX = playerX
                    bullet(bulletX, bulletY)
                    bullet_sound.play()
            if event.key == pygame.K_r:
                if game_status == 'end':
                    game_status = 'running'
                    score = 0
                    playerX = 368
                    pygame.mixer.music.play(-1)
                    for i in range(num_of_enemies):
                        enemyX[i] = random.randint(0, 736)
                        enemyY[i] = random.randint(20, 120)
             

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 playerX_moving = 0



#bullet moving
    if bullet_state == 'fire':
        if bulletY < 10:
            bulletY = 516
            bullet_state = 'ready'
        bulletY += bulletY_moving
        bullet(bulletX, bulletY)
 
    #enemy moving
    for i in range(num_of_enemies):
        # game over
        if enemyY[i] > 466:
            show_game_over(game_overX, game_overY)
            show_restart(restartX, restartY)
            for j in range(num_of_enemies):
                enemyY[j] = 1200

            

        #*********
        enemyX[i] += enemyX_moving[i]
        if enemyX[i] <= 0:
            enemyX[i] = 0
            enemyX_moving[i] = 0.4
            enemyY[i] += enemyY_moving[i]
        elif enemyX[i] >= 736:
            enemyX[i] = 736
            enemyX_moving[i] = -0.4
            enemyY[i] += enemyY_moving[i]

        enemy(enemyX[i], enemyY[i], i)

        # cllision
        collision = iscollistion(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 516
            bullet_state = 'ready'
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(20, 120)
            score += 1 
            explosion_sound.play() 
            print(score)


    show_score(scoreX, scoreY)

    #player moving
    playerX += playerX_moving

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    player(playerX, playerY)


    pygame.display.update ()