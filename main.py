import pygame, player, cup, dice, scorecard, random
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
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            for würfel in dice_list:
                würfel.value = random.randint(1, 6)
    #Erstellung farbe Fenster
    window.fill((74, 154, 69)) #Farbe des Fensters festgelegt

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos)










    
    pygame.display.update()
pygame.quit()
