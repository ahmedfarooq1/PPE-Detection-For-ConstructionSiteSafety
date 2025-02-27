from ultralytics import YOLO
import cvzone
import cv2

# DEFINING VIDEO SOURCE | Use your own video by providing its absolute path on the disk. (e.g.
# C:/users/user-name/videos/your-file-name.mp4)
path = "recording-2.mp4"

# Creating a video capture from opencv based on the path provided.
video = cv2.VideoCapture(path)

# Getting Frame width and height.
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Creating YOLO MODEL.
model = YOLO(
    "../Weights/TBMConstructionSafety.pt")  # Trained By Me; ConstructionSafety Model (Based on YOLO version 8 - Nano)

# Classnames used in the model training.
classnames = ['Excavator', 'Gloves', 'Construction-Hat', 'Ladder', 'Mask', 'NO-Construction-Hat', 'NO-Mask',
              'NO-Safety-Vest', 'Person', 'SUV', 'Safety-Cone', 'Safety-Vest', 'bus', 'Dump-Truck', 'Fire-Hydrant',
              'Machinery', 'mini-van', 'sedan', 'semi', 'trailer', 'truck and trailer', 'truck', 'van', 'vehicle',
              'wheel loader']

# Defining color variables based on BGR format(Blue, Green, Red).
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# Looping through the video and getting the detection started.
while True:
    success, img = video.read()
    results = model(img, stream=True)  # Creating results to display the video.

    for i in results:
        boxes = i.boxes
        for box in boxes:
            # Creating bounding box and setting up axes of image.
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Calculating width and height from subtracting the width and height.
            width, height = x2 - x1, y2 - y1

            bbox = x1, y1, width, height

            cv2.putText(img, "CONSTRUCTION SAFETY DETECTION", org=(50, 50), fontFace=cv2.FONT_HERSHEY_PLAIN,
                        fontScale=3, color=black, thickness=2)

            # Calculating confidence level.
            confidence = round(box.conf[0].item(), 2)

            # Below variable holds the class ID number. (e.g. 1.00)
            clsId = box.cls[0]
            '''box.cls = cls (torch.Tensor) or (numpy.ndarray): The class values of the boxes.'''

            clsId = int(clsId)

            # Variable for holding the detected class name.
            detectedClass = classnames[clsId]

            # Putting condition | The confidence must be high so the detections don't overlap
            if confidence > 0.6:
                # Putting condition | If the detected class is violating the safety protocol.
                if detectedClass in ['NO-Construction-Hat', 'NO-Mask', 'NO-Safety-Vest']:

                    # Creating the corner rectangle from cvzone library.
                    cvzone.cornerRect(img, bbox, colorC=red, colorR=red, t=3)

                    # Putting text over the rectangle.
                    cvzone.putTextRect(img, f'{confidence} {classnames[clsId]}', (max(0, x1), max(20, y1)), scale=0.9,
                                       thickness=1, font=cv2.FONT_HERSHEY_PLAIN, offset=5, colorR=red)

                    cv2.putText(img, "Attention!",
                                (frame_width - 250, frame_height - 50), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2.5,
                                color=red, thickness=3)

                # Putting condition | If the detected class is of a person.
                elif detectedClass == 'Person':

                    # Creating the corner rectangle from cvzone library.
                    cvzone.cornerRect(img, bbox, colorC=blue, colorR=blue, t=3)

                    # Putting text over the rectangle.
                    cvzone.putTextRect(img, f'{confidence} {classnames[clsId]}', (max(0, x1), max(20, y1)), scale=0.9,
                                       thickness=1, font=cv2.FONT_HERSHEY_PLAIN, offset=5, colorR=blue)

                else:
                    # Creating the corner rectangle from cvzone library.
                    cvzone.cornerRect(img, bbox, colorC=green, colorR=green, t=3)

                    # Putting text over the rectangle.
                    cvzone.putTextRect(img, f'{confidence} {classnames[clsId]}', (max(0, x1), max(20, y1)), scale=0.9,
                                       thickness=1, font=cv2.FONT_HERSHEY_PLAIN, offset=5, colorR=green, colorT=black)

    cv2.imshow("Construction Safety Monitor", img)
    cv2.waitKey(1)
