from django.contrib import admin

from appadmin.models import BeautySaloon, Serivice, Employee, Schedule, Customer

# Register your models here.
admin.site.register(BeautySaloon)
admin.site.register(Employee)
admin.site.register(Serivice)
admin.site.register(Customer)
admin.site.register(Schedule)