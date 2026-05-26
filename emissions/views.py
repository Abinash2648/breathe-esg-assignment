from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .serializers import EmissionRecordSerializer
import csv
from .models import *


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])

def upload_csv(request):

    file = request.FILES.get('file')

    if not file:
        return Response({
            "error": "No file uploaded"
        })

    # Get or Create Company
    company, created = Company.objects.get_or_create(
        name="Demo Company",
        industry="Manufacturing"
    )

    # Get or Create Data Source
    data_source, created = DataSource.objects.get_or_create(
        company=company,
        source_type="SAP",
        uploaded_by="Admin"
    )

    decoded_file = file.read().decode('utf-8').splitlines()

    reader = csv.DictReader(decoded_file)

    added_records = 0

    for row in reader:

        record, created = EmissionRecord.objects.get_or_create(

            company=company,
            data_source=data_source,

            scope_type=row['scope_type'],
            category=row['category'],

            raw_unit=row['raw_unit'],
            normalized_unit=row['normalized_unit'],

            raw_value=float(row['raw_value']),
            emission_factor=float(row['emission_factor'])

        )

        if created:
            added_records += 1

    return Response({
        "message": "CSV uploaded successfully",
        "new_records_added": added_records
    })


@api_view(['GET'])
def get_emissions(request):

    records = EmissionRecord.objects.all()

    serializer = EmissionRecordSerializer(
        records,
        many=True
    )

    return Response(serializer.data)


@api_view(['POST'])
def approve_emission(request, id):

    try:

        record = EmissionRecord.objects.get(id=id)

        old_status = record.status

        record.status = "Approved"

        record.save()

        # Create Audit Log
        AuditLog.objects.create(
            record=record,
            action="Approved Emission",

            old_value=old_status,
            new_value="Approved",

            changed_by="Admin"
        )

        return Response({
            "message": "Emission approved"
        })

    except EmissionRecord.DoesNotExist:

        return Response({
            "error": "Record not found"
        })