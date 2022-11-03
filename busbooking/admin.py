from statistics import mode
from unittest import mock
from django.contrib import admin
from .models import  needblood
from .models import donate


# Register your models here.

admin.site.register(needblood)
admin.site.register(donate)
