from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Member, Trainer, MembershipPlan
from .serializers import MemberSerializer, TrainerSerializer, MembershipPlanSerializer
from .forms import MemberForm


# REST API
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('-join_date')
    serializer_class = MemberSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class MembershipPlanViewSet(viewsets.ModelViewSet):
    queryset = MembershipPlan.objects.all()
    serializer_class = MembershipPlanSerializer


# HTML pages
def home(request):
    context = {
        "member_count": Member.objects.count(),
        "active_member_count": Member.objects.filter(active=True).count(),
        "trainer_count": Trainer.objects.count(),
        "recent_members": Member.objects.order_by('-join_date')[:5],
        "trainers": Trainer.objects.all()[:5],
    }
    return render(request, "members/home.html", context)


def member_list(request):
    members = Member.objects.all()
    return render(request, "members/member_list.html", {"members": members})


def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, "members/member_detail.html", {"member": member})


def member_create(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("member-list")
    else:
        form = MemberForm()
    return render(request, "members/member_form.html", {"form": form})


def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect("member-list")
    else:
        form = MemberForm(instance=member)
    return render(request, "members/member_form.html", {"form": form})


def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        member.delete()
        return redirect("member-list")
    return render(request, "members/member_confirm_delete.html", {"member": member})
