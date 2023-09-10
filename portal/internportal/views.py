from django.shortcuts import render
from .models import Internship_details
from .models import Applicant
from .models import contactform


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
    

def internship(request):
    internships = Internship_details.objects.all()
    return render(request, 'internship.html', {'internships': internships})

def faqs(request):
    return render(request,'faq.html')

def index(request):
    return render(request,'index.html')

def abouts(request):
    return render(request,'about.html')

def contact(request):
    contacts=contactform.objects.all()
    if request.method == 'POST':
       first_name = request.POST.get('first')
       last_name = request.POST.get('last')
       mobile = request.POST.get('mobile')
       email = request.POST.get('email')
       course = request.POST.get('course')
       query = request.POST.get('query')
       contact = contactform(
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            email=email,
            course=course,
            query=query
        )
       contact.save()
       return render(request, 'success.html')

    return render(request, 'contact.html',{'contacts':contacts})

def success(request):
    return render(request,'sucess.html')

def datascience(request):
    return render(request,'dscur.html')

def embedded(request):
    return render(request,'escur.html')

def projects(request):
    return render(request,'projects.html')