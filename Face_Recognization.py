import cv2, numpy as np;
import sys
import xlwrite
import time

 

face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0);
recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read('trainer/trainer.yml');
flag = 0;
id=0;
filename='filename';
dict = {
            'item1': 1
}

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cas.detectMultiScale(gray, 1.3, 7);
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2);
        id,conf=recognizer.predict(roi_gray)
        if(conf < 50):
         if(id==1):
            name = 'Ajay Chaudhari'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',1,name,'yes');
                dict[str(id)]=str(id);
            cv2.putText(img, "Ajay", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', img)
                
         elif(id==2):
            name = 'Aashu Kansagara'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',2,name,'yes');
                dict[str(id)]=str(id);
            cv2.putText(img, "Aashu", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', img)

         elif(id==3):
            name = 'Deep Parmar'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',3,name,'yes');
                dict[str(id)]=str(id);
            cv2.putText(img, "Deep", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', img)

         elif(id==4):
            name = 'Kasab'
            if((str(id)) not in dict):
                filename=xlwrite.output('attendance','class1',4,name,'yes');
                dict[str(id)]=str(id);
            cv2.putText(img, "Kasab", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', img)

        else:
            flag = flag+1
            cv2.putText(img, "Unknown!!!", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
            cv2.imshow('Face Cropper', img)
            break
        
        cv2.putText(img,str(id)+" "+str(conf),(x,y-10),font,0.55,(120,255,120),1)
        
    if cv2.waitKey(1)==13:
        break

cap.release();
cv2.destroyAllWindows();
