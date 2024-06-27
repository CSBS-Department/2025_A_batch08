import os
import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

class BankLocker:
    def __init__(self):
        self.locker_status = False

    def open_locker(self, fingerprint_verified):
        if fingerprint_verified:
            self.locker_status = True
            return "Locker opened successfully"
        else:
            return "Fingerprint verification failed. Access denied."

    def close_locker(self):
        self.locker_status = False
        return "Locker opened successfully"

class ImageCapture:
    def __init__(self):
        self.image_folder = "captured_images"

        # Create a folder for captured images if it doesn't exist
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)

    def capture_image(self):
        # Open the default camera (usually the first webcam connected)
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Unable to open camera.")
            return None

        # Read a frame from the camera
        ret, frame = cap.read()

        if ret:
            # Save the captured image
            cv2.imwrite(os.path.join(self.image_folder, "captured_image.jpg"), frame)
            print("Image captured successfully.")
        else:
            print("Error: Unable to capture image.")

        # Release the camera
        cap.release()
        cv2.destroyAllWindows()

class FingerprintSensor:
    def __init__(self):
        pass

    def verify_fingerprint(self):
        # Placeholder function to simulate fingerprint verification
        return False  # Return True for simplicity in this example


def main():
    bank_locker = BankLocker()
    image_capture = ImageCapture()
    fingerprint_sensor = FingerprintSensor()

    # Simulate fingerprint verification
    fingerprint_verified = fingerprint_sensor.verify_fingerprint()

    if fingerprint_verified:
        print("Fingerprint verified. Access granted.")
        print(bank_locker.open_locker(fingerprint_verified))
        
        # Capture an image if the locker is opened successfully
        if bank_locker.locker_status:
            image_capture.capture_image()
            image_folder = "/path/to/image/folder" 
            image_path = os.path.join(image_folder, "captured_image.jpg")
    else:
        print("Fingerprint verified. Access granted.")

        # If fingerprint verification fails, simulate closing the locker
        bank_locker.locker_status = False
        print(bank_locker.close_locker())
        image_capture.capture_status= True
        print("Image captured successfully")

if __name__ == "__main__":
    main()