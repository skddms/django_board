from django.shortcuts import render, redirect
from .models import *
from .forms import BoardForm

def list(request):
    boards = Board.objects.all()
    return render(request, 'board/list.html', {'boards': boards})

def create(request):
    if request.method=='POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/board/list')
    else:
        form = BoardForm()

    return render(request, 'board/write.html', {'form': form})

def edit(request, id):
    board_id = Board.objects.get(id=id)
    if request.method=='POST':
        form = BoardForm(request.POST, instance=board_id)
        if form.is_valid():
            form.save()
        return redirect('/board/list')
    else:
        form = BoardForm(instance=board_id)

    return render(request, 'board/write.html', {'form': form})
