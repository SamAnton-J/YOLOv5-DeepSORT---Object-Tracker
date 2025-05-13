import random
import torch

class Tracker:
    def __init__(self):
        self.id_counter = 0
        self.objects = {}
        self.trails = {}
        self.id_frame_counts = {}
        self.entry_frames = {}
        self.exit_frames = {}
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    def detect(self, frame):
        results = self.model(frame)
        detections = []
        for *box, conf, cls in results.xyxy[0].tolist():
            x1, y1, x2, y2 = map(int, box)
            w, h = x2 - x1, y2 - y1
            detections.append([x1, y1, w, h])
        return detections

    def update(self, detections, frame_count):
        results = []
        for det in detections:
            self.id_counter += 1
            obj_id = self.id_counter
            x, y, w, h = det
            cx, cy = x + w // 2, y + h // 2
            self.objects[obj_id] = (x, y, w, h)
            if obj_id not in self.trails:
                self.trails[obj_id] = []
            self.trails[obj_id].append((cx, cy))
            self.id_frame_counts[obj_id] = 1
            self.entry_frames[obj_id] = frame_count
            results.append((obj_id, x, y, w, h))
        return results

    def update_times(self, tracked_objects, frame_count):
        for obj in tracked_objects:
            obj_id = obj[0]
            if obj_id in self.id_frame_counts:
                self.id_frame_counts[obj_id] += 1
            self.exit_frames[obj_id] = frame_count
