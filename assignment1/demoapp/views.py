from django.shortcuts import render
from .models import Company, Employee, Project


def index_demoapp(request):

    context = {
        # 'employees': Employee.objects.select_related('company').all()
        'companies': Company.objects.prefetch_related("employee_set", "employee_set__projects", "company_projects")
    }

    return render(request, 'demoapp/index.html', context)
