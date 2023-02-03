from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=100)

    # Refererence: https://docs.djangoproject.com/en/4.1/ref/models/options/
    class Meta:
        db_table = "company"

    def __str__(self):
        return self.company_name


class Project(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE,
        related_name="company_projects"
    )
    project_name = models.CharField(max_length=100)

    class Meta:
        db_table = "project"

    def __str__(self):
        return self.project_name


class Employee(models.Model):
    # Reference: https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.employee_name
