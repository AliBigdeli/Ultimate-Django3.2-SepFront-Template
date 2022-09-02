from rest_framework.response import Response
from rest_framework import generics, status, views, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.conf import settings


class ProfileApiView(views.APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "first_name": "Maryam",
            "last_name": "Farajian",
            "avatar": "https://avatars.githubusercontent.com/u/90143150?v=4",
            "job_title": "Frontend React Developer",
            "about": "I always wanted to be able to design website pages and display my ideas, until this dream became a reality and I started learning. After a few months of effort, I reached the result I wanted and now I am on the way to progress and experience something new every day. Whatever it is, I will do it with my will"
        }
        return Response(data, status=status.HTTP_200_OK)


class EducationListApiView(views.APIView):
    def get(self, request, *args, **kwargs):
        data = [{
            "id": 1,
            "university": "Applied science Karaj Worker House",
            "field": "Computer Science",
            "degree": "bachelor",
            "started_date": "2015",
            "ended_date": "2019"
        }]
        return Response(data, status=status.HTTP_200_OK)


class WorkExperienceListApiView(views.APIView):
    def get(self, request, *args, **kwargs):
        data = [{
            "id": 1,
            "job_title": "Frontend Developer and Tester",
            "company": "WomTechnologies",
            "started_date": "2022-1",
            "ended_date": "still",
            "description": "Working as a frontend developer and tester, design and implement pages plus testing website functionality."
        }]
        return Response(data, status=status.HTTP_200_OK)


class SkillListApiView(views.APIView):
    def get(self, request, *args, **kwargs):
        data = [
            {
                "id": 1,
                "name": "HTML"
            },
            {
                "id": 2,
                "name": "CSS/Responsive Design"
            },
            {
                "id": 3,
                "name": "JS/ES6"
            },
            {
                "id": 4,
                "name": "JSX"
            },
            {
                "id": 5,
                "name": "NPM"
            },
            {
                "id": 6,
                "name": "Bootstrap"
            },
            {
                "id": 7,
                "name": "Jquery"
            },
            {
                "id": 8,
                "name": "RestfulApi/CRUD "
            },
            {
                "id": 9,
                "name": "Axios/Fetch"
            },
            {
                "id": 10,
                "name": "Postman/ThunderClient"
            },
            {
                "id": 11,
                "name": "Swagger"
            }
        ]
        return Response(data, status=status.HTTP_200_OK)
