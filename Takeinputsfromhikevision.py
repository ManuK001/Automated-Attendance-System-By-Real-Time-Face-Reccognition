#Need to enable RTSP in HikeVision camera setting - Ask Camera man

import cv2
import time

RTSP_URL = "rtsp://username:password@192.168.1.64:554/Streaming/Channels/102"

while True:
    cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

    if not cap.isOpened():
        print("Retrying connection...")
        time.sleep(3)
        continue

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Stream lost. Reconnecting...")
            break

        frame = cv2.resize(frame, (640, 480))
        cv2.imshow("Hikvision Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit(0)

    cap.release()
    time.sleep(2)
