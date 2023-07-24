# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Applicant


def update_excel_sheet():
    from openpyxl import Workbook

    wb = Workbook()
    sheet = wb.active
    sheet.title = 'Applicant Data'
    headers = [field.name for field in Applicant._meta.fields]
    sheet.append(headers)

    for obj in Applicant.objects.all():
        row = [str(getattr(obj, field)) for field in headers]
        sheet.append(row)

    wb.save('applicant_data.xlsx')


@receiver(post_save, sender=Applicant)
def applicant_post_save(sender, instance, created, **kwargs):
    if created:
        update_excel_sheet()
