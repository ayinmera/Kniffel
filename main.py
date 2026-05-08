import pygame, player, cup, dice, scorecard, random
pygame.init()
window = pygame.display.set_mode((1250,700)) #hier wird das Fenster erstellt
pygame.display.set_caption("Kniffel") #hier wird ein name vergeben für das Fenster

#scorecarde anzeigen
scoresheet = scorecard.Scorecard()

#Würfel

dice_list = [] 
for i in range(5):
    würfel = dice.Dice(
        color = "white",
        value = i+1,
        position = (700 + i*70, 100),
        size =(50,50)
    )
    dice_list.append(würfel)
#allgemein
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            for würfel in dice_list:
                würfel.value = random.randint(1,6) #random zahl von 1 bis 6 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)

    #Erstellung farbe Fenster
    window.fill((74, 154, 69)) #Farbe des Fensters festgelegt

    #Mausklick für Würfelwechsel

    #scorecarde anzeigen
    scorecard.draw(window)
  

    for w in dice_list:
        w.draw(window) #test ob die Werte der Würfel geändert werden
    
    pygame.display.update()
pygame.quit()
