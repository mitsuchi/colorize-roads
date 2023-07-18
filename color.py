import cv2
import math
import numpy as np
import os
import sys
from pylsd import lsd

full_name = sys.argv[1]
folder, img_name = os.path.split(full_name)
img = cv2.imread(full_name, cv2.IMREAD_COLOR)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
segments = lsd(img_gray, scale=0.5)

blank_image = np.zeros_like(img)

# 塗りつぶす色の指定 (BGR形式)
fill_color = (233, 242, 245)  # 例: 赤色 (Blue=0, Green=0, Red=255)

# 塗りつぶし処理
filled_image = np.copy(blank_image)  # 画像のコピーを作成

# 画像全体を指定した色で塗りつぶす
filled_image[:, :] = fill_color

colors = [
    (77, 0, 186),
    (38, 23, 222),
    (0, 111, 239),
    (0, 175, 234),
    (0, 186, 196),
    (50, 168, 55),
    (108, 144, 0),
    (134, 122, 0),
    (140, 106, 0),
    (155, 74, 17),
    (141, 40, 115),
    (116, 0, 146),
]

for i in range(segments.shape[0]):
    pt1 = (int(segments[i, 0]), int(segments[i, 1]))
    pt2 = (int(segments[i, 2]), int(segments[i, 3]))
    width = segments[i, 4]
    rad = - math.atan2(pt2[1] - pt1[1], pt2[0] - pt1[0]) * 24 / math.pi
    if rad < 0:
        rad += 24
    radInt = (int(rad + 3) % 12)
    color = colors[radInt]
    cv2.line(filled_image, pt1, pt2, color, 2)

cv2.imwrite(os.path.join(folder, 'color_' + img_name.split('.')[0] + '.jpg'), filled_image)