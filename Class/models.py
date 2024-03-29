from django.utils import timezone
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils.translation import gettext as _


# Create your models here.
class Class(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    subject = models.CharField(max_length=25, unique=True)
    teachername = models.CharField(max_length=30)

    class Meta:
        db_table = "Class"


class Student(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
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
    asgmt_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    class_name = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        to_field="subject",
        db_column="class_name",
        null=False,
        default="ok"
    )

    class Meta:
        db_table = 'Assignment'


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
    name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'Material'


class Submission(models.Model):
    sub_id = models.AutoField(primary_key=True)
    asgmt_id = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        to_field="asgmt_id",
        db_column="asgmt_id",
    )
    student_id = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        to_field="id",
        db_column="student_id",
    )
    link = models.URLField(max_length=250, null=False)
    name = models.CharField(max_length=50, null=False)
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Submission'
        constraints = [
            models.UniqueConstraint(
                fields=["asgmt_id"], name="unique_submission"
            )
        ]
