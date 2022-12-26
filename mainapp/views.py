from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse('Done')

def sendmail_toall(request):
    send_mail_func.delay()  
    return HttpResponse("Sent")