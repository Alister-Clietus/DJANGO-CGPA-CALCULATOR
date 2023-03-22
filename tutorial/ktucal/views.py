from django.shortcuts import render,redirect
from ktucal.models import result

# Create your views here.
def home(request):
   return render(request,'home.html')
   

def calculate(request):
    if request.method=='POST':
      name=request.POST.get('name',None)
      rollno=request.POST.get('rollno',None)
      s1=float(request.POST.get('s1',None))
      s1sum=s1*17
      s2=float(request.POST.get('s2',None))
      s2sum=s2*21
      s3=float(request.POST.get('s3',None))
      s3sum=s3*22
      s4=float(request.POST.get('s4',None))
      s4sum=s4*22
      s5=float(request.POST.get('s5',None))
      s5sum=s5*23
      s6=float(request.POST.get('s6',None))
      s6sum=s6*23
      s7=float(request.POST.get('s7',None))
      s7sum=s7*15
      s8=float(request.POST.get('s8',None))
      s8sum=s8*17
      totalsemsum=float(s1sum+s2sum+s3sum+s4sum+s5sum+s6sum+s7sum+s8sum)
      cgpa=float(totalsemsum/160)
      temp = result.objects.create(
         Name=name,
         Rollno=rollno,
         Semester_1=s1,Semester_2=s2,Semester_3=s3,Semester_4=s4,
         Semester_5=s5,Semester_6=s6,Semester_7=s7,Semester_8=s8,
         Total_CGPA=cgpa)
      temp.save()
      final={'name':name,'rollno':rollno,'cgpa':cgpa,}
      return render(request,'suc.html',{'final':final})
    else:
      return render(request,'ktucal.html')

         