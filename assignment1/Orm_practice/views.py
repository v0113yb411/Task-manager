from django.shortcuts import render
from .models import School, Student
from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Count
from demoapp.models import Company, Employee, Project


def index_demoapp(request):

    context = {
        'employees': Employee.objects.all()
    }

    return render(request, 'test.html', context)


def practice(request):

    # # all.
    # data = School.objects.all()
    # print(data)

    # # Filters.
    # data = School.objects.filter(school_name='Anza')
    # print(data)

    # # Excludes.
    # data = School.objects.exclude(school_name='yusuf merali')
    # print(data)

    # # Order by.
    # data = School.objects.order_by('school_name')
    # print(data)

    # # Reverse.
    # data = School.objects.reverse()[0:2]
    # print(data)

    # # Values.
    # data = School.objects.values('school_name', 'school_students')
    # print(data)

    # # Values list
    # data = School.objects.values_list('email_id')
    # print(data)

    # # Get.
    # data = School.objects.get(id=1)
    # print(data)

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
    # data = School.objects.all()
    # print(data)

    # Bulk Update.

    # object = [
    #     School.objects.create(school_name='Anza',
    #                           # joining_date='2023-05-30',
    #                           pointer=6.70,
    #                           email_id='Rucha@123.com',
    #                           school_students=100),
    #     School.objects.create(school_name='don bosco',
    #                           # joining_date='2023-05-30',
    #                           pointer=10.00,
    #                           email_id='amruta@123.com',
    #                           school_students=58),
    # ]

    # obj1 = School.objects.get(id=25)
    # obj2 = School.objects.get(id=26)
    # object = [obj1, obj2]
    # object[0].school_name = 'St.joseph'
    # object[1].school_name = 'Miachel high school'
    # School.objects.bulk_update(object, ['school_name'])
    # data = School.objects.all()
    # print(data)

    # Count.

    # data = School.objects.all().count()
    # print(data)

    # Latest.

    # data = School.objects.latest('id')
    # print(data)

    # # First.

    # data = School.objects.order_by('id').first()
    # print(data)

    # Last.

    # data = School.objects.order_by('school_students').last()
    # print(data)

    # Aggregate.

    # data = School.objects.aggregate(Count('email_id'))
    # print(data)

    # Exists().

    # data = School.objects.filter(school_students=987).exists()
    # print(data)

    # Update.

    # data = School.objects.filter(school_name='don bosco').update()
    # print(data)

    # # Delete.

    # data = School.objects.filter(school_name='ANZA').delete()
    # print(data)

    # Select Related.

    data = School.objects.select_related('student_details')
    print(data)
    for i in data:
        test = i.student_details.student_name
        print(test)

    # Prefetch related.

    # data = Students.objects.prefetch_related('school_set')
    # print(data)
    # for i in data:
    #     print(i.school_set.all())
    #     for j in data:
    #         print(j.school_set.all())

        return render(request, 'test.html')
