import cv2

videoCapture = cv2.VideoCapture()
videoCapture.open('test4')

fps = videoCapture.get(cv2.CAP_PROP_FPS)
frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)

print("fps=",fps,"frames=",frames)

for i in range(int(frames)):
    ret,frame = videoCapture.read()
    cv2.imwrite("videoframe/test4(%d).jpg"%i,frame)