from django.shortcuts import render
from django.utils import timezone
from .models import Event, Merch
from django.shortcuts import render, get_object_or_404
from .forms import EventForm, MerchForm
from django.shortcuts import redirect

def event_list(request):
    # events = Event.objects.filter(date__lte=timezone.now()).order_by('date')
    events = Event.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'tour/event_list.html', {'events' : events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'tour/event_detail.html', {'event': event})

def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'tour/event_edit.html', {'form': form})

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'tour/event_edit.html', {'form': form})

def merch_menu(request):
    merch_all = Merch.objects.all()
    return render(request, 'tour/merch_menu.html', {'merch_all' : merch_all})

def merch_list(request):
    merch_all = Merch.objects.all()
    return render(request, 'tour/merch_list.html', {'merch_all' : merch_all})

def merch_sell(request):
    all_merch = Merch.objects.all()
    return render(request, 'tour/merch_sell.html', {'merch_all' : merch_all})

def merch_detail(request, pk):
    merch = get_object_or_404(Merch, pk=pk)
    return render(request, 'tour/merch_detail.html', {'merch' : merch})

def merch_new(request):
    if request.method == "POST":
        form = MerchForm(request.POST)
        if form.is_valid():
            merch = form.save(commit=False)
            merch.save()
            return redirect('merch_detail', pk=merch.pk)
    else:
        form = MerchForm()
    return render(request, 'tour/merch_edit.html', {'form' : form})
