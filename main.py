import cv2
import pyautogui
import time
import numpy as np

def locate_element(template_image, threshold=0.8):
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    template = cv2.imread(template_image, cv2.IMREAD_GRAYSCALE)
    res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val >= threshold:
        return max_loc
    return None

def click_element(template_image, threshold=0.8):
    location = locate_element(template_image, threshold)
    if location:
        template = cv2.imread(template_image, cv2.IMREAD_GRAYSCALE)
        template_height, template_width = template.shape
        center_x = location[0] + template_width // 2
        center_y = location[1] + template_height // 2
        time.sleep(1)
        pyautogui.click(center_x, center_y)
        return True
    return False

def run_bot():
    pyautogui.press("win")
    time.sleep(1)

    pyautogui.typewrite("Steam")
    pyautogui.press("enter")
    time.sleep(1)

    template = "C:\\Users\\Matheus\\Documents\\Lightshot\\steam-play.png"
    if click_element(template):
        time.sleep(1)
    else:
        print("Botão 'Jogar' não encontrado.")

if __name__ == "__main__":
    run_bot()