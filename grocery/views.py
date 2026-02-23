from django.shortcuts import render, redirect, get_object_or_404
from .models import GroceryItem

def index(request):
    items = GroceryItem.objects.all().order_by('-created_at')
    return render(request, 'grocery/index.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            GroceryItem.objects.create(name=name)
    return redirect('grocery:index')

def delete_item(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, id=item_id)
        item.delete()
    return redirect('grocery:index')
