from celery import shared_task
import os

@shared_task
def mock_otp_verification(phone_number, otp):
    desktop_path = os.path.join(os.environ['HOMEPATH'], 'Desktop')# Получаем путь к рабочему столу на Windows
    file_path = os.path.join(desktop_path, 'otp_logs.txt')  # Создаем путь к файлу "otp_logs.txt" на рабочем столе

    with open(file_path, "a") as file:
        file.write(f"Phone Number: {phone_number}, OTP: {otp}\n")

    print(f"OTP verification successful for phone number: {phone_number}")

    return True