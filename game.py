import pygame

class Piece(pygame.sprite.Sprite): # Parent Class
  def __init__(self, path_img, player, x, y):
    self.image = pygame.image.load(path_image) 
    self.rect = self.image.get_rect()
    self.rect.move(x,y) #TRY GOEMETRICS
    self.xpos = x
    self.ypos = y
    self.selected = False
  
  
class Tower(Piece): # Child class of Piece , single inheritance.

    def __init__(self, path_img, player, x, y):
      super(Tower, self).__init__(path_img, player, x, y)
