from django.contrib import admin
from .models import PersonalDetail
from .models import FamilyMember
from .models import Education, EducationImage

admin.site.register(PersonalDetail)
admin.site.register(FamilyMember)
admin.site.register(Education)
admin.site.register(EducationImage)