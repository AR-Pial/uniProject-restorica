from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Signup)
admin.site.register(FoodItem)
admin.site.register(Message)
admin.site.register(Order)
admin.site.register(TableBooking)


