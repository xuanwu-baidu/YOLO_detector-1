import cv2

video_capture = cv.VideoCapture("sample.mp4")

fps = video_capture.get(cv2.CAP_PROP_FPS)
frames = video_capture.get(cv2.CAP_PROP_FRAME_COUNT)

print("fps=",fps,"frames=",frames)

for i in range(int(frames)):
    ret,frame = video_capture.read()
    cv2.imwrite("test/videoframe/test4(%d).jpg"%i,frame)
    print(i)