from django.urls import path,include
from . import views

app_name = 'api-v1'

urlpatterns = [
    # Registration management
    path("profile/", views.ProfileApiView.as_view(), name="profile"),
    path("educations/", views.EducationListApiView.as_view(), name="educations"),
    path("work-experiences/", views.WorkExperienceListApiView.as_view(), name="work_experiences"),
    path("skills/", views.SkillListApiView.as_view(), name="skills"),
]
