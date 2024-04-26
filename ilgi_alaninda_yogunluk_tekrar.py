import cv2 
from ultralytics import YOLO 
import imutils 
import numpy as np
import random
from collections import defaultdict
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-m","--model",required=True,help = "Path to YOLO model file (.onnx or .pt)")
ap.add_argument("-s","--source", default = 0, help = "Path to input video file")
ap.add_argument("-r1","--region1", nargs = "+", type = int, default=[750, 40, 1250, 420], help="Coordinates of region 1 (x1 y1 x2 y2)")
ap.add_argument("-r2","--region2", nargs = "+", type = int, default=[300, 40, 700, 420], help="Coordinates of region 2 (x1 y1 x2 y2)")
args = vars(ap.parse_args())

# Loading YOLO model
model = YOLO(args["model"])

# Opening video capture
if args["source"] == "0":
    video_path = 0  # Webcam
else:
    video_path = args["source"]

cap = cv2.VideoCapture(video_path)

thickness = 1
font = cv2.FONT_HERSHEY_PLAIN
font_scale = 0.7

track_history = defaultdict(lambda: [])

region1 = args["region1"]
region2 = args["region2"]

