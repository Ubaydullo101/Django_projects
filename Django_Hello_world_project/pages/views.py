from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

#Function based view
def home_page_view(request):
    return render(request, 'home.html')

#Class based view
class Home_Page_View(TemplateView):
    template_name = 'home.html'