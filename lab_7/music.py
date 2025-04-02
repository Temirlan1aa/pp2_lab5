import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("lab7/music/a.mp3")

screen = pygame.display.set_mode((300, 400))  
pygame.display.set_caption("Music Player")

running = True
pause = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  

            if event.key == pygame.K_SPACE:
                pygame.mixer.music.play(-1)  

            elif event.key == pygame.K_p:
                if pause:
                    pause = False
                else:
                    pause = True 

                if pause:
                    pygame.mixer.music.pause()
                else:
                   pygame.mixer.music.unpause() 
                


    screen.fill((0, 0, 0)) 
    pygame.display.update()