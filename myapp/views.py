
from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentModel, ResultModel



# HOME
def home(request):
    return render(request, 'home.html')



# STUDENT CRUD
def student_list(request):
    students = StudentModel.objects.all()

    return render(request, 'student_list.html', {
        'students': students
    })


def student_create(request):

    if request.method == 'POST':

        student_name = request.POST.get('student_name')
        admission_date = request.POST.get('admission_date')
        course_name = request.POST.get('course_name')
        course_fee = request.POST.get('course_fee')
        image = request.FILES.get('image')

        StudentModel.objects.create(
            student_name=student_name,
            image=image,
            admission_date=admission_date,
            course_name=course_name,
            course_fee=course_fee
        )

        return redirect('student_list')

    return render(request, 'student_form.html')


def student_update(request, id):

    student = get_object_or_404(StudentModel, id=id)

    if request.method == 'POST':

        student.student_name = request.POST.get('student_name')
        student.admission_date = request.POST.get('admission_date')
        student.course_name = request.POST.get('course_name')
        student.course_fee = request.POST.get('course_fee')

        image = request.FILES.get('image')

        if image:
            student.image = image

        student.save()

        return redirect('student_list')

    return render(request, 'student_form.html', {
        'student': student
    })


def student_delete(request, id):

    student = get_object_or_404(StudentModel, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'student_confirm_delete.html', {
        'student': student
    })



# RESULT CRUD
def result_list(request):

    results = ResultModel.objects.all()

    return render(request, 'result_list.html', {
        'results': results
    })


def result_create(request):

    if request.method == 'POST':

        student_name = request.POST.get('student_name')
        marks = request.POST.get('marks')
        grade = request.POST.get('grade')

        ResultModel.objects.create(
            student_name=student_name,
            marks=marks,
            grade=grade
        )

        return redirect('result_list')

    return render(request, 'result_form.html')


def result_update(request, id):

    result = get_object_or_404(ResultModel, id=id)

    if request.method == 'POST':

        result.student_name = request.POST.get('student_name')
        result.marks = request.POST.get('marks')
        result.grade = request.POST.get('grade')

        result.save()

        return redirect('result_list')

    return render(request, 'result_form.html', {
        'result': result
    })


def result_delete(request, id):

    result = get_object_or_404(ResultModel, id=id)

    if request.method == 'POST':
        result.delete()
        return redirect('result_list')

    return render(request, 'result_confirm_delete.html', {
        'result': result
    })

