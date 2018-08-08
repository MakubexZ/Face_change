# -*- coding: utf-8 -*-

import numpy as np
import cv2


def cover(pic, pnt):
    cover0 = np.zeros(pic.shape[:2], np.uint8)
    pnts = np.float32([pnt[17], pnt[6], pnt[26], pnt[10]])
    #cv2.circle(pic, pnt[17], 3, (0, 0, 255), -1)
    #cv2.circle(pic, pnt[6], 3, (0, 0, 255), -1)
    #cv2.circle(pic, pnt[26], 3, (0, 0, 255), -1)
    #cv2.circle(pic, pnt[10], 3, (0, 0, 255), -1)

    #cv2.line(pic, pnt[6], pnt[10], (255, 255, 255), 1)
    #cv2.line(pic, pnt[10], pnt[26], (255, 255, 255), 1)
    #cv2.line(pic, pnt[26], pnt[17], (255, 255, 255), 1)
    #cv2.line(pic, pnt[17], pnt[6], (255, 255, 255), 1)

    chain = np.array(pnt[0:17] + pnt[24:27][::-1] + pnt[17:20][::-1])
    cv2.fillConvexPoly(cover0, chain, (255, 255, 255))
    face0 = cv2.bitwise_and(pic, pic, mask=cover0)
    #delt = 10
    #face = face0[(min(pnt[20][1], pnt[25][1])-delt): (pnt[9][1]+delt), (pnt[0][0]-delt):(pnt[16][0]+delt)]
    #cv2.imshow('cover', cover0)
    #cv2.imwrite('D://Python//facechange//pic//cover.jpg', cover0)
    return face0, pnts, cover0