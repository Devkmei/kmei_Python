import pygame

pygame.init()
# les variable initial
couleur_fnt_rouge = [255, 0, 0]
FRAMERATE = 30
"""
ouverture de la fenêtre de part
l'outil de pygame pygame.display.set_caption()
"""
taille_ecran = (800,600)# dimension de la fenetre (x,y)
la_fenêtre = pygame.display.set_mode(taille_ecran) #taile de la fenêtre
pygame.display.set_caption("Puissance 4") #le nom de la fenêtre
la_fenêtre.fill(couleur_fnt_rouge) #l'extension de fill de la fenêtre avec la couleur indiqué entre crochet
pygame.display.flip() #pour executer la couleur de la fenêtre

"""
mettre l'icon de part la fonction pygame.display.set_icon()
"""
icon = pygame.image.load("pygame_image/icon_image.png")# récupération d'une image 
pygame.display.set_icon(icon)# convertir l'image en taille d'icon
jeu_en_cours = True # la fenetre continura de tourner 
horloge_framerate = pygame.time.Clock()
"""
la boucle pour maintenir la fenêtre
avant de cliquer sur la coit de fermeture
"""
while jeu_en_cours :# pour que continue de tourner tant qu'on n'a pas appuyé sur la touche de fermeture 
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jeu_en_cours = False
    horloge_framerate.tick(FRAMERATE)

pygame.quit()
