import pygame as pg 

pg.init()
b,h = 800,600
screen = pg.display.set_mode((b,h))

paddle1 = pg.Rect(0,h/2,10,100)
paddle2 = pg.Rect(b-10,h/2,10,100)
pong = pg.Rect(b/2, h/2, 20, 20)
pong_richtung = [15,12]

weitermachen = True
clock = pg.time.Clock()
while weitermachen:
  clock.tick(40)
  screen.fill((0,0,0))
  for ereignis in pg.event.get():
    if ereignis.type == pg.QUIT:
      weitermachen = False
  paddle1[1] = pg.mouse.get_pos()[1]
  paddle2[1] = pong[1] - 50
  pg.draw.rect(screen,(255,255,255), paddle1)
  pg.draw.rect(screen,(255,255,255), paddle2)
  pg.draw.rect(screen,(255,255,255), pong)
  pong[0] += pong_richtung[0]
  pong[1] += pong_richtung[1]
  if pong[0] < 0 or pong[0] > b-20:
    pong_richtung[0] *= -1
  if pong[1] < 0 or pong[1] > h-20:
    pong_richtung[1] *= -1  
  pg.display.flip()

pg.quit()