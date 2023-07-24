from django.shortcuts import render
from django.http import HttpResponse
from .models import Internship_details
from .models import Applicant
from django.shortcuts import render

def display_details(request, internship_id):
    internship = Internship_details.objects.get(id=internship_id)
    responsibilities = internship.responsibilities.split("\n") if internship.responsibilities else []
    skills = internship.skills.split("\n") if internship.skills else []
    requirements = internship.requirements.split("\n") if internship.requirements else []
    benefits = internship.perks_and_benefits.split("\n") if internship.perks_and_benefits else []

    context = {
        'internship': internship,
        'responsibilities': responsibilities,
        'skills': skills,
        'requirements':requirements,
        'benefits':benefits,
    }

    return render(request, 'display.html', context)

def login(request):
    applys = Applicant.objects.all()
    if request.method == 'POST':
        firname = request.POST['firname']
        lasname = request.POST['lasname']
        mobile=request.POST['mobile']
        email = request.POST['email']
        college=request.POST['college']
        edu=request.POST['edu']
        jobtitle=request.POST['jobtitle']
        exp=request.POST['exp']
        projects = request.POST['projects']
        train = request.POST['train']
        loc = request.POST['loc']
        skills = request.POST['skills']
        lan = request.POST['lan']
        why_job = request.POST['why_job']
        resume = request.FILES['resume']
        if Applicant.objects.filter(email=email, jobtitle=jobtitle).exists():
            return render(request,'login.html', {'applys': applys, 'show_popup': True})
        else:
            applicant = Applicant(firname=firname, lasname=lasname, mobile=mobile, email=email, college=college, edu=edu,
                                  exp=exp, train=train, loc=loc, lan=lan,
                                  jobtitle=jobtitle, skills=skills, projects=projects,
                                  resume=resume, why_job=why_job)
            applicant.save()
            return render(request, 'success.html')

    
    return render(request, 'login.html', {'applys': applys})
    

def index(request):
    internships = Internship_details.objects.all()
    return render(request, 'index.html', {'internships': internships})
