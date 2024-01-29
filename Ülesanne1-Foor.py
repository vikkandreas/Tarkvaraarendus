import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Ülesanne1/foor - Andreas Soitu")
screen.fill([0, 0, 0])

#joonistamine
pygame.draw.rect(screen, [128, 128, 128], [100, 15, 100, 270], 2)
pygame.draw.circle(screen, [255, 0, 0], [150, 65], 40, 0)
pygame.draw.circle(screen, [255, 255, 0], [150, 150], 40, 0)
pygame.draw.circle(screen, [0, 255, 0], [150, 235], 40, 0)

pygame.display.flip()
# Mängu tsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Kontrollib, kas kasutaja on sulgemisnuppu klõpsanud
            running = False  # Lõpetab mängu tsükli ja sulgeb akna
    
    # Siia võid lisada muud mänguloogikat
    
    pygame.display.update()

pygame.quit()  # Lõpetab pygame'i kasutamise pärast mängu tsükli lõppu
