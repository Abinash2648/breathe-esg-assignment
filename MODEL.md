
---

# MODEL.md

```md
# MODEL.md

## Data Model Design

The system was designed to support enterprise ESG ingestion workflows where data arrives from multiple external systems in inconsistent formats.

The core design goal was:
- source traceability
- auditability
- emission normalization
- analyst review workflow

---

# Models

## 1 Company

Represents a client organization onboarded to the ESG platform.

### Fields
- name
- industry

### Why

Enterprise ESG systems are multi-tenant by nature.  
Each uploaded dataset belongs to a company.

---

## 2 DataSource

Tracks where uploaded data originated from.

### Fields
- company
- source_type
- uploaded_by
- uploaded_at
- status

### Why

Enterprise emissions data comes from multiple systems:
- SAP
- Utility portals
- Travel platforms

Tracking the original source is important for:
- audit verification
- traceability
- debugging ingestion issues

---

## 3 EmissionRecord

Stores normalized emissions/activity records.

### Fields
- scope_type
- category
- raw_unit
- normalized_unit
- raw_value
- emission_factor
- total_emission

### Why

Different sources expose different units and formats.

The model stores:
- original source units
- normalized units
- calculated emissions

This allows analysts to trace how emissions were derived.

---

# Emission Calculation

Total emissions are automatically calculated during save:

```python
total_emission = raw_value * emission_factor