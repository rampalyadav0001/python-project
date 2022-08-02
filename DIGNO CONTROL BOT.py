from email.mime import image
import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
# from numpy import asarray
import time
# how to take a screenshot
# def takescreenshot():
#     image=ImageGrab.grab()
#     image.show()

# if __name__== "__main__":     #calling of function here
#     time.sleep(1)
#     takescreenshot()


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Draw the rectangle for birds
    for i in range(250, 300):
        for j in range(250, 300):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(240, 280):
        for j in range(480, 520):
            if data[i, j] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # print(asarray(image))
    '''
        # Draw the rectangle for cactus
        for i in range(200, 240):
            for j in range(480,550 ):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(250, 300):
            for j in range(200, 280):
                data[i, j] = 171

        image.show()
        break
    '''
