from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.core.paginator import Paginator

def studentview(request):
    student = Student.objects.all()
    paginator = Paginator(student,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'FirstApp/laptop_list.html',{'page_obj':page_obj})

def addView(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            rollno=form.cleaned_data['rollno']
            name=form.cleaned_data['name']
            course=form.cleaned_data['course']
            marks=form.cleaned_data['marks']
            fees=form.cleaned_data['fees']

            laptop= Student(rollno=rollno,name=name,course=course,marks=marks,fees=fees)
            laptop.save()
            return redirect('home')
    template_name = 'addlap.html'
    context = {'form': form}
    return render(request, template_name, context)

def delete(request,i):
    student=Student.objects.get(id=i)
    student.delete()
    return redirect('home')

def update(request,i):
    student=Student.objects.get(id=i)
    form=StudentForm(instance=student)
    if request.method == 'POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    template_name = 'addlap.html'
    context = {'form': form}
    return render(request, template_name, context)


