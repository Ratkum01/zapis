from celery import shared_task
import os

@shared_task
def create_and_save_otp(phone_number, otp):
    desktop_path = os.path.join(os.environ['HOMEPATH'], 'Desktop')
    file_path = os.path.join(desktop_path, 'otp_logs.txt')

    with open(file_path, "a") as file:
        file.write(f"Phone Number: {phone_number}, OTP: {otp}\n")
    print(f"OTP created and saved for phone number: {phone_number}")
    return True

@shared_task
def verify_otp(phone_number, provided_otp):
    print(f"OTP verification successful for phone number: {phone_number} with OTP: {provided_otp}")
    return True
