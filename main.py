import cv2 as cv
import numpy as np
from coin import Coin


def main(file_path: str) -> None:
    # use OpenCV library to read the img file
    img_src = cv.imread(file_path, cv.IMREAD_COLOR)

    # create a grayscale copy for use with algorithm, add blur to reduce noise
    img_gray = cv.cvtColor(img_src, cv.COLOR_BGR2GRAY)
    img_gray = cv.medianBlur(img_gray, 5)

    img_rows = img_gray.shape[0]

    # use Hough Circles algorithm to find circles within the image
    img_circles = cv.HoughCircles(
        img_gray, cv.HOUGH_GRADIENT, 1, img_rows / 6, param1=50, param2=30, minRadius=55, maxRadius=130
    )

    # create an empy list to put each coin found into
    purse = []
    # use numpy to get the coordinates from the open cv object
    circles = np.uint16(np.around(img_circles))
    # iterate over coordinates
    for circle in circles[0, :]:
        # get brightness value of coin using subsection of img
        brightness_value = np.mean(img_src[circle[1] - 20:circle[1] + 20, circle[0] - 20:circle[0] + 20])
        # create coin object and add to purse list
        coin = Coin((circle[0], circle[1]), circle[2], brightness_value)
        purse.append(coin)
        # draw circles using coin object
        cv.circle(img_src, coin.center, coin.radius, (0, 255, 0), 2)
        # draw center point using coin object
        cv.circle(img_src, coin.center, 1, (0, 0, 255), 3)
        # write coin value to img using coin properties
        cv.putText(img_src, f'{str(coin.value)}p', coin.center, 1,  2, (255, 255, 255), 2)

    # get the total value of the coins found
    values = [coin.value for coin in purse]
    # write total to img
    cv.putText(img_src, f'Estimated total value: {sum(values)}p', (200, 100), 1,  2, (255, 255, 255), 2)
    # show the img to user
    cv.imshow("Image", img_src)
    cv.waitKey(0)


if __name__ == '__main__':
    main('coins.png')
