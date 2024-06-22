import torch
import numpy as np
import cv2
from time import time
from ultralytics import YOLO


class ObjectDetections:
    def __init__(self, capture_index):
        self.capture_index = capture_index
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print("Using Device: ", self.device)
        self.model = self.load_model()

    def load_model(self):
        model = YOLO("yolov8n.pt")
        model.fuse()
        return model

    def predict(self, frame):
        results = self.model(frame)
        return results

    def plot_bboxes(self, results, frame):
        for result in results:
            boxes = result.boxes
            for box in boxes:
                xyxy = box.xyxy[0].cpu().numpy()
                x1, y1, x2, y2 = map(int, xyxy[:4])
                confidence = box.conf[0]
                class_id = int(box.cls[0])
                label = f"{self.model.names[class_id]} {confidence:.2f}"

                # Draw the bounding box and label on the frame
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        return frame

    def __call__(self):
        cap = cv2.VideoCapture(self.capture_index)
        assert cap.isOpened(), f"Error opening video stream or file: {self.capture_index}"

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            start_time = time()
            results = self.predict(frame)
            frame = self.plot_bboxes(results, frame)
            end_time = time()

            fps = 1 / (end_time - start_time)
            cv2.putText(frame, f"FPS: {fps:.2f}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow("YOLO Object Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_index = 0  # Change this to the appropriate index or file path
    detector = ObjectDetections(capture_index)
    detector()
