from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from .models import Program, Reponse,Payload
from .forms import ResponseForm, LoginForm

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.utils import timezone

# Create your views here.

def user_login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated '\
                                        'Successfully')
                else:
                    return HttpResponse(' Disabled Account')
            else:
                return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    return render(request,'reTranslation/authentication/login.html',
                  {'form':form})


@login_required
def list_programs(request):
    member = request.user.username
    programs = Program.objects.filter(member__username=member,active=True)
    return render(request,
                  'reTranslation/list.html',
                  {'programs':programs})

@login_required
def program_detail(request, user, programname):
    if user != request.user.username:
        return redirect('retranslation:list_programs')

    program = get_object_or_404(Program,
                                member__username=user,
                                programName=programname)
    reponses = Reponse.objects.filter(program__member__username=user,
                                      program__programName=programname,
                                      finished=True)
    if reponses.count() >= 6:
        scrollAble= "pre-scrollable"
    else:
        scrollAble = ""
    unFinished = Reponse.objects.filter(program__member__username=user,
                                        program__programName=programname,
                                        finished=False)
    if unFinished.count() >= 6:
        finishScroll = "pre-scrollable"
    else:
        finishScroll = ""

    myTime = timezone.now()

    return render(request,
                  'reTranslation/detail.html',
                  {'program':program,
                   'reponses':reponses,
                   'unfinished':unFinished,
                   'scroll':scrollAble,
                   'finishscroll':finishScroll,
                   'currenttime':myTime})

@login_required
def response_detail(request, user, programname, payloadnumber):
    if user != request.user.username:
        return redirect('retranslation:list_programs')
    program = get_object_or_404(Program,
                                member__username=user,
                                programName=programname)
    payload = get_object_or_404(Payload,
                                programName=programname,
                                payloadnumber=payloadnumber)
    new_response = None
    # If we dont have a response yet, then a form needs to be displayed
    # so the user can make one.
    if request.method =='POST':
        response_form = ResponseForm(data=request.POST)
        if response_form.is_valid():
            # Get the text response information
            new_response = response_form.save(commit=False)
            # Get the program and payload objects
            #program.programCount += 1
            #program.save()
            response = Reponse.objects.get(program__member__username=user,
                                           program__programName=programname,
                                           payload__payloadnumber=payloadnumber)
            response.textresponse = new_response.textresponse
            response.program = program
            response.finished = True
            response.created = timezone.now()
            response.save()
            new_response = True
    else:
        response_form = ResponseForm()


    try:
        response = Reponse.objects.get(program__member__username=user,
                                          program__programName=programname,
                                          payload__payloadnumber=payloadnumber)
        if not response.finished:
            response = None

    except:
        response = None
        # Create new Response with finish value false
        tempResponse = Reponse(program=program,
                               payload=payload,
                               textresponse="")
        program.programCount += 1
        program.save()
        tempResponse.program = program
        tempResponse.save()




    # The page doesnt need to load if the payload doesnt exist


    return render(request,
                  'reTranslation/responsedetail.html',
                  {'program':program,
                   'response':response,
                   'payload':payload,
                   'response_form':response_form,
                   'new_response':new_response})
