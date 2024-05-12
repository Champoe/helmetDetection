import cv2
import tkinter as tk
from ultralytics import YOLO
import threading

model = YOLO("best-newv4.pt")
class_names = ["With Helmet", "Without Helmet"]
confidence_threshold = 0.57
webcam = cv2.VideoCapture(0)
detection_running = False

def start_detection():
    global webcam, detection_running
    detection_running = True
    while detection_running:
        ret, frame = webcam.read()
        if not ret:
            break

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
                        cv2.putText(frame, f"{class_names[class_id]}: {confidence:.2f}",
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

def stop_detection():
    global detection_running
    detection_running = False

root = tk.Tk()
root.title("Helmet Detection")

window_width = 400
window_height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

frame = tk.Frame(root)
frame.pack(pady=20)

start_button = tk.Button(frame, text="Start Detection", command=lambda: threading.Thread(target=start_detection).start(), width=15, height=2)
start_button.grid(row=0, column=0, padx=10)

stop_button = tk.Button(frame, text="Stop Detection", command=stop_detection, width=15, height=2)
stop_button.grid(row=0, column=1, padx=10)

quit_button = tk.Button(frame, text="Quit", command=root.quit, width=15, height=2)
quit_button.grid(row=0, column=2, padx=10)

root.mainloop()