from django.shortcuts import render
from .models import Yazi
import random

def yazi(request):
    yazilar = Yazi.objects.order_by("?").first()
    return render(request, 'yazilar/yazi.html', {'yazilar': yazilar})
# Create your views here.
