import cv2
def imgcv2(i):
    cv2.imshow("image",i)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

import matplotlib.pyplot as plt
def pltimg(i):
    img = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)# BGR (Blue-Green-Red) to RGB (Red-Green-Blue) format
    plt.imshow(img)
    plt.axis('off') 
    plt.show()