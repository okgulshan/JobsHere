from django.shortcuts import render,redirect
from .models import Listing,JobListing,reportIssue,contactUs,JobApplication
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

# home page

def homepage(request):
    return render(request , 'homepage.html')

# job posting page

def jobposting(request):
    jobs = JobListing.objects.all()
    return render(request , 'job list portal.html',{'jobs':jobs})
# internship posting page 

def internshipposting(request):
    interns = Listing.objects.all()
    return render(request ,'intern list portal.html',{'interns':interns})

# Footer 

def aboutus(request):
    return render(request , 'about us.html')

def privacypolicy(request):
    return render(request , 'privacy policy.html')

def reportissue(request):
    n=''
    if request.method=="POST":
        rep= str(request.POST.get('reportedby'))
        des= str(request.POST.get('Description'))

        info = reportIssue(
            reportedby=rep,
            Description=des,)
        info.save()
        n='Issue Reported'

    return render(request , 'report issue.html', {'n':n})

def contactus(request):
    m=''
    if request.method=="POST":
        yn= str(request.POST.get('yourname'))
        em= str(request.POST.get('email'))
        msg= str(request.POST.get('message'))

        cont = contactUs (
            yourname=yn,
            email=em,
            message=msg,)
        cont.save()
        m='Thanks for Contacting Us'
       
    return render(request , 'contact us.html',{'m':m})

# job postings

def loreal(request):
    return render(request , 'Sales Manager Loreal.html')

def apollo(request):
    return render(request , 'ENT Apollo Hospitals.html')

def sarlabirla(request):
    return render(request , 'Physics Teacher SBPS.html')

def microsoft(request):
    return render(request , 'Software Engineer Microsoft.html')

# internship posting

def techolution(request):
    return render(request , 'AI Internship Techolution.html')

def axiom(request):
    return render(request , 'Python Internship Axiom.html')

def happyfox(request):
    return render(request , 'QA Internship Happyfox.html')

def cadence(request):
    return render(request , 'PV Internship Cadence.html')

def filter(request):
    return render(request,'filter.html')

# Ronak internship
def savedata(request):
    n =""
    jbt = ""
    r = ""
    jd = ""
    res = ""
    qua = ""
    gab = ""
    ai = ""
    b = ""
    loc = ""
    
    if request.method == "POST":
            n =(request.POST.get('companyname'))
            jbt =(request.POST.get('jobtype'))
            r =(request.POST.get('role'))
            jd = request.POST.get('jobdescription')
            res =(request.POST.get('responsibilities'))
            qua =(request.POST.get('qualifications'))
            gab =(request.POST.get('gainsandbenefits'))
            ai =(request.POST.get('additionalinformation'))
            b = request.FILES.get('banner')
            loc =(request.POST.get('location'))

    data = Listing(companyname = n,
                   jobtype=jbt,
                   role = r,
                   jobdescription=jd,
                   responsibilities=res,
                   qualifications=qua,
                   gainsandbenefits=gab,
                   additionalinformation=ai,
                   banner=b,
                   location = loc)
    if n!="":
        data.save()
    return render(request ,'output.html')

def detailpage(request):
    data = Listing.objects.all()
    return render(request,'dynamic.html',{'data':data})

# RONAK JOB 
def savejobdata(request):
    cn =""
    jbt = ""
    r = ""
    jd = ""
    res = ""
    qua = ""
    gab = ""
    ai = ""
    b = ""
    loc = ""

    if request.method == "POST":
            cn = str(request.POST.get('companyname'))
            jbt = str(request.POST.get('jobtype'))
            r = str(request.POST.get('role'))
            jd = str(request.POST.get('jobdescription'))
            res = str(request.POST.get('responsibilities'))
            qua = str(request.POST.get('qualifications'))
            gab = str(request.POST.get('gainsandbenefits'))
            ai = str(request.POST.get('additionalinformation'))
            b = request.POST.get('banner')
            loc = str(request.POST.get('location'))

    data = JobListing(companyname = cn,
                   jobtype=jbt,
                   role = r,
                   jobdescription=jd,
                   responsibilities=res,
                   qualifications=qua,
                   gainsandbenefits=gab,
                   additionalinformation=ai,
                   banner=b,
                   location = loc)
    if cn!="":
        data.save()
    return render(request , 'jobform.html')

def jobdetailpage(request):
    jobs = JobListing.objects.all()
    return render(request,'jobsdynamic.html',{'jobs':jobs})

def base(request):
    return render(request ,'base.html')

# DHRUV'S APPLICATION FORM
def saveApplicationForm(request):
    if request.method == "POST":
        fn = str(request.POST.get('fullname'))
        em = str(request.POST.get('email'))
        pno = str(request.POST.get('phone'))
        cmpnies = str(request.POST.get('companies'))
        rsme = request.FILES.get('resume')
        q1 = str(request.POST.get('ques1'))
        q2 = str(request.POST.get('ques2'))
        q3 = str(request.POST.get('ques3'))

        data = JobApplication(fullname = fn, email = em, phone = pno, companies = cmpnies, resume = rsme, ques1 = q1, ques2 = q2, ques3 = q3)
        data.save()
        
        return redirect('homepage')
    else:
        listings = Listing.objects.all()  # Fetch all listings
        return render(request, 'apply here.html', {'listings': listings})

def indexpage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid username.')
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Password does not match with username.')

    context = {}
    return render(request , 'index.html', context)

# signup

def signup(request):
    if request.method =='POST':
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        pswd=request.POST.get('password1')
        pswd2=request.POST.get('password2')

        if not (fname and lname and email and username and pswd and pswd2):
            messages.error(request, "All fields are required")
        elif pswd != pswd2:
            messages.error(request, "Your password and confirm password are not the same")
        else:
            try:
                # Check if username already exists
                User.objects.get(username=username)
                messages.error(request, "Username already exists")
            except User.DoesNotExist:
                # Create new user
                myuser = User.objects.create_user(username=username, email=email, password=pswd, first_name=fname, last_name=lname)
                myuser.save()
                messages.success(request, "Account created successfully. You can now log in.")
                return redirect('/')  # Redirect to login page after successful signup
    
    return render(request, "signup.html")

