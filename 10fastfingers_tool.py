import pyautogui
import pyperclip
import time

word_html=open("words.txt","r",encoding="utf-8").read().split("<span wordnr=")
time.sleep(5)
a=1
for x in kelimeler:
    y=x.strip(" 1234567890\"<>/")[9:].split("</span")[0]
    if '"' in y:
        if "style" in y:
            y=""
        else:
            y=x.strip(" 1234567890\"<>/")[9:].split("</span")[0].split('"')[1][1:]
    print(y)
    if a !=1:
        pyperclip.copy(y)
        pyautogui.hotkey("ctrl", "v")
    pyautogui.press("space")
    time.sleep((30/int(len(word_html))))
    a=a+1