from django.shortcuts import render

from .forms import AddForm
from .models import Post,Category

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def createPost(request):
    form = AddForm(request.POST)
    post_category = Category.objects.all()
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            post_saved = form.save(commit=False)
            post_saved.author = request.user.id
            form.save()
    return render(request, 'add.html', {'form': form, 'post_category': post_category})