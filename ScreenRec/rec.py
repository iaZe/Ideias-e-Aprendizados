import cv2
import numpy as np
import pyautogui as pag
import datetime

SCREEN_SIZE = (1366, 768)
name = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(f"{name}.avi", fourcc, 20.0, (SCREEN_SIZE))

while True:
    img = pag.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
out.release()