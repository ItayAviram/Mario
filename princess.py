from character import Character
import pygame


gravity = 10


class Princess(Character):
    # noinspection PyMissingConstructor
    def __init__(self, pos, image, leaves, throws=3, health=3):
        self.x, self.y = pos[0], pos[1]  # (x, y)
        self.image = image  # type: pygame.Surface
        image.fill("white")
        self.rect = self.image.get_rect(topleft=pos)
        self.leaves = leaves
        self.throws = throws
        self.health = health
        # movement:
        #   constants:
        self.x_speed_mul = 8
        self.jump_height = 8
        self.gravity = 0.25
        #   changeables:
        self.direction = 0  # direction of x
        self.yvel = 0

    def set_x(self, val):
        self.x = val
        self.rect.left = val

    def set_y(self, val):
        self.y = val
        self.rect.top = val

    def move_x(self):
        self.set_x(self.x + self.direction * self.x_speed_mul)

    def move_y(self):
        self.set_y(self.y + self.yvel)

    def jump(self):
        self.yvel = self.jump_height * (-1)

    def stop_x(self):
        self.direction = 0

    def stop_y(self):
        self.yvel = 0

    def stop(self):
        self.stop_x()
        self.stop_y()


    def accelerate(self):
        self.yvel += self.gravity

    def die(self):
        pass
        # if self.health > 0:
        #     self.update_health(self.health - 1)

    def speak(self, what_to_say):
        pass

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction = 1
        elif keys[pygame.K_a]:
            self.direction = -1
        else:
            self.direction = 0
        if keys[pygame.K_w]:
            self.jump()
        if keys[pygame.K_SPACE]:
            self.stop()

    def update(self, tiles):
        print(self.yvel)
        self.get_input()
        self.move_x()
        self.check_collision_horizontal(tiles)
        self.move_y()
        self.check_collision_vertical(tiles)

        self.accelerate()

    def update_health(self, val):
        self.health = val

    def update_leaves(self, val):
        self.leaves = val

    def get_rect(self):
        return self.rect

    def check_collision_horizontal(self, tiles):
        for tile in tiles:
            col = tile.check_collision_horizontal(self)
            if col:
                print(col)

    def check_collision_vertical(self, tiles):
        for tile in tiles:
            col = tile.check_collision_vertical(self)
            if col:
                print(col)

    def set_rect_left(self, val):
        self.rect.left = val
        self.x = self.rect.left

    def set_rect_right(self, val):
        self.rect.right = val
        self.x = self.rect.left

    def set_rect_top(self, val):
        self.rect.top = val
        self.y = self.rect.top

    def set_rect_bottom(self,val):
        self.rect.bottom = val
        self.y = self.rect.top
