# Object Detection and Tracking System

## Project Overview

This project implements an object detection and tracking system using YOLOv5 for object detection and a custom tracker for maintaining object identities across video frames. The system processes an input video, detects objects in each frame, tracks their movements, and generates an output video with bounding boxes and trails. Additionally, it calculates the time each object spends in view and generates an HTML report summarizing the results.

## Key Features

### Object Detection
- Utilizes YOLOv5 (yolov5s model) for real-time object detection.
- Detects objects in each frame and provides bounding box coordinates.

### Object Tracking
- Assigns unique IDs to detected objects.
- Tracks objects across frames using a custom tracking algorithm.
- Maintains trails for visualizing object movement.

### Output Generation
- Creates an annotated video (`output.mp4`) with bounding boxes and trails.
- Calculates the time each object spends in view.
- Generates an HTML report (`result.html`) summarizing the tracking results and embedding the output video.

## System Architecture

### Input
- A video file (`input.mp4`) is provided as input.

### Processing Pipeline
1. **Detection**: YOLOv5 detects objects in each frame.
2. **Tracking**: A custom tracker assigns unique IDs to objects and tracks their movement across frames.
3. **Visualization**: Bounding boxes and trails are drawn on each frame.

### Output
- An annotated video (`outputs/output.mp4`) with bounding boxes and trails.
- An HTML report (`result.html`) summarizing the results.

## Implementation Details

### detect_and_track.py
- Handles video processing and integrates detection, tracking, and visualization.
- Writes the annotated frames to an output video.
- Generates an HTML report summarizing the tracking results.

### tracker.py
- Implements the `Tracker` class for object tracking.
- Uses YOLOv5 for object detection.
- Tracks object entry and exit times and maintains trails for visualization.

### local_utils.py
- Provides utility functions for drawing bounding boxes and trails.
- Calculates the time each object spends in view.

## Workflow

### Initialization
- Load the YOLOv5 model.
- Set up video input and output.

### Frame Processing
- Read each frame from the input video.
- Detect objects using YOLOv5.
- Track objects and update their positions and trails.
- Annotate the frame with bounding boxes and trails.

### Output Generation
- Write the annotated frames to the output video.
- Calculate object times in view.
- Generate an HTML report summarizing the results.

## Dependencies

The following Python libraries are required:

- `torch`: For YOLOv5 model inference.
- `opencv-python`: For video processing and visualization.
- `random`: For generating unique colors for object IDs.

Install the dependencies using:

```bash
pip install torch torchvision opencv-python
