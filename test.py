import cv2
face_cascade = cv2.CascadeClassifier('/root/Downloads/project/haarcascade_frontalface_alt.xml')
img = cv2.imread('2.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print (len(faces))
