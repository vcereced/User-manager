from django.shortcuts import render, redirect, get_object_or_404
from .forms import DefaultForm
from .models import Default

def index(request):
    return render(request, 'playerApp/index.html')

def add_default(request):
    if request.method == 'POST':
        form = DefaultForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ok')
    else:
        form = DefaultForm()
    
    return render(request, 'playerApp/add_default.html', {'form':form})

def ok(request):
    return render(request, 'playerApp/ok.html')

def displayer(request, item_id):
    item = get_object_or_404(Default, id=item_id)
    total_items = Default.objects.count()

     # Identificar el anterior y siguiente
    next_item = Default.objects.filter(id__gt=item.id).order_by('id').first()
    before_item = Default.objects.filter(id__lt=item.id).order_by('-id').first()
    context = {
        'item': item,
        'next_item': next_item,
        'before_item': before_item,
        'total_items': total_items
    }

    return render(request, 'playerApp/displayer.html', context)

