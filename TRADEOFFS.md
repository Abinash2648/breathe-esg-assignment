# TRADEOFFS.md

## 1 No Authentication System

The prototype does not implement:
- JWT authentication
- RBAC
- SSO

Reason:
The focus was ingestion workflow and data modeling.

---

# 2 No PDF Parsing

Utility PDF parsing was intentionally excluded.

Reason:
OCR pipelines introduce:
- parsing complexity
- inconsistent layouts
- additional dependencies

CSV ingestion was prioritized instead.

---

# 3 No Real SAP API Integration

The system does not connect directly to SAP.

Reason:
Real SAP integrations require:
- enterprise access
- credentials
- middleware configuration

CSV exports were used to simulate realistic ingestion.

---

# 4 No Async Processing

Uploads are processed synchronously.

Reason:
The assignment scope was prototype-level.

Production systems would likely use:
- Celery
- Kafka
- background workers

---

# 5 No Suspicious Row Detection Engine

The prototype does not automatically flag anomalies.

Reason:
Rule design requires:
- business thresholds
- historical benchmarks
- domain-specific logic

This was intentionally deferred.