import pygame, player, cup, dice, scorecard
pygame.init()
window = pygame.display.set_mode((1250,700)) #hier wird das Fenster erstellt
pygame.display.set_caption("Kniffel") #hier wird ein name vergeben für das Fenster
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    #Erstellung farbe Fenster
    window.fill((74, 154, 69)) #Farbe des Fensters festgelegt












    
    pygame.display.update()
pygame.quit()
