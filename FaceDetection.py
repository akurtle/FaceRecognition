import cv2
import mediapipe as mp
import time

from os import path



cap = cv2.VideoCapture('1.mp4')

pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils

faceDetection = mpFaceDetection.FaceDetection()


while True:
    success,img = cap.read()    
    

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results = faceDetection.process(imgRGB)


    if results.detections:
        for id, detection in enumerate(results.detections):
            # mpDraw.draw_detection(img,detection)
            
            # print(detection.location_data.relative_bounding_box)

            ih,iw,ic = img.shape

            bboxC = detection.location_data.relative_bounding_box
            bbox = int(bboxC.xmin* iw),int(bboxC.ymin* ih),\
            int(bboxC.width* iw),int(bboxC.height* ih)

            cv2.rectangle(img,bbox,(255,0,255),2)
            

    cTime = time.time()

    fps = 1/(cTime-pTime)

    pTime = cTime

    cv2.putText(img,f"FPS:{int(fps)}",(20,70),cv2.FONT_HERSHEY_PLAIN,
                3,(0,255,0),2)

    cv2.imshow("Video",img)

    cv2.waitKey(1)