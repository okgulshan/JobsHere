from django.contrib import admin
from .models import Listing,JobListing,contactUs,reportIssue,JobApplication

# Register your models here.

admin.site.register(Listing)
admin.site.register(JobListing)
class contactUsAdmin(admin.ModelAdmin):
    list_display=('yourname','email','message')

class reportIssueAdmin(admin.ModelAdmin):
    list=('reportedby','Description')

admin.site.register(contactUs,contactUsAdmin)
admin.site.register(reportIssue,reportIssueAdmin)
admin.site.register(JobApplication)