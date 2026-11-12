from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RequestForm
from .models import Request


@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.author = request.user
            new_request.save()
            return redirect('request_submitted', pk=new_request.pk)
    else:
        initial = {}
        if request.user.is_authenticated:
            initial = {
                'name': request.user.full_name or request.user.get_full_name() or request.user.username,
                'email': request.user.email,
            }
        form = RequestForm(initial=initial)
    return render(request, 'requests/request_form.html', {'form': form})


@login_required
def request_submitted(request, pk):
    ticket = get_object_or_404(Request, pk=pk, author=request.user)
    return render(request, 'requests/request_submitted.html', {'ticket': ticket})


@login_required
def my_requests(request):
    tickets = Request.objects.filter(author=request.user)
    return render(request, 'requests/request_list.html', {'tickets': tickets})


@login_required
def request_detail(request, pk):
    ticket = get_object_or_404(Request, pk=pk, author=request.user)
    return render(request, 'requests/request_detail.html', {'ticket': ticket})
