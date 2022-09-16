from random import shuffle, choice

from django.conf import settings
from django.core.mail import send_mail


def get_code() -> str:
    a = list("12345678901234567890")
    shuffle(a)
    a = "".join(a)
    return "".join(choice(a) for _ in range(6))


def send_code(email: str) -> str:
    code: str = get_code()
    subject = "Tasdiqlash kodi"
    message = "Assalomu Alaykum Hurmatli foydalanuvchi!!!\n" \
              f"Tasdiqlash uchun kod: {code}\n\n" \
              f"Kodni hech kimga bermang, hattoki men bo'lsam ham!!!"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, recipient_list=recipient_list, from_email=from_email)
    return code
