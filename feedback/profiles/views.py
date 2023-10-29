from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views import View
from .forms import ProfileForm
from .models import UserProfile

# Create your views here.

class CreateProfileView(CreateView):
    model = UserProfile
    fields = "__all__"
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         context = {"form": form}
#         return render(request, "profiles/create_profile.html", context)

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
        
#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
        
#         context = {"form": submitted_form}
        
#         return HttpResponseRedirect("profiles/create_profile.html", context)
        