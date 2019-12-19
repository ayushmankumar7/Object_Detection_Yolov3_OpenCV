import numpy as np 
import cv2


def yolo_loader():
    net = cv2.dnn.readNet("yolov3.weights", "cfg/yolov3.cfg")
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layers_name = net.getLayerNames()
    outputlayers = [layers_name[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    
    return net, classes, outputlayers