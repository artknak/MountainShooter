import pygame

print('Setup start.')
# pygame.init é obrigatório para iniciar o pygame e todas
# as suas dependências!
pygame.init()
# Criando a janela do jogo.
window = pygame.display.set_mode(size=(600, 480))
print('Setup end.')

print('Loop start.')
# A janela precisa de um loop para se manter aberta.
while True:
    # Check for all events.
    # Criando evento para fechar janela!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close window
            quit()        # End pygame
