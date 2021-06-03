import pygame as pg 

fenster = pg.display.set_mode((800,600))
x,y = 400,300
rx,ry = 16,16
s1x,s1y = 780,200
s2x,s2y = 0,200

weitermachen = True
clock = pg.time.Clock()

while weitermachen:
  fenster.fill((0,0,0))
  clock.tick(40)
  for ereignis in pg.event.get():
    if ereignis.type == pg.QUIT:
      weitermachen = False
  pg.draw.rect(fenster,(255,0,0),(x,y,20,20))
  pg.draw.rect(fenster,(0,0,255),(s1x,s1y,20,100))
  pg.draw.rect(fenster,(255,0,255),(s2x,s2y,20,100))
  s2y = pg.mouse.get_pos()[1]
  x+=rx
  y+=ry
  s1y = y-30
  if x > 780 or x < 20:
    rx = -rx
  if y > 600 or y < 0:
    ry = -ry
  pg.display.flip()    