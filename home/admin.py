from django.contrib import admin
from .models import Book
from .models import *
# Register your models here.

admin.site.register(Book)
admin.site.register(BookCategory)
admin.site.register(Cart)
admin.site.register(Order)