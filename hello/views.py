from django.http import HttpResponse
import re #regex
from datetime import datetime
from django.shortcuts import render,redirect
from hello.forms import LogMessageForm
from django.views.generic import ListView
from hello.models import LogMessage

def log_message(request):
    form = LogMessageForm(request.POST or None)
    
    if request.method == "POST" :
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form}) 
# Create your views here.
class HomeListView(ListView):
    """Renders the home page, with a list of all the messages"""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context
# def home(request):
#     return render(request, 'hello/home.html')

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def about(request):
    return render(request, 'hello/about.html')

def contact(request):
    return render(request, 'hello/contact.html')
    # now = datetime.now()
    # formatter_now = now.strftime("%A, %d %B, %Y at %X")

    # match_object = re.match("[a-zA-Z]+", name)

    # if(match_object):
    #     clean_name = match_object.group(0)
    # else:
    #     clean_name = "Friend"
    # content = "Hello There hecswkdjfb, " + clean_name + "! It's " + formatter_now
    # return HttpResponse(content)