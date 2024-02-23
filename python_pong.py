import pygame

pygame.init()

#INITIALS
WIDTH, HEIGHT= 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python_Pong")
run = True

#colours
ORANGE = (255, 165, 0)

#for the ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius

#Main Loop
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    pygame.draw.circle(wn, ORANGE, (ball_x, ball_y), radius)