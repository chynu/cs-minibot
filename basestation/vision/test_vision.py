import cv2
import numpy as np
import time

def read_position(img):
    # bimg = cv2.GaussianBlur(img, (4, 4), 2, 2)
    gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sta = time.time()
    bimg = cv2.medianBlur(gimg, 5)
    # b,g,r = cv2.split(bimg)
    circles = cv2.HoughCircles(bimg, cv2.HOUGH_GRADIENT, 1, 100,
                param1 = 100, param2 = 60, minRadius = 100, maxRadius = 0)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        
        for i in circles[0,:]: # x, y, r = i
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    
    return img

if __name__ == "__main__":
    # Read codes from a camera
    width = 1280
    height = 720
    fps = 30
    
    vc = cv2.VideoCapture(0)
    vc.set(cv2.CAP_PROP_FRAME_WIDTH,  width)
    vc.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    vc.set(cv2.CAP_PROP_FPS, fps)

    # Main GUI loop
    cv2.namedWindow("camera")
    frame = 0
    while True:
        ret, img = vc.read()
        if ret and img is not None:
            dimg = read_position(img)
            cv2.imshow("camera", dimg)

        key = cv2.waitKey(1)
        if key == 27:
            # Quit
            break

        frame += 1

    # Clean up
    vc.release()
    cv2.destroyAllWindows()
    