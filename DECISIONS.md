
---

# DECISIONS.md

```md
# DECISIONS.md

## 1 Why Django REST Framework

I selected Django REST Framework because:
- fast backend development
- built-in admin panel
- ORM support
- strong API tooling

The assignment prioritized system design and ingestion workflows over frontend complexity.

---

# 2 Why CSV Upload Instead of Live SAP Integration

Real SAP integrations require:
- authentication
- enterprise credentials
- SAP middleware

For the prototype, CSV upload was chosen because:
- SAP exports are commonly shared as flat files
- CSV ingestion demonstrates normalization logic
- easier to test locally

---

# 3 Why Utility CSV Instead of PDF Parsing

Utility companies often provide:
- portal CSV exports
- downloadable bills
- APIs

CSV was selected because:
- realistic for analyst workflows
- simpler ingestion pipeline
- avoids OCR complexity in a prototype

---

# 4 Why Simplified Travel Data

Corporate travel platforms expose:
- flights
- hotels
- taxis
- airport codes

The prototype simplified this into:
- travel type
- source location
- destination
- distance

to focus on emissions ingestion rather than itinerary reconstruction.

---

# 5 Why SQLite

SQLite was selected because:
- lightweight
- fast setup
- suitable for prototype delivery

For production:
- PostgreSQL would be preferred.

---

# 6 Why Django Admin

The assignment required analyst review workflows.

Django Admin provided:
- fast internal dashboard creation
- record review
- audit visibility

without spending excessive time on frontend implementation.

---

# Questions I Would Ask PM

- Expected ingestion volume?
- Real SAP integration expectations?
- Should approval locking be immutable?
- Should suspicious emissions detection be rule-based or ML-based?
- Which emission factor standards should be used?