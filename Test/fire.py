# Import required libaries
import cv2
import numpy as np
import tensorflow.lite as tflite
from BeepSound import beepsound

# Load the TensorFlow Lite model.
interpreter = tflite.Interpreter(model_path=r"C:\Users\alexk\Documents\Test\Model\fire_model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Initialize the OpenCV video capture object.
cap = cv2.VideoCapture(0)

# Initialize a counter for fire detections.
fire_counter = 0

while True:
    # Capture a frame from the video feed.
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the video frame.
    resized_frame = cv2.resize(frame, (224, 224))
    normalized_frame = resized_frame.astype("float32") / 255.0
    input_data = np.expand_dims(normalized_frame, axis=0)

    # Run inference on the model.
    interpreter.set_tensor(input_details[0]["index"], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]["index"])
    prediction = output_data[0][0]
    # Draw bounding box and label on the frame if fire is detected.
    if prediction < 0.5:
        print('Fire Detected!!!!')
        label = "Fire detected!!!!"
        cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Get the coordinates of the bounding box.
        h, w, _ = frame.shape
        xmin, ymin, xmax, ymax = 0, 0, w, h

        # Draw the bounding box on the frame.
        thickness = 3
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 0, 255), thickness)

        # Increment the fire counter.
        fire_counter += 1

        # Check if fire has been detected 10 times.
        if fire_counter >= 10:
            # Sound the beep sound.
            beepsound()

            # Reset the fire counter.
            fire_counter = 0

    else:
        # print('No fire present')
        label = "No fire"
        cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Get the coordinates of the bounding box.
        h, w, _ = frame.shape
        xmin, ymin, xmax, ymax = 0, 0, w, h

        # Draw the bounding box on the frame.
        thickness = 3
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), thickness)

    # Display the frame with the bounding box and label.
    cv2.imshow("Fire detection", frame)

    # Exit the program if the 'q' key is pressed.
    if cv2.waitKey(1) == ord("q"):
        break

# Release the video capture object and close the display window.
cap.release()
cv2.destroyAllWindows()