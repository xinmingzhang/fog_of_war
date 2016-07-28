import pygame as pg
from player import Player
from wolf import Wolf

from prepare import SCREEN_RECT


class Fog(pg.sprite.Sprite):
    def __init__(self,*groups):
        super(Fog, self).__init__(*groups)
        self.rect = SCREEN_RECT
        self.image = pg.Surface(self.rect.size,pg.SRCALPHA)
        self.visible_area = self.image.copy()
        self.image.fill((0,0,0,220))
        self.footprint = self.rect
        self.footprint.midbottom = self.rect.midbottom
        self.mask = pg.mask.from_surface(self.visible_area)



    def update(self,pos):
        player_surface = pg.Surface(self.rect.size).convert_alpha()
        for i in range(220,0,-10):
            pg.draw.circle(player_surface,(0,0,0,i),(int(pos[0]),int(pos[1])),int(i/220.0*10+90))
        pg.draw.circle(player_surface,(0,0,0,0),(int(pos[0]),int(pos[1])),90)
        self.image.blit(player_surface,(0,0),special_flags=pg.BLEND_RGBA_MIN)
        pg.draw.circle(self.visible_area, (255, 0, 0), (int(pos[0]), int(pos[1])), 80)
        self.mask = pg.mask.from_surface(self.visible_area)


    def draw(self,surface):
        surface.blit(self.image,self.rect)
