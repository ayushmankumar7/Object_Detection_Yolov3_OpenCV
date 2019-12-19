import numpy as np 
import cv2 

#Load YOLO 

net = cv2.dnn.readNet("yolov3.weights", "cfg/yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layers_name = net.getLayerNames()
outputlayers = [layers_name[i[0] - 1] for i in net.getUnconnectedOutLayers()]

#''''''''''''''''''''''''''''''''''''
#That's all we need to load our Algorithm

#Loading Image
cap = cv2.VideoCapture()

while(1):
    ret, img = cap.read()
    img = cv2.resize(img, None, fx =  0.4, fy = 0.4)

    # We cannot send this image into our algorithm
    #We need to create a blob
    height, width, channels = img.shape
    blob = cv2.dnn.blobFromImage(img,0.00392,(416,416),(0,0,0), True, crop = False)

    '''for b in blob:
        for n ,img_blob in enumerate(b):
            cv2.imshow(str(n), img_blob)
            '''

    net.setInput(blob)
    outs = net.forward(outputlayers)

    #showing Information on the screen

    boxes = []
    confidences = []
    class_ids = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:

                #object detected

                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3]* height)

                #cv2.circle(img, (center_x, center_y), 10, (0,255,0), 2)
                #Rectangle Coordinate

                x=int(center_x - w / 2)
                y = int(center_y-h /2)

                #cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
                boxes.append([x,y,w,h])
                confidences.append(float(confidence))
                class_ids.append(class_id)


    objects_detected = len(boxes)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        x,y,w,h = boxes[i]
        label = str(classes[class_ids[i]])
        print(label)

        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(img, label, (x,y+30), font,1, (0,0,255), 2)



    cv2.imshow('Image', img)
    if cv2.waitKey(25) == 27:
        break

cap.release()
cv2.destroyAllWindows()