from django.db import models

class DepartmentModel(models.Model):
    department_name = models.CharField(max_length=100)
    description = models.TextField()
    department_head = models.CharField(max_length=100)


def __str__(self):
    return self.department_name


class CourseModel(models.Model):
    course_title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')


def __str__(self):
    return self.course_title


class StudentModel(models.Model):
    student_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='students/')
    admission_date = models.DateField()
    course_name = models.CharField(max_length=150)
    course_fee = models.DecimalField(max_digits=10, decimal_places=2)


def __str__(self):
    return self.student_name


class TeacherModel(models.Model):
    teacher_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)


def __str__(self):
    return self.teacher_name


class ResultModel(models.Model):
    student_name = models.CharField(max_length=100)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=5)


def __str__(self):
    return self.student_name

