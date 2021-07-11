from pygame import *

init()
info = display.Info()
window = display.set_mode((info.current_w, info.current_h), RESIZABLE)
class Unit():
    def __init__(self, file, x, y, w, h, speed_x, speed_y):
        self.file = image.load(file)
        self.file = transform.scale(self.file, (int(w), int(h)))
        self.rect = self.file.get_rect(centerx = x, centery = y)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def draw(self):
        window.blit(self.file, self.rect)

cross = Unit("Cross Quit.png", info.current_w//1.1, info.current_h//10, info.current_w/10, info.current_h/10, 0, 0)

fps = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if cross.rect.collidepoint(mouse.get_pos()):
                game = False
    window.fill((100, 100, 255))
    cross.draw()
    display.update()
    fps.tick(60)