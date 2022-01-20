import random
import pyautogui
import numpy as np
import time
from scipy import interpolate
import math


# Any duration less than this is rounded to 0.0 to instantly move the mouse.
pyautogui.MINIMUM_DURATION = 0  # Default: 0.1
# Minimal number of seconds to sleep between mouse moves.
pyautogui.MINIMUM_SLEEP = 0  # Default: 0.05
# The number of seconds to pause after EVERY public function call.
pyautogui.PAUSE = 0  # Default: 0.1

def clickOnScreen():
  pass

def point_dist(x1,y1,x2,y2):
  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def moveTo(x1, y1, x2, y2):
  cp = random.randint(3, 6)  # Number of control points. Must be at least 2.

  # Distribute control points between start and destination evenly.
  x = np.linspace(x1, x2, num=cp, dtype='int')
  y = np.linspace(y1, y2, num=cp, dtype='int')

  # Randomise inner points a bit (+-RND at most).
  RND = 10
  xr = [random.randint(-RND, RND) for k in range(cp)]
  yr = [random.randint(-RND, RND) for k in range(cp)]
  xr[0] = yr[0] = xr[-1] = yr[-1] = 0
  x += xr
  y += yr

  # Approximate using Bezier spline.
  degree = 3 if cp > 3 else cp - 1  # Degree of b-spline. 3 is recommended.
                                    # Must be less than number of control points.
  tck, u = interpolate.splprep([x, y], k=degree)
  # Move upto a certain number of points
  u = np.linspace(0, 1, num=2+int(point_dist(x1,y1,x2,y2)/50.0))
  points = interpolate.splev(u, tck)

  # Move mouse.
  duration = 0.1
  timeout = duration / len(points[0])
  point_list=zip(*(i.astype(int) for i in points))
  for point in point_list:
      pyautogui.moveTo(*point)
      time.sleep(timeout)


def main():
  while True:
    x1, y1 = pyautogui.position()
    x2 = random.randint(56, 248)
    y2 = random.randint(6, 27)
    moveTo(x1, y1, x2, y2) # move to tab
    pyautogui.click()
    sleepTime = random.random() + 0.2 
    time.sleep(sleepTime)
    x1, y1 = pyautogui.position()
    x2 = random.randint(916, 934)
    y2 = random.randint(673, 683)
    moveTo(x1, y1, x2, y2) # move to arrow that opens heroes
    pyautogui.click()
    sleepTime = random.random() + 0.3
    time.sleep(sleepTime)
    pyautogui.click()
    sleepTime = random.random() + 0.7
    time.sleep(sleepTime)
    x1, y1 = pyautogui.position()
    x2 = random.randint(832, 870)
    y2 = random.randint(301, 315)
    moveTo(x1, y1, x2, y2) # moves to all work
    pyautogui.click()
    sleepTime = random.random() + 0.3
    time.sleep(sleepTime)
    x1, y1 = pyautogui.position()
    x2 = random.randint(965, 993)
    y2 = random.randint(248, 263)
    moveTo(x1, y1, x2, y2) # moves to X
    pyautogui.click()
    sleepTime = random.random() + 0.5
    time.sleep(sleepTime)
    pyautogui.click()
    sleepTime = random.random() + 0.5
    time.sleep(sleepTime)
    x1, y1 = pyautogui.position()
    x2 = random.randint(297, 490)
    y2 = random.randint(6, 27)
    moveTo(x1, y1, x2, y2) # moves to second tab
    pyautogui.click()
    sleepTime = random.random() + 0.3
    time.sleep(sleepTime)
    

    waitTime = 0
    while(waitTime < 780):
      sleepTime = random.randint(1, 15)

      if(sleepTime + waitTime > 780):
        sleepTime = 780 - waitTime + random.randint(1, 30)
      
      x1, y1 = pyautogui.position()
      x2 = random.randint(0, 1920)
      y2 = random.randint(0, 1080)
      moveTo(x1, y1, x2, y2)
      time.sleep(sleepTime)
      waitTime += sleepTime

if __name__ == '__main__':
  main()