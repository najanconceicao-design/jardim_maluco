pastar: personagens.py
 class Player(pygame.sprite.Sprite):
       def __init__(self, x, y):

       def get_input(self):

       def toggle_mode(self):
       if self.mode == "SCISSORS":
            self.mode = "WATERING_CAN"
     
       def apply_gravity(self):

       def update(self, platforms):

       def horizontal_collision(self, platforms):

       def vertical_collision(self, platforms):


class Plant(pygame.sprite.Sprite):
      def __init__(self, x, y, weakness, color):

      def update_cooldown(self):


class ShortRangePlant(Plant):
      def __init__(self, x, y, weakness):
        super().__init__(x, y, weakness, RED)

      def behavior(self, player):


class LongRangePlant(Plant):
      def __init__(self, x, y, weakness):
        super().__init__(x, y, weakness, YELLOW)

      def behavior(self, player, projectile_group):


class HealingPlant(Plant):
      def __init__(self, x, y):
      super().__init__(x, y, "WATERING_CAN", BLUE)



class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction_x):

    def update(self, platforms, player):
        self.rect.x += self.speed
