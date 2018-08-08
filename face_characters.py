# -*- coding: utf-8 -*-

import cv2
import dlib
from depict import depict_f
from depict_frame import depict_fra

probe = dlib.get_frontal_face_detector()
character_predict = dlib.shape_predictor('D://Python//facechange//shape_predictor_68_face_landmarks.dat')


def face_character(pic):
    f = probe(pic, 1)
    if len(f) > 0:
        for i, retan in enumerate(f):
            characters = character_predict(pic, retan)
            character_coordinate = [(0, 0)]*68
            for j in range(68):
                character_coordinate[j] = (characters.part(j).x, characters.part(j).y)
                #cv2.putText(pic, '%s' % i, (characters.part(i).x, characters.part(i).y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (0, 0, 255), 1, cv2.LINE_8, 0)
            #depict_f(pic, character_coordinate)
            #depict_fra(pic, retan)
            return character_coordinate