from asyncio.windows_events import NULL
from contextlib import nullcontext
from curses.textpad import rectangle
from email.mime import image
import cv2
from datetime import datetime
import numpy as np
import os
import ctypes
import time
import asyncio
from firebase_admin import credentials, initialize_app, storage
import firebase_admin
from firebase_admin import firestore


cred = credentials.Certificate("***CRED***")#firebase credentials.json dosyası
initialize_app(cred, {'storageBucket': '***firebase-storage-link***'},)#veritabanı linki


cap = cv2.VideoCapture(0)  # ip webcam, ip
face_cascade = cv2.CascadeClassifier("frontalface.xml")#ön yüz tanıma dosyası
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


async def dbKaydet():#veritabanına tespit edilen yüzü kaydeder.
    cv2.imwrite(dt_string+"test.png", img)
    fileName = "test.png"
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename("test.png")
    print("Veritabanına kaydedildi")
    print(blob.public_url)
    time.sleep(10)

while cap.isOpened():
    _, img = cap.read()
    cv2.waitKey(200)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    cv2.imshow("Kamera", img)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
        cv2.imshow("Kamera", img)
        
    if cv2.rectangle:
        asyncio.run(dbKaydet())
              
    else:
        print("Yüz Tanınmadı!")
                
            

    if cv2.waitKey(1) == ord("q"):
        break
