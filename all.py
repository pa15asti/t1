import pygame

pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Прямоугольники с Ctrl+Z')

screen2 = pygame.Surface(screen.get_size())
x1, y1, w, h = 0, 0, 0, 0
running = True
llist = []
drawing = False  # режим рисования выключен
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print(llist)
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True  # включаем режим рисования
            # запоминаем координаты одного угла
            x1, y1 = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            # сохраняем нарисованное (на втором холсте)
            screen2.blit(screen, (0, 0))
            drawing = False
            llist.append(((x1, y1), (w, h)))
            x1, y1, w, h = 0, 0, 0, 0
        if event.type == pygame.MOUSEMOTION:
            # запоминаем текущие размеры
            if drawing:
                w, h = event.pos[0] - x1, event.pos[1] - y1
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z] and keys[pygame.K_LCTRL]:
                try:
                    llist.remove(llist[-1])
                    screen.fill(pygame.Color('black'))
                    screen2.fill('black')
                    for i in llist:
                        pygame.draw.rect(screen2, (0, 0, 255), i, 1)
                except:
                    print("Холст пуст")
    # рисуем на экране сохранённое на втором холсте
    screen.fill(pygame.Color('black'))
    screen.blit(screen2, (0, 0))
    if drawing:  # и, если надо, текущий прямоугольник
        if w > 0 and h > 0:
            pygame.draw.rect(screen, (0, 0, 255), ((x1, y1), (w, h)), 1)
    pygame.display.flip()
