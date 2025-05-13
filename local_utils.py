import cv2
import random

def draw_boxes(frame, tracked_objects):
    for obj in tracked_objects:
        obj_id, x, y, w, h = obj
        color = get_color(obj_id)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, f"ID {obj_id}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return frame

def draw_trails(frame, trails):
    for object_id, points in trails.items():
        color = get_color(object_id)
        for i in range(1, len(points)):
            if points[i - 1] is None or points[i] is None:
                continue
            cv2.line(frame, points[i - 1], points[i], color, 2)
    return frame

def calculate_times(entry_frames, exit_frames, frame_rate):
    times = {}
    for obj_id in entry_frames:
        if obj_id in exit_frames:
            time_in_view = (exit_frames[obj_id] - entry_frames[obj_id]) / frame_rate
            times[obj_id] = time_in_view
    return times

def get_color(object_id):
    random.seed(object_id)
    return tuple(random.randint(0, 255) for _ in range(3))
