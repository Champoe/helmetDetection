import cv2
from ultralytics import YOLO

model = YOLO("best-newv4.pt")
class_names = ["With Helmet", "Without Helmet"]
confidence_threshold = 0.55

video_path = r"C:\Users\Admin\Downloads\helmetDetection\video\video_0.mp4"
webcam = cv2.VideoCapture(video_path)

user_screen_width = 1280
user_screen_height = 720

while True:
    ret, frame = webcam.read()
    if not ret:
        break

    frame = cv2.resize(frame, (user_screen_width, user_screen_height))

    helmet_detected = False

    results = model.predict(frame, conf=confidence_threshold)

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls.item())
            confidence = box.conf.item()

            if 0 <= class_id < len(class_names):
                if class_names[class_id] == "With Helmet":
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{'Helmet Detected'}: {confidence:.2f}",
                                (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 255, 0), 2)
                    helmet_detected = True

    if not helmet_detected:
        cv2.putText(frame, "No Helmet Detected", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Helmet Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()
