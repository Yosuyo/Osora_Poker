import pyautogui as pgui
import time
from os import chdir
from PIL import Image

#クリックコマンド
def start():
    pgui.click(250, 670)
def no():
    pgui.click(175, 670)
def yes():
    pgui.click(320, 670)

#カード画像のためのリスト
club = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13"]
diamond = ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "d12", "d13"]
heart = ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "h11", "h12", "h13"]
spade = ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13"]

#カードの検出とハンドリスト作成
def check():
    sample = Image.open(R"G:\AutoPoker\data\JOKER.png")
    try:
        x, y = pgui.locateCenterOnScreen(sample, region=(20, 380, 450, 170), confidence=0.980)
        hand.append([x, y, 0, 0])
    except:
        pass

    n = 1
    for name in club:
        if len(hand) == 5:
            break
        sample = f"G:\AutoPoker\data\{name}.png"
        search = Image.open(sample)
        try:
            x, y = pgui.locateCenterOnScreen(search, region=(20, 380, 450, 170), confidence=0.980)
            hand.append([x, y, 1, n])
        except:
            pass
        n += 1
            
    n = 1
    for name in diamond:
        if len(hand) == 5:
            break

        sample = f"G:\AutoPoker\data\{name}.png"
        search = Image.open(sample)
        try:
            x, y = pgui.locateCenterOnScreen(search, region=(20, 380, 450, 170), confidence=0.980)
            hand.append([x, y, 2, n])
        except:
            pass
        n += 1

    n = 1
    for name in heart:
        if len(hand) == 5:
            break

        sample = f"G:\AutoPoker\data\{name}.png"
        search = Image.open(sample)
        try:
            x, y = pgui.locateCenterOnScreen(search, region=(20, 380, 450, 170), confidence=0.980)
            hand.append([x, y, 3, n])
        except:
            pass
        n += 1

    n = 1
    for name in spade:
        if len(hand) == 5:
            break

        sample = f"G:\AutoPoker\data\{name}.png"
        search = Image.open(sample)
        try:
            x, y = pgui.locateCenterOnScreen(search, region=(20, 380, 450, 170), confidence=0.980)
            hand.append([x, y, 4, n])
        except:
            pass
        n += 1

#ジョーカー判定
def joker():
    for card in hand:
        if card[2] == 0:
            print("joker exists")
            pgui.click(num[0], num[1])
            hand.remove(num)
            JOKER = 1
            break

#フラッシュ系列
def flush():
    cl = [1,0]
    di = [2,0]
    he = [3,0]
    sp = [4,0]
    suit = [cl, di, he, sp]
    p = 4
    if JOKER == 1:
        p = 3
    for card in hand:
        if card[2] == 1:
            cl[1] += 1
        elif card[2] == 2:
            di[1] += 1
        elif card[2] == 3:
            he[1] += 1
        elif card[2] == 4:
            sp[1] += 1
    for n in suit:
        if n[1] >= p:
            print("flush " + n[1] + "枚 " + n[0])
            for card in hand:
                if n[0] == card[2]:
                    pgui.click(card[0], card[1])
                    time.sleep(0.3)
            FIN = 1
            break
                
#ペア系列
def pair():
    one = [1,0]
    two = [2,0]
    three = [3,0]
    four = [4,0]
    five = [5,0]
    six = [6,0]
    seven = [7,0]
    eight = [8,0]
    nine = [9,0]
    ten = [10,0]
    eleven = [11,0]
    twelve = [12,0]
    thirteen = [13,0]
    number = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen]
    for card in hand:
        for num in number:
            if card[3] == num[0]:
                num[1] += 1
    for num in number:
        if num[1] >= 2:
            for card in hand:
                if card[3] == num[0]:
                    pgui.click(card[0], card[1])
                    time.sleep(0.3)
            FIN = 1
        


#リストとフラグ
hand = []
JOKER = 0
FIN = 0

check() #存在するカードの情報をhandに加える
joker() #ジョーカーが存在した場合handから削除し、JOKERフラグを立てる
flush() #フラッシュ期待ハンドの対応
if FIN == 0:
    pair()  #スリーペア期待ハンドの対応