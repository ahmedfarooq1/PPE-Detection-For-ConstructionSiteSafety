# PPE-Detection-For-Construction-Site-Safety
🚧 Project Overview 🚧

The Construction Safety Monitoring System is an advanced AI-powered solution designed to enhance safety protocols on construction sites. By leveraging computer vision and the YOLO (You Only Look Once) model, this system monitors and detects safety compliance in real-time, ensuring a safer working environment.

Key Features
📹 Real-Time Video Analysis: Utilizes OpenCV for capturing and processing live video streams.

🤖 YOLOv8 Model: Custom-trained model to recognize various safety equipment and potential safety violations.

🚨 Safety Alerts: Identifies and alerts on the absence of essential safety gear like construction hats, masks, and safety vests.

🖼️ Visual Annotations: Provides visual cues and text annotations to highlight detected objects and their confidence levels.

🎨 Dynamic Bounding Boxes: Uses cvzone to draw attention to detected objects, with different colors indicating safety compliance or violations.

Technical Details:

Model and Training
Model: YOLOv8 (You Only Look Once, version 8)

Training Data: Custom dataset including classes such as Excavator, Gloves, Construction-Hat, Ladder, Mask, NO-Construction-Hat, NO-Mask, NO-Safety-Vest, Person, and various vehicles.

Class Names:

['Excavator', 'Gloves', 'Construction-Hat', 'Ladder', 'Mask', 'NO-Construction-Hat', 'NO-Mask', 'NO-Safety-Vest', 'Person', 'SUV', 'Safety-Cone', 'Safety-Vest', 'Bus', 'Dump-Truck', 'Fire-Hydrant', 'Machinery', 'Mini-van', 'Sedan', 'Semi', 'Trailer', 'Truck and Trailer', 'Truck', 'Van', 'Vehicle', 'Wheel Loader']

Tools and Libraries:

YOLO: ultralytics

OpenCV: Open Source Computer Vision Library

cvzone: A high-level OpenCV library for easier computer vision application development
