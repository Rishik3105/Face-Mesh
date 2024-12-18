import cv2 as cv
import mediapipe as mp
import time

cap=cv.VideoCapture(0)
mpFaceMesh=mp.solutions.face_mesh
facemesh=mpFaceMesh.FaceMesh(max_num_faces=3)
mpdraw=mp.solutions.drawing_utils
drawspec=mpdraw.DrawingSpec(thickness=1,circle_radius=2,color=(25,0,255))
ptime=0
while True:
    ret,img=cap.read()
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results=facemesh.process(imgRGB)
    if results.multi_face_landmarks:
        for facelms in results.multi_face_landmarks:
            mpdraw.draw_landmarks(img,facelms,mpFaceMesh.FACEMESH_TESSELATION,drawspec,drawspec)
            for lm in facelms.landmark: 
                #print(f'LandMarks:{lm}') # Uncomment this line if you want to print the landmarks
                ih,iw,ic=img.shape
                x,y=int(lm.x*iw),int(lm.y*ih)
                print(f'Pixel values:{x,y}')
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv.imshow('Image',img)
    if cv.waitKey(20) & 0XFF==ord('q'):
        break
