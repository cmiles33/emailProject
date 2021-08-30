from django.shortcuts import render, get_object_or_404
from .models import Program

# Create your views here.



def list_programs(request):
    programs = Program.objects.filter(active=True)
    return render(request,
                  'reTranslation/list.html',
                  {'programs':programs})

def program_detail(request, user, programname):
    program = get_object_or_404(Program,
                                member=user,
                                programName=programname)
