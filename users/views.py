from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    template_name = 'users/logout.html'

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import Profile

class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile