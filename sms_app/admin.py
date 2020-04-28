from django.contrib import admin
admin.autodiscover()
from .models import (
    Teacher,Student,Group,
    Subject,Table,Dairy,
    NotParticipating,Task,StudentTask,
)


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Table)
admin.site.register(Dairy)
admin.site.register(NotParticipating)
admin.site.register(Task)
admin.site.register(StudentTask)
