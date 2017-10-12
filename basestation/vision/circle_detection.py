import cv2

def process_image(img):
    """
    Ha
    """
    bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return bw

if __name__ == "__main__":
    cv2.namedWindow("camera")

    # Setting up video capture.
    vc = cv2.VideoCapture(0)
    vc.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    vc.set(cv2.CAP_PROP_FPS, 30)

    while True:
        # Read data from webcam.
        ret, image = vc.read()
        display_img = process_image(image)
        cv2.imshow("camera", image)

        if cv2.waitKey(1) != -1:
            print("Exiting!")
            break
        
    cv2.destroyAllWindows()
