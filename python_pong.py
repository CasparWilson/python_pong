import pygame

pygame.init()

#INITIALS
WIDTH, HEIGHT= 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python_Pong")
run = True
player_1 = player_2 = 0

#colours
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0,)

#for the ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.2, 0.2

#paddle dimensions
paddle_width, paddle_height = 20,120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH -(100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0

#Main Loop
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.5
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.5
            if i.key == pygame.K_w:
                left_paddle_vel = -0.5
            if i.key == pygame.K_s:
                left_paddle_vel = 0.5
        if i.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0



    #ball's movement boundary
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        ball_vel_x, ball_vel_y = -0.2, -0.2
        player_1 += 1
    if ball_x <= 0 + radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        ball_vel_x, ball_vel_y = 0.2, 0.2
        player_2 += 1

    #movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel

    #paddle boundaries
    if right_paddle_y > HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y < 0:
        right_paddle_y = 0
    if left_paddle_y > HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y < 0:
        left_paddle_y = 0

    #collision
    if (right_paddle_x <= ball_x + radius <= right_paddle_x + paddle_width and right_paddle_y <= ball_y <= right_paddle_y + paddle_height):
        ball_vel_x *= -1.2
    if (left_paddle_x + paddle_width >= ball_x - radius > left_paddle_x and left_paddle_y <= ball_y <= left_paddle_y + paddle_height):
        ball_vel_x *= -1.2

    #scoreboard
        font = pygame.font.SysFont('callibri', 32)
        score_1 = font.render("Player_1:" + str(player_1), True, ORANGE)
        wn.blit(score_1, (25, 25))
        score_2 = font.render("Player_2:" + str(player_2), True, ORANGE)
        wn.blit(score_2, (825, 25))

    #OBJECTS
    pygame.draw.circle(wn, ORANGE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, BLUE, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, BLUE, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    
    pygame.display.update()