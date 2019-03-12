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
    global hand
    sample = Image.open(R"G:\AutoPoker\data\JOKER.png")
    try:
        x, y = pgui.locateCenterOnScreen(sample, region=(35, 400, 370, 55), confidence=0.980, grayscale=True)
        hand.append([x, y, 0, 0])
        print("JOKER")
    except:
        pass

    n = 1
    for name in club:
        if len(hand) == 5:
            break
        
        sample = f"G:\AutoPoker\data\{name}.png"
        search = Image.open(sample)
        try:
            x, y = pgui.locateCenterOnScreen(search, region=(35, 400, 370, 55), confidence=0.980, grayscale=True)
            hand.append([x, y, 1, n])
            print(name)
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
            x, y = pgui.locateCenterOnScreen(search, region=(35, 400, 370, 55), confidence=0.980, grayscale=True)
            hand.append([x, y, 2, n])
            print(name)
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
            x, y = pgui.locateCenterOnScreen(search, region=(35, 400, 370, 55), confidence=0.980, grayscale=True)
            hand.append([x, y, 3, n])
            print(name)
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
            x, y = pgui.locateCenterOnScreen(search, region=(35, 400, 370, 55), confidence=0.980, grayscale=True)
            hand.append([x, y, 4, n])
            print(name)
        except:
            pass
        n += 1

#ジョーカー判定
def joker():
    global hand
    for card in hand:
        if card[2] == 0:
            pgui.click(card[0], card[1])
            hand.remove(card)
            global JOKER
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
            for card in hand:
                if n[0] == card[2]:
                    pgui.click(card[0], card[1])
                    time.sleep(0.3)
            global FIN
            FIN = 1
            suit.clear()
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
            global FIN
            FIN = 1
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


#選択セクション     
def choice():
    check() #存在するカードの情報をhandに加える
    joker() #ジョーカーが存在した場合handから削除し、JOKERフラグを立てる
    pair()  #スリーペア期待ハンドの対応
    if FIN == 0:
        flush() #フラッシュ期待ハンドの対応
    start()

#High and Lowセクション
def highlow():
    num = 0
    for name in range(2, 15):
        ad = f"G:\AutoPoker\data\{name}.png"
        numImage = Image.open(ad)
        try:
            pgui.locateOnScreen(numImage, region=(120, 365, 40, 40), confidence=0.900, grayscale=True)
            print("High and Low", name)
            num = name
            break
        except:
            pass
    if num == 0:
        pass
    elif 1 <= num <= 8:
        print("HIGH")
        no()
    elif 9 <= num <= 14:
        print("LOW")
        yes()
    
#指示判定と対応
def order():
    ORDER = 0
    if ORDER == 0:
        hold = Image.open(R"G:\AutoPoker\data\hold.png")
        try:
            pgui.locateOnScreen(hold, region=(120, 310, 260, 50), confidence=0.950, grayscale=True)
            print("ホールドするカードを選択")
            choice()
            ORDER = 1
        except:
            pass
    if ORDER == 0:
        restart = Image.open(R"G:\AutoPoker\data\restart.png")
        try:
            pgui.locateOnScreen(restart, region=(120, 310, 260, 50), confidence=0.950, grayscale=True)
            print("STARTで再挑戦できます")
            start()
            ORDER = 1
        except:
            pass
    if ORDER == 0:
        highOrLow = Image.open(R"G:\AutoPoker\data\highOrLow.png")
        try:
            pgui.locateOnScreen(highOrLow, region=(75, 280, 350, 50), confidence=0.950, grayscale=True)
            print("HighかLowを選んでください")
            highlow()
            ORDER = 1
        except:
            pass
    if ORDER == 0:
        doubleUp = Image.open(R"G:\AutoPoker\data\doubleUp.png")
        try:
            pgui.locateOnScreen(doubleUp, region=(110, 310, 270, 50), confidence=0.950, grayscale=True)
            print("ダブルアップに挑戦しますか？")
            yes()
            ORDER = 1
        except:
            pass
    if ORDER == 0:
        Continue = Image.open(R"G:\AutoPoker\data\continue.png")
        try:
            pgui.locateOnScreen(Continue, region=(110, 275, 270, 50), confidence=0.950, grayscale=True)
            print("続けて挑戦しますか？")
            yes()
            ORDER = 1
        except:
            pass
    if ORDER == 0:
        restart = Image.open(R"G:\AutoPoker\data\restart2.png")
        try:
            pgui.locateOnScreen(restart, region=(110, 275, 290, 55), confidence=0.950, grayscale=True)
            print("STARTでポーカーを始めます")
            start()
            ORDER = 1
        except:
            pass
    if ORDER == 0:
        restart = Image.open(R"G:\AutoPoker\data\restart3.png")
        try:
            pgui.locateOnScreen(restart, region=(90, 275, 330, 55), confidence=0.950, grayscale=True)
            print("STARTで再度ポーカーを始めます")
            start()
            ORDER = 1
        except:
            pass
    if ORDER == 0:
        order()

#リストとフラグの初期化
def flag():
    global hand
    hand.clear()
    global JOKER
    JOKER = 0
    global FIN
    FIN = 0

hand = []
JOKER = 0
FIN = 0

for c in range(500):
    print("try", c+1)
    flag()
    order()