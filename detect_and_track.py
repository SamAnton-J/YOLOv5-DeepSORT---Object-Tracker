import cv2
from tracker import Tracker
from local_utils import draw_boxes, draw_trails, calculate_times
import os

cap = cv2.VideoCapture('input.mp4')
tracker = Tracker()
frame_rate = cap.get(cv2.CAP_PROP_FPS)
frame_count = 0

fourcc = cv2.VideoWriter_fourcc(*'XVID')
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
os.makedirs('outputs', exist_ok=True)
out = cv2.VideoWriter('outputs/output.mp4', fourcc, frame_rate, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("No more frames to read.")
        break

    detections = tracker.detect(frame)
    tracked_objects = tracker.update(detections, frame_count)
    tracker.update_times(tracked_objects, frame_count)

    frame = draw_boxes(frame, tracked_objects)
    frame = draw_trails(frame, tracker.trails)

    print("Writing frame to output video...")
    out.write(frame)
    frame_count += 1

cap.release()
out.release()

times = calculate_times(tracker.entry_frames, tracker.exit_frames, frame_rate)
print(f"Total unique IDs detected: {len(times)}")
for object_id, t in times.items():
    print(f"Object ID {object_id} spent {t:.2f} seconds in view.")

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Tracking Results</title>
</head>
<body>
    <h1>Object Tracking Results</h1>
    <p>Total unique IDs detected: {len(times)}</p>
    <ul>
        {"".join([f"<li>Object ID {object_id}: {t:.2f} seconds in view</li>" for object_id, t in times.items()])}
    </ul>
    <video controls width="640" height="480">
        <source src="outputs/output.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</body>
</html>
"""

with open("result.html", "w") as f:
    f.write(html_content)