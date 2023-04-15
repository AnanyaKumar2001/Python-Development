from django.shortcuts import redirect, render, get_object_or_404

from .form import MeetingForm

# Create your views here.

from .models import Meeting, Room


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)

    return render(request, 'meetings/detail.html', {"meeting": meeting})


def rooms_list(request):
    return render(request, 'meetings/rooms_list.html', {"rooms": Room.objects.all()})


def form(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('welcome')

    else:
        form = MeetingForm()

    return render(request, 'meetings/form.html', {"form": form})
