from uuid import uuid4

from django.shortcuts import render

from app.models import UserConfirm
from app.utils import send_code


def home(request):
    if request.POST:
        email: str = request.POST.get('email')
        code: str = send_code(email=email)
        token = uuid4()
        user = UserConfirm(email=email, code=code, token=token)
        user.save()
        return render(request=request, template_name='code.html', context={"token": token})
    return render(request=request, template_name='index.html', context={})


def code_confirm(request):
    if request.POST:
        code: str = request.POST.get('code')
        token: str = request.COOKIES.get('token', "default")
        try:
            user = UserConfirm.objects.get(token=token, code=code.strip(), is_active=False)
        except UserConfirm.DoesNotExist:
            return render(request=request, template_name='code.html', context={"token": token, 'message': "Error"})
        user.is_active = True
        user.save()
        return render(request=request, template_name='code.html', context={"token": token, "message": "Success"})
