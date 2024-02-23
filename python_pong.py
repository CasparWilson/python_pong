import pygame

pygame.init()

#INITIALS
WIDTH, HEIGHT= 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python_Pong")
run = True

#colours
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)

#for the ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 1, 1

#paddle dimensions
paddle_width, paddle_height = 20,120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH -(100 - paddle_width/2)

#Main Loop
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    #movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    #OBJECTS
    pygame.draw.circle(wn, ORANGE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, BLUE, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, BLUE, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    
    pygame.display.update()