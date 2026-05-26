# SOURCES.md

# 1 SAP Fuel & Procurement Data

## Research

I researched common SAP export approaches including:
- IDoc
- OData
- Flat file exports

For the prototype, I selected CSV/flat file style exports because they are commonly shared between enterprise systems and sustainability teams.

---

# Typical SAP Characteristics

- plant codes
- vendor identifiers
- inconsistent units
- date formatting differences

---

# Sample Data Design

The sample fuel data contains:
- plant codes
- fuel quantities
- vendors
- units
- dates

to simulate realistic operational exports.

---

# 2 Utility Electricity Data

## Research

Utility providers commonly expose:
- portal CSV exports
- downloadable PDF bills
- APIs

CSV export was selected because it is common in facilities workflows.

---

# Typical Utility Data

- meter IDs
- billing periods
- electricity usage
- tariffs
- cost fields

---

# Sample Data Design

The utility sample includes:
- billing periods
- meter IDs
- electricity usage

to simulate monthly facility reporting.

---

# 3 Corporate Travel Data

## Research

I researched travel platforms such as:
- Concur
- Navan

These systems expose:
- flights
- hotel bookings
- taxis
- airport/location codes

---

# Typical Travel Challenges

- missing distances
- multiple transport categories
- inconsistent location formats

---

# Sample Data Design

The travel sample includes:
- airport codes
- travel categories
- source/destination locations
- distances

to simulate employee business travel emissions.

---

# What Would Break in Production

## SAP
- multilingual column names
- inconsistent schemas
- custom enterprise mappings

## Utility
- PDF parsing inconsistencies
- timezone handling
- missing billing periods

## Travel
- missing airport mappings
- duplicate trips
- incomplete itinerary data