from django.shortcuts import render
from .models import School
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.


def practice(request):

    # all.
    data = School.objects.all()
    print(data)

    # Filters.
    data = School.objects.filter(school_name='Anza')
    print(data)

    # Excludes.
    data = School.objects.exclude(school_name='yusuf merali')
    print(data)

    # Order by.
    data = School.objects.order_by('school_name')
    print(data)

    # Reverse.
    data = School.objects.reverse()[0:2]
    print(data)

    # Values.
    data = School.objects.values('school_name', 'school_students')
    print(data)

    # Values list
    data = School.objects.values_list('email_id')
    print(data)

    # Get.
    data = School.objects.get(id=1)
    print(data)

    # Create.
    # data = School.objects.create(school_name='Vidyamandir',
    #                              joining_date='2019-01-29',
    #                              pointer=8.3,
    #                              email_id='deepak@123.com',
    #                              school_students=68)
    # print(data)

    # data = School.objects.all()
    # print(data)

    # Get or Create
    # data = School.objects.get_or_create(school_name='St george',
    #                                     joining_date='2021-01-25',
    #                                     pointer=3.3,
    #                                     email_id='rohit@123.com',
    #                                     school_students=78)
    # print(data)

    # Bulk create.

    # obj1 = School(school_name='don bosco',
    #               joining_date='2021-08-27',
    #               pointer=10.0,
    #               email_id='amruta@123.com',
    #               school_students=58)
    # obj2 = School(school_name='ST ignatius',
    #               joining_date='2023-05-30',
    #               pointer=3.7,
    #               email_id='ashish@123.com',
    #               school_students=28)
    # ls = [obj1, obj2]
    # data = School.objects.bulk_create(ls)
    data = School.objects.all()
    print(data)

    return HttpResponse('ORM Practice')
