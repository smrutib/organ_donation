from django.contrib import admin
from admin_app.models import Heart_Waitlist,Liver_Waitlist,Kidney_Waitlist
from admin_app.models import Heart_Donor,Liver_Donor,Kidney_Donor
admin.site.register(Heart_Waitlist)
admin.site.register(Heart_Donor)
admin.site.register(Liver_Waitlist)
admin.site.register(Liver_Donor)
admin.site.register(Kidney_Waitlist)
admin.site.register(Kidney_Donor)
