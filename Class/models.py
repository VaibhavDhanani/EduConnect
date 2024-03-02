from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils.translation import gettext as _


# Create your models here.
class Class(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    subject = models.CharField(max_length=25,unique=True)
    teachername = models.CharField(max_length=30)

    class Meta:
        db_table = "Class"


class Student(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)

    # email = models.EmailField(_("Email"), max_length=254)
    # password = models.CharField(_("Password"), max_length=128)
    # def set_password(self, raw_password):
    #     self.password = make_password(raw_password)
    # def check_password(self, raw_password):
    #     return check_password(raw_password, self.password)

    class Meta:
        db_table = "Student"


class Teacher(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "Teacher"


class Lecture(models.Model):
    lec_id = models.AutoField(primary_key=True)
    link = models.URLField(max_length=250, null=False)
    class_name = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        to_field="subject",
        db_column="class_name",
        default="123456",
    )
    title = models.CharField(max_length=30)

    class Meta:
        db_table = "Lecture"



class Class_Teacher(models.Model):
    class_id = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        to_field="code",
        db_column="class_id",
    )
    teacher_id = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        to_field="id",
        db_column="teacher_id",
    )

    class Meta:
        db_table = "Class_Teacher"
        constraints = [
            models.UniqueConstraint(
                fields=["class_id", "teacher_id"], name="unique_class_teacher"
            )
        ]


class Class_Student(models.Model):
    class_id = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        to_field="code",
        db_column="class_id",
    )
    student_id = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        to_field="id",
        db_column="student_id",
    )

    class Meta:
        db_table = "Class_Student"
        constraints = [
            models.UniqueConstraint(
                fields=["class_id", "student_id"], name="unique_class_students"
            )
        ]


class Assignment(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    class_id = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        to_field="code",
        db_column="class_id",
    )
    asgmt_id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'Assignment'


class Test(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    test_id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        to_field="code",
        db_column="class_id",
    )

    class Meta:
        db_table = 'Test'


class Result(models.Model):
    res_id = models.AutoField(primary_key=True)
    test_id = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        to_field='test_id',
        db_column='test_id',
    )
    student_id = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        to_field="id",
        db_column="student_id",
    )
    marks = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        db_table = 'Result'


class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        to_field="code",
        db_column="class_id",
    )
    title = models.CharField(max_length=50)
    link = models.URLField(max_length=250, null=False)

    class Meta:
        db_table = 'Material'
