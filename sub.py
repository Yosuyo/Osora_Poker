import pyautogui as pgui

sc = pgui.screenshot(region=(90, 275, 330, 55))
sc.save("sc.png")