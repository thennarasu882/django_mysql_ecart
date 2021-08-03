from django.db.models import query
from django.shortcuts import render
from .models import orders_data


def index(request):
    all_dataobj = orders_data.objects.all()
    return render(request, "index.html", {"data": all_dataobj})
