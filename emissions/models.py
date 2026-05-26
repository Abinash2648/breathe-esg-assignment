from django.db import models


class Company(models.Model):

    name = models.CharField(max_length=255)

    industry = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class DataSource(models.Model):

    SOURCE_TYPES = (
        ('SAP', 'SAP'),
        ('UTILITY', 'UTILITY'),
        ('TRAVEL', 'TRAVEL'),
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=50,
        choices=SOURCE_TYPES
    )

    uploaded_by = models.CharField(max_length=255)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=50,
        default='processed'
    )



class EmissionRecord(models.Model):

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    data_source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    scope_type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    raw_unit = models.CharField(max_length=50)
    normalized_unit = models.CharField(max_length=50)

    raw_value = models.FloatField()
    emission_factor = models.FloatField()

    total_emission = models.FloatField(default=0)
    status = models.CharField(
    max_length=50,
    default='Pending'
)

    def save(self, *args, **kwargs):
        self.total_emission = self.raw_value * self.emission_factor
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category


class AuditLog(models.Model):

    record = models.ForeignKey(
        EmissionRecord,
        on_delete=models.CASCADE
    )

    action = models.CharField(max_length=255)

    old_value = models.TextField(
        null=True,
        blank=True
    )

    new_value = models.TextField(
        null=True,
        blank=True
    )

    changed_by = models.CharField(max_length=255)

    timestamp = models.DateTimeField(auto_now_add=True)