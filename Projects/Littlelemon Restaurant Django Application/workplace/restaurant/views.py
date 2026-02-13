from django.shortcuts import render, get_object_or_404
from .models import Menu
from .forms import BookingForm


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'book.html', {'form': form})


def menu(request):
    menu_data = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menu_data})


def display_menu_item(request, pk):
    menu_item = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu_item.html', {'menu_item': menu_item})
