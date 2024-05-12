import cv2
from ultralytics import YOLO
import os

model = YOLO("best-newv4.pt")
class_names = ["With Helmet", "Without Helmet"]
confidence_threshold = 0.7
folder_path = r"C:\Users\Admin\Downloads\helmetDetection\images"
resized_images = []

for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        image_path = os.path.join(folder_path, filename)
        frame = cv2.imread(image_path)
        resized_frame = cv2.resize(frame, (340, 340))
        helmet_detected = False
        results = model.predict(resized_frame, conf=confidence_threshold)
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls.item())
                confidence = box.conf.item()
                if 0 <= class_id < len(class_names):
                    if class_names[class_id] == "With Helmet":
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        cv2.rectangle(resized_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(resized_frame, f"{'Helmet Detected'}: {confidence:.2f}",
                                    (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (0, 255, 0), 2)
                        helmet_detected = True
        if not helmet_detected:
            cv2.putText(resized_frame, "No Helmet Detected", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        resized_images.append(resized_frame)

rows = 2
cols = (len(resized_images) + 1) // rows
collage = None

for i in range(rows):
    row_images = resized_images[i * cols: (i + 1) * cols]
    row_collage = cv2.hconcat(row_images)
    if collage is None:
        collage = row_collage
    else:
        collage = cv2.vconcat([collage, row_collage])

cv2.imshow("Helmet Detection Collage", collage)
cv2.waitKey(0)
cv2.destroyAllWindows()
