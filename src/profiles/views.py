import re

import codecs
import time

from django.db import IntegrityError
from django.http import Http404
from events.models import default_event_date, Registration
from profiles.forms import UserImportForm
from random import randint

from django.shortcuts import render
import csv

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from registration.forms import User

from .models import Profile


class ProfileList(ListView):
    model = Profile


def mass_update(request):

    new_staff_list = []
    new_student_list = []
    student_errors = []
    staff_errors = []
    staff_import = False
    student_import = False
    form = UserImportForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        if 'staff_csv_file' in request.FILES:
            file = request.FILES['staff_csv_file']
            reader = csv.reader(codecs.iterdecode(file, 'utf-8'))
            staff_import = True
            for row in reader:
                if row:  # check for blank rows
                    username = row[0]
                    qs = User.objects.all()
                    # check if user exists, else create new user
                    if not qs.filter(username=username).exists():
                        user = User.objects.create_user(
                            username=username,
                            password="wolf",
                            first_name=row[1],
                            last_name=row[2],
                            is_staff=True,
                        )
                        new_staff_list.append(user)

        if 'student_csv_file' in request.FILES:
            file = request.FILES['student_csv_file']
            semester = form.cleaned_data['semester']

            reader = csv.reader(codecs.iterdecode(file, 'utf-8'))
            student_import = True
            count = 0
            for row in reader:

                sn_regex_string = r"^(9[789])(\d{5})$"

                # skip empty rows
                if row:
                    # check for student number
                    if not re.match(sn_regex_string, row[0]):
                        student_errors.append({'error': "Student number doesn't match pattern", 'row': row})
                    else:
                        # students should have one entry for each semester, only use semester indicated in form
                        if row[5] == semester:
                            username = row[0]
                            first_name = row[1]
                            last_name = row[2]
                            homeroom_teacher = row[3]
                            grade = row[4]
                            phone = row[6]
                            email = row[7]

                            # validate data
                            try:  # sometimes homeroom id shows up as 0, which doesn't exist
                                homeroom_teacher = User.objects.get(username=homeroom_teacher)
                            except User.DoesNotExist:
                                student_errors.append({'warning': "Homeroom teacher not recognized", 'row': row})
                                homeroom_teacher = None
                            if not grade:  # needs an int so empty string is bad
                                grade = None
                            if not phone:
                                phone = None
                            if not email:
                                email = None

                            qs = User.objects.all()
                            # check if user exists, else create new user
                            if not qs.filter(username=username).exists():
                                user = User.objects.create_user(
                                    username=username,
                                    password="wolf",
                                    first_name=first_name,
                                    last_name=last_name,
                                )
                                new_student_list.append(user.id)
                            else:
                                user = User.objects.get(username=username)

                            # A profile is created automatically when a new user is created.  Update it.
                            # But sometimes errors cause a user to be created without a profile.  So just in case:
                            profile, created = Profile.objects.get_or_create(user=user)
                            homeroom_teacher = homeroom_teacher
                            profile.homeroom_teacher = homeroom_teacher
                            profile.grade = grade
                            profile.phone = phone
                            profile.email = email
                            profile.save()
                            count += 1
                            print(str(count) + ": " + str(profile))

            new_student_list = User.objects.all().filter(id__in=new_student_list)

    # student_import=True
    # new_student_list = User.objects.all().filter(is_staff=False)
    context = {
        "new_staff_list": new_staff_list,
        "staff_import": staff_import,
        "new_student_list": new_student_list,
        "student_import": student_import,
        "student_errors": student_errors,
        "form": form,
    }
    return render(request, "profiles/profile_imports.html", context)


def mass_user_import(request):
    # path = static("user_list.csv")
    path = "/home/couture/Developer/flex-site/static_cdn/user_list.csv"
    teachers = User.objects.all().filter(is_staff=True)

    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:

            try:
                user = User.objects.create_user(
                    username=row[0],
                    password="123123",
                    first_name=row[1],
                    last_name=row[2],
                )
            except IntegrityError:  # user already exists
                user = get_object_or_404(User, username=row[0])

            random_index = randint(0, len(teachers) - 1)

            # even if new user NOT created, update profile data
            profile = get_object_or_404(Profile, user=user)
            profile.first_name = row[1]
            profile.last_name = row[2]
            profile.homeroom_teacher = teachers[random_index]
            profile.save()

        return redirect("profiles:list")

