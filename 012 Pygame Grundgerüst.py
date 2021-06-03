import pygame as pg

fenster = pg.display.set_mode((800, 600))

weitermachen = True
clock = pg.time.Clock()

while weitermachen:
  fenster.fill((0, 0, 0))
  clock.tick(40)
  for ereignis in pg.event.get():
    if ereignis.type == pg.QUIT or \
       ereignis.type == pg.KEYDOWN and ereignis.key == pg.K_ESCAPE:
      weitermachen = False

  pg.display.flip()
