
# autoit.run("C:\\Program Files (x86)\\Ping Identity\\PingID\\PingID.exe")
# time.sleep(10)

import subprocess
import pyautogui
import time
def handle_pingid():
    # 1. Open the application (.exe)
    # Replace "notepad.exe" with the full path to your PingID exe if needed
    app_path = "C:\\Program Files (x86)\\Ping Identity\\PingID\\PingID.exe"
    subprocess.Popen(app_path)

    # 2. Wait for the application to fully load and gain focus
    # Increase this if the app takes longer to open
    time.sleep(10)

    # 3. Perform actions
    # Type the text (interval adds a human-like delay between keys)
    pyautogui.press('tab', presses=2, interval=0.25)
    pyautogui.write("0143440", interval=0.1)

    # Press a specific key (like Enter or Tab)
    pyautogui.press("enter")
    time.sleep(10)
    pyautogui.press('tab', presses=1, interval=0.25)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(2)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(5)
