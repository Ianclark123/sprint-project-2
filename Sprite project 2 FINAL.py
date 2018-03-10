import sprite_public
import random
import pygame
pygame.init()
window = pygame.display.set_mode([1018, 573])
button_1 = sprite_public.Sprite("YesButton.jpg",110,49,window)
button_2 = sprite_public.Sprite("NoButton.jpg",110,49,window)
ball = sprite_public.Sprite("TennisBall.jpg", 110, 49,window)

x = random.randint(0, 1018)
y = random.randint(0, 573)
window.fill((255, 0, 0))
drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_1.draw() or button_2.draw()
            print("drawing the button")
        if event.type == pygame.MOUSEBUTTONUP:
            ball.draw()
            print("drawing the ball!")
    pygame.display.flip()
