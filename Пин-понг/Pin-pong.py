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

class Player(Unit):
    def move(self):
        key_list = key.get_pressed()
        self.hitbox.centerx = self.rect.centerx
        self.hitbox.centery = self.rect.centery
        if key_list[K_UP]:
            if self.rect.top > 0:
                self.rect.y -= self.speed_y
        if key_list[K_DOWN]:
            if self.rect.bottom < info.current_h:
                self.rect.y += self.speed_y
    def make_hitbox(self):
        self.hitbox = Rect(0, 0, info.current_w//100, info.current_h//5)

class Ball(Unit):
    def move(self):
        self.rect.y -= self.speed_y
        self.rect.x -= self.speed_x
        if self.rect.bottom > info.current_h:
            self.speed_y *= -1
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.right > info.current_w:
            self.speed_x *= -1
            self.rect.centerx = info.current_w//2
            self.rect.centery = info.current_h//2
            time.wait(1000)
        if self.rect.left < 0:
            self.speed_x *= -1
            self.rect.centerx = info.current_w//2
            self.rect.centery = info.current_h//2
            time.wait(1000)
    def collide(self):
        if self.rect.colliderect(player_1.hitbox):
            self.speed_x = -5


player_1 = Player("player.png", info.current_w//10, info.current_h//2, info.current_w//5, info.current_h//5, 0, 10)
player_1.make_hitbox()
cross = Unit("Cross Quit.png", info.current_w//1.05, info.current_h//9, info.current_h//15, info.current_h//15, 0, 0)
ball = Ball("Ball.png", info.current_w//2, info.current_h//2, info.current_w//20, info.current_w//20, 5, 5)

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
    player_1.draw()
    player_1.move()
    ball.draw()
    ball.move()
    ball.collide()
    display.update()
    fps.tick(60)