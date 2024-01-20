import random
import pygame

MAX_FRAMERATE = 60
SCREEN_SIZE = (1000, 600)


# player
class Player:
    def __init__(self):
        self.rect = pygame.Rect(500, 300, 50, 100)
        self.health = 100

    def playerInput(self):
        keys_pressed = pygame.key.get_pressed()
        if not self.rect.x < 0 or not self.rect.x > 1000:  # Player Input
            if keys_pressed[pygame.K_d]:
                if self.rect.right < screen.get_width() - 10:
                    self.rect.x += 5
            if keys_pressed[pygame.K_a]:
                if self.rect.left > 10:
                    self.rect.x += -5
            if keys_pressed[pygame.K_w]:
                if self.rect.top > 10:
                    self.rect.y += -5
            if keys_pressed[pygame.K_s]:
                if self.rect.bottom < screen.get_height() - 10:
                    self.rect.y += 5

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)

    def update(self):
        self.playerInput()
        self.draw()
        if self.health == 0:
            quit()


# Fruitje
class Druif:
    def __init__(self, druif_id):
        self.id = druif_id
        self.circle = None
        spawn_zone = None
        spawn_location = random.randint(1, 20)

        # // onder zeus
        if 15 > spawn_location > 5:
            self.x = random.randint(25, screen.get_width() - 25)
            self.y = random.randint(100, screen.get_height() - 25)
            spawn_zone = 1

        # // links van zeus
        elif spawn_location <= 5:
            self.x = random.randint(25, 200)
            self.y = random.randint(25, 100)
            spawn_zone = 2

        # // rechts van zeus
        elif spawn_location >= 15:
            self.x = random.randint(screen.get_width() - 200, screen.get_width() - 25)
            self.y = random.randint(25, 100)
            spawn_zone = 3

        print(f"Druif {self.id}, coörds: {(self.x, self.y)}, spawn zone: {spawn_zone}")

    def drawDruif(self):
        self.circle = pygame.draw.circle(screen, "yellow", (self.x, self.y), 25)

    def collision(self):
        if abs(player.rect.centerx - self.x) < 50 and abs(player.rect.centery - self.y) < 75:
            return True
        else:
            return False

    def update(self):
        self.drawDruif()


class Attack_1:
    pass


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill((255, 255, 255))
pygame.display.set_caption("Ricky & Caas Productions")

# kleuren
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Zeus
zeus = pygame.Rect((screen.get_width() / 2), 50, 50, 50)
zeus.x -= zeus.width / 2

# Player
player = Player()

# bg
bg_surface = pygame.transform.rotozoom(pygame.image.load("Resources\\Naamloos.png").convert(),0 ,1)
bg_rect = bg_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

# text
arial_font = pygame.font.SysFont('Arial', 50)


def main():
    counter = 0
    score = 0
    druifDict = {}
    while counter < 3:
        druifDict[counter] = Druif(counter)
        counter += 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.blit(bg_surface, bg_rect)
        screen.blit(arial_font.render(f'Score: {score}', True, (0, 0, 0)), (25, screen.get_height() - 75))
        for i, druif in druifDict.items():
            druif.update()
            if druif.collision():
                druifDict[druif.id] = Druif(druif.id)
                score += 1
        player.update()
        pygame.draw.rect(screen, RED, zeus)

        pygame.display.update()
        clock.tick(MAX_FRAMERATE)


if __name__ == "__main__":
    main()
