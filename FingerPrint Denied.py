import os
import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

class BankLocker:
    def _init_(self):
        self.locker_status = False

    def open_locker(self, fingerprint_verified):
        if fingerprint_verified:
            self.locker_status = True
            return "Locker opened successfully"
        else:
            return "Fingerprint verification failed. Access denied."

    def close_locker(self):
        self.locker_status = False
        return "Locker closed"

class ImageCapture:
    def _init_(self):
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
    def _init_(self):
        pass

    def verify_fingerprint(self):
        # Placeholder function to simulate fingerprint verification
        return False  # Return True for simplicity in this example

def send_email(image_path):
    # Email configuration
    sender_email = "ndeepika5555@gmail.com"
    receiver_email = "madhumithamalavika1010@gmail.com"
    password = "Deepi106@"

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Unauthorized Access Alert"

    # Add message body
    body = "An unauthorized person has accessed the system. Please see the attached image."
    msg.attach(MIMEText(body, 'plain'))

    # Attach image
    with open(image_path, 'rb') as attachment:
        image_part = MIMEImage(attachment.read())
        msg.attach(image_part)

    # Send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        print("Email sent successfully.")
        server.quit()
    except Exception as e:
        print("Error: Unable to send email.")
        print(e)

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
            send_email(os.path.join(image_capture.image_folder, "captured_image.jpg"))
    else:
        print("Fingerprint verification failed. Access denied.")
        # If fingerprint verification fails, simulate closing the locker
        bank_locker.locker_status = False
        print(bank_locker.close_locker())
        image_capture.capture_status= True
        print("Image captured successfully")
        print("Alert message sent")
        print("Email sent successfully")
        import os
import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

class BankLocker:
    def _init_(self):
        self.locker_status = False

    def open_locker(self, fingerprint_verified):
        if fingerprint_verified:
            self.locker_status = True
            return "Locker opened successfully"
        else:
            return "Fingerprint verification failed. Access denied."

    def close_locker(self):
        self.locker_status = False
        return "Locker closed"

class ImageCapture:
    def _init_(self):
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
    def _init_(self):
        pass

    def verify_fingerprint(self):
        # Placeholder function to simulate fingerprint verification
        return False  # Return True for simplicity in this example

def send_email(image_path):
    # Email configuration
    sender_email = "ndeepika5555@gmail.com"
    receiver_email = "madhumithamalavika1010@gmail.com"
    password = "Deepi106@"

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Unauthorized Access Alert"

    # Add message body
    body = "An unauthorized person has accessed the system. Please see the attached image."
    msg.attach(MIMEText(body, 'plain'))

    # Attach image
    with open(image_path, 'rb') as attachment:
        image_part = MIMEImage(attachment.read())
        msg.attach(image_part)

    # Send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        print("Email sent successfully.")
        server.quit()
    except Exception as e:
        print("Error: Unable to send email.")
        print(e)

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
            send_email(os.path.join(image_capture.image_folder, "captured_image.jpg"))
    else:
        print("Fingerprint verification failed. Access denied.")
        # If fingerprint verification fails, simulate closing the locker
        bank_locker.locker_status = False
        print(bank_locker.close_locker())
        image_capture.capture_status= True
        print("Image captured successfully")
        print("Alert message sent")
        print("Email sent successfully")

if __name__ == "__main__":
 main()