import torch
import numpy as np
import cv2
from time import time
from ultralytics import YOLO

class ObjectDetections:
  def __init__(self,capture_index):
    self.capture_index = capture_index
    self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print("Using Device: ", self.device)
    self.model = self.load_model()
  
  def load_model(self):
    model = YOLO("yolov8n.pt")
    model.fuse()
    return model

  def predict(self,frame):
    results = self.model(frame)
    return results
  
  def plot_bboxes(self, results, frame):
    xyxys = []
    confidences = []
    class_ids = []
    for r in results:
      boxes = r.boxes.cpu().numpy()
      print(boxes)
    return frame
  
  def __call__(self):
    cap = cv2.VideoCapture(self.capture_index)
    assert cap.isOpened()


