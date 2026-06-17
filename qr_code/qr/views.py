import qrcode
import os

from django.shortcuts import render
from django.conf import settings

def home(request):
    qr_code_url = None

    if request.method == "POST":
        data = request.POST.get("data")

        qr = qrcode.make(data)

        filename = "qr_code.png"

        folder = os.path.join(settings.MEDIA_ROOT, "qr_codes")
        os.makedirs(folder, exist_ok=True)

        filepath = os.path.join(folder, filename)

        qr.save(filepath)

        qr_code_url = settings.MEDIA_URL + "qr_codes/" + filename

    return render(request, "index.html", {
    "qr_code_url": qr_code_url,
    "data": request.POST.get("data", "")
})