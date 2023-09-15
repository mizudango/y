### インポート
import sys
import pygame
from pygame.locals import *

### 定数
WIDE   = 640  # 画面横サイズ
HIGHT  = 400  # 画面縦サイズ
M_DOT  = 20   # 移動ドットs
W_TIME = 20   # 待ち時間

 
### メイン関数
def main():
    pygame.init()
    surface = pygame.display.set_mode((WIDE, HIGHT))
    pygame.display.set_caption("PONG")
    icon=pygame.image.load('pong_atari.jpg')
    pygame.display.set_icon(icon)
 
    ### 変数初期化
    x = 15
    y = 155
    x2= 599.333333333338
    y2= 155
    BallX=320
    BallY=200
    BallSpeedX=2
    BallSpeedY=2
    Bounce=False
 
 
    while True:
 
        ### 描画
        surface.fill((0,0,0))
        pygame.draw.rect(surface, (255,255,255), pygame.Rect(x,y,15,50))
        pygame.draw.rect(surface, (255,255,255), pygame.Rect(x2,y2,15,50))
        pygame.draw.rect(surface, (240,240,240), pygame.Rect(310,0,15,400))
        pygame.draw.circle(surface, (255,255,255), (BallX,BallY),(5))
        pygame.display.update()
        pygame.time.wait(W_TIME)
        if BallX>640:
            BallSpeedX=-2
            pygame.mixer.music.load("決定ボタンを押す31.mp3") #読み込み
            pygame.mixer.music.play(1) #再生
        if BallY>400:
            BallSpeedY=-2
            pygame.mixer.music.load("決定ボタンを押す31.mp3") #読み込み
            pygame.mixer.music.play(1) #再生
        if BallX<0:
            BallSpeedX=2
            pygame.mixer.music.load("決定ボタンを押す31.mp3") #読み込み
            pygame.mixer.music.play(1) #再生
        if BallY<0:
            pygame.mixer.music.load("決定ボタンを押す31.mp3") #読み込み
            pygame.mixer.music.play(1) #再生
            BallSpeedY=2
        if BallX>x and BallX<x+15 and BallY>y and BallY<y+50:
            BallSpeedX=2
            pygame.mixer.music.load("決定ボタンを押す44.mp3") #読み込み
            pygame.mixer.music.play(1) #再生
        if  BallX>x2 and BallX<x2+15 and BallY>y2 and BallY<y2+50:
            BallSpeedX-=2
            pygame.mixer.music.load("決定ボタンを押す44.mp3")
            pygame.mixer.music.play(1)
        BallX+=BallSpeedX
        BallY+=BallSpeedY
 
        ### イベント取得
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                if event.key == K_UP:
                    if y > 0:
                        y -= M_DOT
                if event.key == K_DOWN:
                    if y<400 - 50:
                        y += M_DOT
                if event.key == K_w:
                    if y2>0 - 50:
                        y2 -= M_DOT
                if event.key == K_s:
                    if y2<400 - 50:
                        y2 += M_DOT 
### 終了関数
def exit():
    pygame.quit()
    sys.exit()
 
### メイン関数呼び出し
if __name__ == "__main__":
    main()