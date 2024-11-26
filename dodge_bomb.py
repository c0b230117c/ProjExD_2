import os
import random
import sys
import time 
from datetime import datetime

import pygame as pg


WIDTH, HEIGHT = 1100, 650
DELTA = {
    pg.K_UP: (0,-5),
    pg.K_DOWN: (0,+5),
    pg.K_LEFT: (-5,0),
    pg.K_RIGHT: (+5,0),
    }
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def check_bound(rct:pg.Rect) -> tuple[bool,bool]:
    """
    引数で与えられたRectが画面の中か外か判定する
    引数：こうかとんRect or 爆弾rect
    戻り値：真理値タプル（横、縦）/画面内：True、画面外：False
    """
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:
        tate = False
    return yoko,tate

def game_over(screen: pg.Surface) -> None:
    re = pg.Surface((1100,650))
    pg.draw.rect(re, (0,0,0), (0,1100,0,560))
    #screen = pg.Surface.set_alpha()
    re.set_alpha(122)
    fonto = pg.font.Font(None,80)
    txt = fonto.render("Game Over", True, (255,255,255))
    txt_rct = txt.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    cry_img = pg.transform.rotozoom(pg.image.load("fig/8.png"), 0, 0.9)
    cry_rct = cry_img.get_rect(center=((WIDTH // 4)+80, HEIGHT // 2)) #適切な位置に微調整
    cry2_rct = cry_img.get_rect(center=((WIDTH // 4)+100+380, HEIGHT // 2))
    screen.blit((re), (0, 0))
    screen.blit(txt, txt_rct)
    screen.blit(cry_img, cry_rct)
    screen.blit(cry_img, cry2_rct)

    pg.display.update()
    time.sleep(5)
    return re

def init_bb_imgs() -> tuple[list[pg.Surface], list[int]]:
    accs = [a for a in range(1,11)]
    lst = []
    for r in range(1,11):
        bb_img = pg.Surface((20*r, 20*r))
        pg.draw.circle(bb_img, (255,0,0),(10*r,10*r),10*r)
        bb_img.set_colorkey((0,0,0))
        lst.append(bb_img)

    return lst,accs

def get_kk_img(sum_mv: tuple[int, int]) -> pg.Surface:
    
    return 

def calc_orientationn(org: pg.Rect, dst: pg.Rect, current_xy: tuple[float, float]) -> tuple[float,float]:

    return
    


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    kk_img = get_kk_img((0,0))
    kk_img = get_kk_img(tuple(sum_mv))
    bb_img = pg.Surface((20,20)) #爆弾用の空サーフェイス
    pg.draw.circle(bb_img, (255,0,0), (10,10), 10) #爆弾円を描く
    bb_img.set_colorkey((0,0,0)) #四隅の黒を透過させる
    bb_rct = bb_img.get_rect() #爆弾rectの抽出
    bb_rct.center = random.randint(0,WIDTH), random.randint(0,HEIGHT)
    clock = pg.time.Clock()
    tmr = 0
    vx, vy = +5, +5
    vx, vy = calc_orientationn(bb_rct, kk_rct, (vx,vy))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(bb_rct):
            
            return game_over(screen)
            
        screen.blit(bg_img, [0, 0]) 

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for key, tpl in DELTA.items():
            if key_lst[key]:
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]
        
        kk_rct.move_ip(sum_mv)
        #こうかとんが画面外なら、元の場所に戻す
        if check_bound(kk_rct) != (True,True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1]) 
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx,vy)
        yoko, tate = check_bound(bb_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        bb_rct.move_ip(vx,vy)
        bb_imgs, bb_accs = init_bb_imgs()
        avx = vx*bb_accs[min(tmr//500, 9)]
        bb_img = bb_imgs[min(tmr//500, 9)]
        screen.blit(bb_img, bb_rct)
        
        pg.display.update()
        tmr += 1
        clock.tick(50)
        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
