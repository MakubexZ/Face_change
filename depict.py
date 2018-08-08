# -*- coding: utf-8 -*-

import cv2


def depict_f(pic, dots):
    for i in range(16):
        cv2.line(pic, dots[i], dots[i + 1], (255, 0, 0), 1)
    for i in range(17, 21):
        cv2.line(pic, dots[i], dots[i + 1], (255, 0, 0), 1)
    cv2.line(pic, dots[17], dots[21], (255, 0, 0), 1)
    for i in range(22, 26):
        cv2.line(pic, dots[i], dots[i + 1], (255, 0, 0), 1)
    cv2.line(pic, dots[22], dots[26], (255, 0, 0), 1)
    for i in range(27, 35):
        cv2.line(pic, dots[i], dots[i + 1], (255, 0, 0), 1)
    cv2.line(pic, dots[30], dots[35], (255, 0, 0), 1)
    for i in range(36, 41):
        cv2.line(pic, dots[i], dots[i + 1], (255, 0, 0), 1)
    cv2.line(pic, dots[36], dots[41], (255, 0, 0), 1)
    for i in range(42, 47):
        cv2.line(pic, dots[i], dots[i + 1], (255, 0, 0), 1)
    cv2.line(pic, dots[42], dots[47], (255, 0, 0), 1)
    for i in range(48, 54):
        cv2.line(pic, dots[i], dots[i + 1], (255, 0, 0), 1)
    for i in range(60, 64):
        cv2.line(pic, dots[i], dots[i + 1], (255, 0, 0), 1)
    cv2.line(pic, dots[48], dots[60], (255, 0, 0), 1)
    cv2.line(pic, dots[54], dots[64], (255, 0, 0), 1)
    for i in range(64, 67):
        cv2.line(pic, dots[i], dots[i + 1], (255, 0, 0), 1)
    for i in range(54, 59):
        cv2.line(pic, dots[i], dots[i + 1], (255, 0, 0), 1)
    cv2.line(pic, dots[48], dots[67], (255, 0, 0), 1)
    cv2.line(pic, dots[48], dots[59], (255, 0, 0), 1)
    cv2.line(pic, dots[54], dots[64], (255, 0, 0), 1)