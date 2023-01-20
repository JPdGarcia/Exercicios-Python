import pyautogui as gui
import time
import pyperclip as clip

'''gui.PAUSE = .2
time.sleep(7)
print(gui.position())'''

gui.click(40,858)
gui.write('chro')
gui.press('enter')
clip.copy("https://luizalabs.swiftkanban.com/pui/index.jsp#projectid=359&itemtype=backlog")
gui.hotkey('ctrl', 'v')
gui.press('enter')

gui.hotkey('ctrl', 't')
clip.copy("https://magazineluiza.workplace.com/")
gui.hotkey('ctrl', 'v')
gui.press('enter')

gui.hotkey('ctrl', 't')
clip.copy("https://calendar.google.com/calendar/u/0/r?tab=rc")
gui.hotkey('ctrl', 'v')
gui.press('enter')

gui.click(40,858)
gui.write('slack')
gui.press('enter')
time.sleep(1)

gui.click(40,858)
gui.write('global')
gui.press('enter')
time.sleep(1)
gui.click(1302,283)
time.sleep(5)
gui.click(470,393)
time.sleep(1)
clip.copy("jop_garcia")
gui.press('tab')