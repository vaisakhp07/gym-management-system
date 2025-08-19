from django.shortcuts import render, get_object_or_404
from .models import Trainer

def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, "trainers/trainer_list.html", {"trainers": trainers})

def trainer_detail(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    return render(request, "trainers/trainer_detail.html", {"trainer": trainer})
