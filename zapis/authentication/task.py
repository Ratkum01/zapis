from celery import shared_task
import os

@shared_task
def create_and_save_otp(phone_number, otp):
    desktop_path = os.path.join(os.environ['HOMEPATH'], 'Desktop')  # Получаем путь к рабочему столу на Windows
    file_path = os.path.join(desktop_path, 'otp_logs.txt')  # Создаем путь к файлу "otp_logs.txt" на рабочем столе

    with open(file_path, "a") as file:
        file.write(f"Phone Number: {phone_number}, OTP: {otp}\n")
    print(f"OTP created and saved for phone number: {phone_number}")
    return True

@shared_task
def verify_otp(phone_number, provided_otp):
    # Здесь может быть логика для проверки OTP
    # В данном примере мы просто печатаем сообщение об успешной проверке
    print(f"OTP verification successful for phone number: {phone_number} with OTP: {provided_otp}")
    return True
