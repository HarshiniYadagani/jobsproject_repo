from django.shortcuts import render

# Create your views here.
def homepage_view(request):
    return render(request,'firstapp/index.html')

from firstapp.models import Hydjobs
def hydjobs_view(request):
    jobs_list=Hydjobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'firstapp/hydjobs.html',my_dict)

from firstapp.models import Banglorejobs
def blrjobs_view(request):
    jobs_list=Banglorejobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'firstapp/blrjobs.html',my_dict)

from firstapp.models import Punejobs
def punejobs_view(request):
    jobs_list=Punejobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'firstapp/punejobs.html',my_dict)
