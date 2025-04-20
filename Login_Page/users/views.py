from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('sus')
        else:
            messages.warning(request, 'Please correct the error(s) below.')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})



def sus(request):
    return render(request, 'users/sus.html')