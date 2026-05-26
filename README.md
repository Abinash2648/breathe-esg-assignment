# Breathe ESG – Emissions Data Ingestion Platform

A Django REST + React prototype for ESG emissions ingestion, normalization, analyst review, and audit workflows.

---

# Live Deployment

Frontend:
https://your-frontend.vercel.app

Backend API:
https://your-backend.onrender.com

Admin Panel:
https://your-backend.onrender.com/admin

---

# GitHub Repository

https://github.com/yourusername/breathe-esg-assignment

---

# Tech Stack

## Backend
- Django
- Django REST Framework
- SQLite
- Gunicorn

## Frontend
- React
- Bootstrap
- Axios

## Deployment
- Render (Backend)
- Vercel (Frontend)

---

# Architecture

## Frontend
React dashboard consuming Django REST APIs.

## Backend
Django REST Framework handling:
- CSV ingestion
- normalization
- emissions calculation
- approval workflows
- audit logging

## Database
SQLite used for prototype persistence and relational modeling.

---

# Project Overview

This project is a prototype ESG emissions ingestion and review platform built using Django REST Framework and React.

The system simulates how enterprise sustainability teams ingest emissions-related operational data from multiple disconnected business systems and normalize it into a unified review workflow for analysts.

The platform focuses on three common enterprise data sources:

- SAP exports for fuel and procurement activity
- Utility electricity consumption data
- Corporate travel activity data

The system supports:

- CSV-based ingestion
- Data normalization
- Automatic emissions calculation
- Audit logging
- REST APIs for retrieval
- Analyst review workflows

The goal of the project is to demonstrate realistic backend architecture and ingestion logic rather than building a feature-heavy CRUD application.

---

# Features

## 1. CSV Data Ingestion

The platform supports CSV uploads representing enterprise operational data from different ESG-related systems.

Supported source categories:

- Fuel consumption
- Electricity usage
- Travel activity

---

## 2. Automatic Emissions Calculation

Each uploaded record automatically calculates total emissions using:

```text
Total Emission = Raw Value × Emission Factor
```

Example:

- Diesel Fuel = 500 Liters
- Emission Factor = 2.68
- Total Emission = 1340.0

This logic is implemented at the model layer to ensure consistency across ingestion workflows.

---

## 3. Audit Logging

Audit log entries are generated during analyst approval workflows to maintain traceability and review history.

The audit system tracks:

- Action performed
- Old value
- New value
- Timestamp
- User/system actor

This improves traceability and supports future compliance workflows.

---

## 4. REST APIs

The platform exposes REST APIs for:

- CSV ingestion
- Emission data retrieval
- Analyst approval workflows

The APIs are designed to simulate ingestion pipelines used in ESG reporting systems.

---

## 5. Multi-Source ESG Data Handling

The architecture is designed to support multiple ESG data categories:

- Scope 1
- Scope 2
- Scope 3

This allows future expansion into broader carbon accounting workflows.

---

## 6. Django Admin Dashboard

The Django admin panel is used as an internal analyst review interface where uploaded records and audit logs can be inspected and verified.

---

# Analyst Review Workflow

The platform supports a lightweight analyst review workflow:

1. Upload ESG activity data
2. Normalize and calculate emissions
3. Review records in dashboard/admin panel
4. Approve records for audit readiness
5. Maintain audit logs for traceability

This simulates a simplified enterprise ESG operational workflow.

---

# APIs

## Upload CSV API

### Endpoint

```text
POST /api/upload-csv/
```

### Description

Uploads and processes ESG emission records from CSV files.

### Supported Fields

| Field | Description |
|-------|-------------|
| scope_type | Scope category |
| category | Emission category |
| raw_unit | Original measurement unit |
| normalized_unit | Standardized unit |
| raw_value | Activity value |
| emission_factor | CO2 emission factor |

---

## Get Emissions API

### Endpoint

```text
GET /api/emissions/
```

### Description

Returns all uploaded emission records in JSON format.

---

## Approve Emission API

### Endpoint

```text
POST /api/approve/<id>/
```

### Description

Approves an emission record and creates an audit log entry for traceability.

---

# Setup Steps

## 1. Clone Repository

```bash
git clone <repository-url>
cd breathe-esg-assignment
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 6. Create Admin User

```bash
python manage.py createsuperuser
```

---

## 7. Start Backend Server

```bash
python manage.py runserver
```

---

## 8. Start Frontend

```bash
cd frontend
npm install
npm start
```

---

## 9. Open Application

### Frontend

```text
http://localhost:3000
```

### Admin Panel

```text
http://127.0.0.1:8000/admin
```

### APIs

```text
http://127.0.0.1:8000/api/upload-csv/
```

```text
http://127.0.0.1:8000/api/emissions/
```

---

# Sample CSV Format

```csv
scope_type,category,raw_unit,normalized_unit,raw_value,emission_factor
Scope 1,Diesel,Liters,Liters,500,2.68
Scope 2,Electricity,kWh,kWh,1200,0.82
Scope 3,Travel,km,km,2000,0.15
```

---

# Sample Source Files

## sample_sap_fuel.csv

```csv
plant_code,fuel_type,quantity,unit,date,vendor
PLT1001,Diesel,500,Liters,2026-05-01,Shell
PLT1002,Petrol,300,Liters,2026-05-02,BP
```

---

## sample_utility.csv

```csv
meter_id,billing_period,electricity_kwh,cost
MTR001,2026-04,1200,15000
MTR002,2026-04,900,12000
```

---

## sample_travel.csv

```csv
employee,travel_type,from_location,to_location,distance_km
John Doe,Flight,DEL,BOM,1150
Jane Smith,Cab,Delhi,Gurgaon,35
```

---

# Design Decisions

## Why CSV-Based Ingestion?

Enterprise ESG onboarding workflows commonly begin with manually exported CSV files from operational systems.

CSV ingestion was chosen because:

- It is realistic for early-stage onboarding
- Easier to validate and normalize
- Reduces dependency on external APIs
- Common in sustainability reporting workflows

---

## Why Django REST Framework?

Django REST Framework allowed rapid prototyping of:

- ingestion APIs
- admin review workflows
- relational data models
- audit logging

while maintaining clean backend architecture.

---

## Why React Frontend?

React was used to build a lightweight analyst dashboard for:

- reviewing uploaded records
- visualizing emissions
- approving workflows
- improving analyst usability

The frontend was intentionally kept simple and operationally focused.

---

# Deployment Notes

The backend API is deployed on Render using Gunicorn.

The frontend React application is deployed on Vercel and communicates with the Django REST backend through REST APIs.

CORS handling was enabled to allow secure frontend-backend communication during deployment.

---

# Admin Credentials

Username: admin

Password: admin123

---

# Future Improvements

Possible future enhancements include:

- asynchronous ingestion pipelines
- background task queues
- PDF utility bill parsing
- SAP API integrations
- authentication and RBAC
- anomaly detection for suspicious emissions
- bulk approval workflows
- advanced reporting dashboards

---

# Conclusion

This prototype demonstrates a realistic ESG ingestion workflow focused on:

- clean data modeling
- ingestion pipelines
- auditability
- normalization
- backend engineering fundamentals

The implementation prioritizes clarity, maintainability, and realistic operational workflows over excessive feature complexity.