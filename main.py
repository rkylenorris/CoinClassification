import cv2 as cv
import numpy as np
from coin import Coin

def main(file_path: str) -> None:
    img_src = cv.imread(file_path, cv.IMREAD_COLOR)

    img_gray = cv.cvtColor(img_src, cv.COLOR_BGR2GRAY)
    img_gray = cv.medianBlur(img_gray, 5)

    img_rows = img_gray.shape[0]

    img_circles = cv.HoughCircles(
        img_gray, cv.HOUGH_GRADIENT, 1, img_rows / 6, param1=50, param2=30, minRadius=55, maxRadius=130
    )

    purse = []
    circles = np.uint16(np.around(img_circles))
    for circle in circles[0, :]:
        # create coin object
        brightness_value = np.mean(img_src[circle[1] - 20:circle[1] + 20, circle[0] - 20:circle[0] + 20])
        coin = Coin((circle[0], circle[1]), circle[2], brightness_value)
        purse.append(coin)
        # draw circles
        cv.circle(img_src, coin.center, coin.radius, (0, 255, 0), 2)
        # draw center point
        cv.circle(img_src, coin.center, 1, (0, 0, 255), 3)
        cv.putText(img_src, f'{str(coin.value)}p', coin.center, 1,  2, (255, 255, 255), 2)

    values = [coin.value for coin in purse]
    cv.putText(img_src, f'Estimated total value: {sum(values)}p', (200, 100), 1,  2, (255, 255, 255), 2)
    cv.imshow("Image", img_src)
    cv.waitKey(0)


if __name__ == '__main__':
    main('coins.png')
