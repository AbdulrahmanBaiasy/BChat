from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import addRoomForm
from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})


@login_required
def room_add (request): 
    if request.method == "POST":
        form = addRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms')
        else : 
            print (form.errors)

    else:
        form = addRoomForm()
    return render(request, 'room/room_add.html', {'form': form})