from django.shortcuts import render

# Create your views here.
def student_info_views(request):
    employees=Employee.objects.all()
    return render(request,'testapp/results.html',{'employees':employees})
    
