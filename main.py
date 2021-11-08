import pygame
from pygame import mixer

#Intialize Pygame
pygame.init()

#Create the Screen
screen = pygame.display.set_mode((800,600))

#Change Title & Game Window Icon
pygame.display.set_caption("god vs evil")
icon = pygame.image.load("zeus.png")
pygame.display.set_icon(icon)

#background
background = pygame.image.load("back.png")


#setup font 
font = pygame.font.Font('freesansbold.ttf',32)
game_over_font = pygame.font.Font('freesansbold.ttf',64)

#show score

score_x = 20
score_y = 20

score_value = 0 
def show_score(x,y):
    score = font.render("Score :"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


#show life

life_x = 600
life_y = 20

life_value = 100

def show_life(x,y):
    life = font.render("Life :"+str(life_value),True,(255,255,255))
    screen.blit(life,(x,y))


#aroow
bulletImg = pygame.image.load("arrow.png")
bullet_x = 0
bullet_y = 0
bullet_state = False

def bullet(x,y):
    screen.blit(bulletImg,(x+20,y))
    global bullet_state
    bullet_state = True


#Asteroids

draw_access_1 = True
draw_access_2 = True
draw_access_3 = True
draw_access_4 = True
draw_access_5 = True
astro_x = 50
astro_y = 50
astro_y_1 = 200
astro_y_2 = 400
astro_y_3 = 50
astro_y_4 = 100

astrox1 = 50
astrox2 = 150
astrox3 = 250
astrox4 = 350
astrox5 = 450



asteroidsImg = pygame.image.load("devil.png")
def asto(x,y):
    screen.blit(asteroidsImg,(x,y))

#Player
player_x = 400
player_y = 500
player_move = 0
player_move_up_down = 0

playerImg = pygame.image.load("rama.png")
def player(player_x,player_y):
    screen.blit(playerImg,(player_x,player_y))

#Game Over

game_fail = False

def game_over():
    over = game_over_font.render("Game Over",True,(255,255,255))
    screen.blit(over,(230,300))



# Game Loop
loop_run = True
while loop_run:

    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop_run = False

        #Player Handle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_move = -2
                print("Left")
            if event.key == pygame.K_RIGHT:
                player_move = 2
                print("Right")
            if event.key == pygame.K_UP:
                player_move_up_down = -2
                print("Up")
            if event.key == pygame.K_DOWN:
                player_move_up_down = 2
                print("Down")
            #Bullet Fire
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound("arrowshoot.wav")
                bullet_sound.play()
                bullet_x = player_x
                bullet_y = player_y
                bullet(bullet_x,bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player_move = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_move_up_down = 0

        #mouse events

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_button = pygame.mouse.get_pressed()
            if mouse_button[0]:
                bullet_sound = mixer.Sound("arrowshoot.wav")
                bullet_sound.play()
                bullet_x = player_x
                bullet_y = player_y
                bullet(bullet_x, bullet_y)




 
    #player limitation
    if player_x <= 50:
        player_x = 50
    elif player_x >= 686:
        player_x = 686
    elif player_y <= 50:
        player_y = 50
    elif player_y >= 486:
        player_y = 486


    player_x += player_move
    player_y += player_move_up_down
    player(player_x,player_y)

    #Display Asteroids constantly
    #devil move
    if game_fail == False:
        if draw_access_1:
            astro_y += 0.7
        if draw_access_2:
            astro_y_1 += 0.7
        if draw_access_3:
            astro_y_2 += 0.7
        if draw_access_4:
            astro_y_3 += 0.7
        if draw_access_5:
            astro_y_4 += 0.7


    #devil limitation
    
    if astro_y >= 650:
        
        astro_y = 0
    if astro_y_1 >= 650:
        astro_y_1 = 0
    if astro_y_2 >= 650:
        astro_y_2 = 0
    if astro_y_3 >= 650:
        astro_y_3 = 0
    if astro_y_4 >= 650:
        astro_y_4 = 0

    #good life
    if game_fail == False:
        if astro_y >= 550 and astro_y <= 551:
            life_value -=5
        if astro_y_1 >= 550 and astro_y_1 <= 551:
            life_value -= 5
        if astro_y_2 >=550 and astro_y_2 <= 551:
            life_value -= 5
        if astro_y_3 >=550 and astro_y_3 <= 551:
            life_value -= 5
        if astro_y_4 >=550 and astro_y_4 <= 551:
            life_value -= 5

    #devil draw
    if game_fail == False:
        if draw_access_1:
            asto(astrox1,astro_y)
        if draw_access_2:
            asto(astrox2, astro_y_1)
        if draw_access_3:
            asto(astrox3, astro_y_2)
        if draw_access_4:
            asto(astrox4, astro_y_3)
        if draw_access_5:
            asto(astrox5, astro_y_4)

    #arrow move
    if bullet_state == True:
        bullet_y -= 10
        bullet(bullet_x,bullet_y)
    
    

    #Get Range Astroid x Position
    astro_x_1 = range(astrox1,astrox1+40)
    astro_x_2 = range(astrox2,astrox2+40)
    astro_x_3 = range(astrox3,astrox3+40)
    astro_x_4 = range(astrox4,astrox4+40)
    astro_x_5 = range(astrox5,astrox5+40)

    if bullet_x in astro_x_1:
        if bullet_y <= astro_y+64:
            astrox1 = -64
            draw_access_1 = False
            score_value += 20

    if bullet_x in astro_x_2:
        if bullet_y <= astro_y_1+64:
            astrox2 = -64
            draw_access_2 = False
            score_value += 20

    if bullet_x in astro_x_3:
        if bullet_y <= astro_y_2+64:
            astrox3 = -64
            draw_access_3 = False
            score_value += 20

    if bullet_x in astro_x_4:
        if bullet_y <= astro_y_3+64:
            astrox4 = -64
            draw_access_4 = False
            score_value += 20

    if bullet_x in astro_x_5:
        if bullet_y <= astro_y_4+64:
            astrox5 = -64
            draw_access_5 = False
            score_value += 20

    show_score(score_x,score_y)
    show_life(life_x,life_y)

    if life_value <= 0 :
        life_value = 0
        game_fail = True
        game_over() 

  
    #Display Update
    pygame.display.update()
