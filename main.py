# -*- coding: utf-8 -*-

import cv2
from face_characters import face_character
from cover import cover

document1 = 'D://Python//facechange//pic//zhu.jpg'
document2 = 'D://Python//facechange//pic//Donald_Trump.jpg'


def main():
    pic1 = cv2.imread(document1)
    pic2 = cv2.imread(document2)
    h1, w1 = pic1.shape[:2]
    h2, w2 = pic2.shape[:2]
    character_coordinate1 = face_character(pic1)
    character_coordinate2 = face_character(pic2)
    f1, p1, cover1 = cover(pic1, character_coordinate1)
    f2, p2, cover2 = cover(pic2, character_coordinate2)
    #cv2.imshow('face1', f1)
    #cv2.imshow('face2', f2)
    #cv2.imshow('cover1', cover1)
    #cv2.imshow('cover2', cover2)

    #cv2.imwrite('D://Python//facechange//pic//face1.jpg', f1)
    #cv2.imwrite('D://Python//facechange//pic//face2.jpg', f2)
    #cv2.imwrite('D://Python//facechange//pic//cover1.jpg', cover1)
    #cv2.imwrite('D://Python//facechange//pic//cover2.jpg', cover2)

    M1 = cv2.getPerspectiveTransform(p1, p2)
    d11 = cv2.warpPerspective(f1, M1, (w2, h2))
    cover1_2 = cv2.warpPerspective(cover1, M1, (w2, h2))
    c1, hier1, rr1 = cv2.findContours(cover1_2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in hier1:
        x11, y11, w11, h11 = cv2.boundingRect(i)
    #cv2.rectangle(cover1_2, (x11,y11),(x11+w11, y11+h11), (255, 255, 255), 2)
    #cv2.line(cover1_2, (x11, y11), (x11+w11, y11+h11), (255, 255, 255), 1)
    #cv2.line(cover1_2, (x11+w11, y11), (x11, y11+h11), (255, 255, 255), 1)
    dot1 = (x11 + w11 // 2, y11 + h11 // 2)
    #cv2.circle(cover1_2, dot1, 3, (0, 0, 255), -1)

    #cv2.imshow('cover11', cover1_2)
    #cv2.imshow('cover2', d11)

    #cv2.imwrite('D://Python//facechange//pic//cover11.jpg', cover1_2)
    #cv2.imwrite('D://Python//facechange//pic//cover21.jpg', d11)

    cover_in1_2 = cv2.bitwise_not(cover1_2)
    d12 = cv2.bitwise_and(pic2, pic2, mask=cover_in1_2)
    d1_2 = cv2.add(d11, d12)
    pic1_2 = cv2.seamlessClone(d1_2, pic2, cover1_2, dot1, cv2.NORMAL_CLONE)
    cv2.imshow('d11', pic1)
    cv2.imshow('d1', pic1_2)
    cv2.imshow('d12', pic2)

    #cv2.imwrite('D://Python//facechange//pic//d11.jpg', pic1)
    #cv2.imwrite('D://Python//facechange//pic//d1.jpg', pic1_2)
    cv2.imwrite('D://Python//facechange//pic//Donald_Trumpandzhu.jpg', pic1_2)

    M2 = cv2.getPerspectiveTransform(p2, p1)
    d21 = cv2.warpPerspective(f2, M2, (w1, h1))
    cover2_1 = cv2.warpPerspective(cover2, M2, (w1, h1))
    c2, hier2, rr2 = cv2.findContours(cover2_1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for j in hier2:
        x21, y21, w21, h21 = cv2.boundingRect(j)
    cv2.rectangle(cover2_1, (x21, y21), (x21 + w21, y21 + h21), (255, 255, 255), 2)
    cv2.line(cover1_2, (x21, y21), (x21 + w21, y21 + h21), (255, 255, 255), 1)
    cv2.line(cover1_2, (x21 + w21, y21), (x21, y21 + h21), (255, 255, 255), 1)
    dot2 = (x21 + w21 // 2, y21 + h21 // 2)
    cv2.circle(cover2_1, dot2, 3, (0, 0, 255), -1)
    cover_in2_1 = cv2.bitwise_not(cover2_1)
    d22 = cv2.bitwise_and(pic1, pic1, mask=cover_in2_1)
    d2_1 = cv2.add(d21, d22)
    pic2_1 = cv2.seamlessClone(d2_1, pic1, cover2_1, dot2, cv2.NORMAL_CLONE)
    #cv2.imshow('d1', cover1_2)
    #cv2.imshow('d2', d2_1)
    #cv2.imshow('d2', pic2_1)

    #cv2.imwrite('D://Python//facechange//pic//cover1_2.jpg', cover1_2)
    #cv2.imwrite('D://Python//facechange//pic//d21.jpg', d2_1)
    #cv2.imwrite('D://Python//facechange//pic//d22.jpg', pic2_1)

    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()