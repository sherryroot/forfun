from django.contrib import admin


# Register your models here.
from .models import Orders_td
from .models import Orders_tm
from .models import Orders_af

admin.site.register(Orders_td)
admin.site.register(Orders_tm)
admin.site.register(Orders_af)