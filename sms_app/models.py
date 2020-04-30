from django.db import models
from account_app.models import User
from django.utils import timezone
from dashboard_app.models import Badge

class Teacher(models.Model):
    user = models.OneToOneField(User, related_name = 'teacher', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Müəllim'
        verbose_name_plural = 'Müəllimlər'

    def __str__(self):
        return self.user.get_full_name()


class Student(models.Model):
    user = models.OneToOneField(User, related_name = 'student', on_delete = models.CASCADE)
    group = models.ForeignKey('Group', related_name = 'students', on_delete = models.CASCADE)
    admission_date = models.DateField('Qəbul ili', )
    admission_point = models.PositiveIntegerField('Qəbul Balı', )
    badges = models.ManyToManyField(Badge, related_name = 'students', blank = True, null = True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Tələbə'
        verbose_name_plural = 'Tələbələr'

    def __str__(self):
        return f'{self.user.get_full_name()}'


class Group(models.Model):
    name = models.CharField('Adı', max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Qrup'
        verbose_name_plural = 'Qruplar'

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=127,)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fənn'
        verbose_name_plural = 'Fənnlər'


class Table(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    starts = models.DateTimeField('Başlama vaxtı',)
    ends = models.DateTimeField('Bitmə vaxtı',)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)
    class Meta:
        verbose_name = 'Cədvəl'
        verbose_name_plural = 'Cədvəllər'

    def __str__(self):
        return f'{self.subject.name} | {self.starts} | {self.ends}'


class Dairy(models.Model):

    POINT_CHOICES = (
        (1,'One'),
        (2,'Two'),
        (3,'Three'),
        (4,'Four'),
        (5,'Five'),
        (6,'Six'),
        (7,'Seven'),
        (8,'Eight'),
        (9,'Nine'),
        (10,'Ten'),
    )
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    table = models.ForeignKey(Table, on_delete = models.CASCADE)
    point = models.PositiveSmallIntegerField('Bal', choices= POINT_CHOICES)
    # day = models.DateField('Gün', default = timezone.now())

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return f' Şagird: {self.student.user.get_full_name()} | By teacher: {self.teacher.user.get_full_name()} | qiymət: {self.point} |\
        fənn: {self.table.subject.name} | vaxt: {self.table.starts}'

    class Meta:
        verbose_name = 'Gündəlik qiymət'
        verbose_name_plural = 'Gündəlik qiymətlər'


class NotParticipating(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Qayıb'
        verbose_name_plural = 'Qayıblar'

    def __str__(self):
        return f'{self.student.user.get_full_name()} | {self.table.starts}'


class Task(models.Model):
    name = models.CharField('Taskın adı', max_length = 127)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    deadline = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        verbose_name = 'Sərbəst '
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f'{self.name} | {self.subject.name} | {self.deadline}'


class StudentTask(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    point = models.PositiveIntegerField()

    created_at = models.DateTimeField(editable=False,auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return f'{self.student.user.get_full_name()} | {self.point}'

    class Meta:
        verbose_name = 'StudentTask '
        verbose_name_plural = 'StudentTasks'
