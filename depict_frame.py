# -*- coding: utf-8 -*-

import cv2


def depict_fra(pic, d):
    x1 = d.left()
    y1 = d.top()
    x2 = d.right()
    y2 = d.bottom()
    delt = (x2 - x1) // 6
    cv2.rectangle(pic, (x1 + delt // 3, y1 + delt // 3), (x2 - delt // 3, y2 - delt // 3), (255, 255, 255), 1)
    cv2.line(pic, (x1, y1), (x1 + delt, y1), (255, 255, 255), 2)
    cv2.line(pic, (x1, y1), (x1, y1 + delt), (255, 255, 255), 2)
    cv2.line(pic, (x2, y1), (x2 - delt, y1), (255, 255, 255), 2)
    cv2.line(pic, (x2, y1), (x2, y1 + delt), (255, 255, 255), 2)
    cv2.line(pic, (x1, y2), (x1 + delt, y2), (255, 255, 255), 2)
    cv2.line(pic, (x1, y2), (x1, y2 - delt), (255, 255, 255), 2)
    cv2.line(pic, (x2, y2), (x2 - delt, y2), (255, 255, 255), 2)
    cv2.line(pic, (x2, y2), (x2, y2 - delt), (255, 255, 255), 2)