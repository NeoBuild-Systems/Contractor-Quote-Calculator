## Division of Labour

The project is being developed by **2 people**, with responsibilities split between the **core application** and the **data, scraping, and CAD systems**.

The goal is to keep responsibilities clear while still working together on major decisions and integration.

---

### 👤 Person 1 — Core Application & Backend

**Primary focus:** Build and maintain the main application.

#### Responsibilities

**Backend**

* Java
* Spring Boot
* REST API
* Business logic
* Quote calculations
* Authentication

**Database**

* MySQL
* Database structure
* Relationships
* Queries
* Migrations

**Quote System**

* Creating quotes
* Adding materials
* Adding labour
* Equipment costs
* Markup
* VAT
* Quote history

**PDF**

* PDF generation
* Quote templates
* Professional quote formatting

#### Main folders

```text
backend/
database/
pdf/
tests/backend/
```

---

### 👤 Person 2 — Data, Scraping, CAD & Frontend

**Primary focus:** Handle external construction data, CAD processing, and the user-facing side of the application.

#### Responsibilities

**Pricing & Data**

* Material pricing
* Supplier data
* Price history
* Data cleaning
* Unit conversions

**Web Scraping**

* Python
* Supplier price extraction
* Scraping schedules
* Caching
* Price updates
* Scraper testing

**CAD / Quantity Takeoff**

* AutoCAD workflow
* DXF processing
* Drawing measurements
* Area and length calculations
* Object counting
* Quantity takeoff

**Frontend / UI**

* User interface
* Quote creation workflow
* Material selection
* Quote preview
* CAD/takeoff interface

#### Main folders

```text
scraper/
cad/
frontend/
tests/scraper/
tests/cad/
```

---

## 🤝 Shared Responsibilities

Some parts of the project require both developers to work together.

### Product Decisions

* MVP scope
* Feature priorities
* User requirements
* Future features

### Architecture

* How the frontend communicates with the backend
* How Python communicates with Java
* Database decisions
* Data flow

### Testing

* Integration testing
* End-to-end testing
* Bug fixing
* Performance testing

### GitHub

* Pull request reviews
* Branch management
* Code standards
* Documentation
* Major architectural decisions

---

## 🔄 How the Two Parts Connect

The main system is expected to work approximately like this:

```text
                    FRONTEND
                       │
                       ↓
                JAVA SPRING BOOT
                       │
             ┌─────────┴─────────┐
             ↓                   ↓
          MySQL              PDF SYSTEM
             ↑
             │
      ┌──────┴───────┐
      │              │
 Python Scraper   CAD Processing
      │              │
 Supplier Data    DXF Measurements
```

The Java backend acts as the **main application**, while Python handles specialized tasks such as scraping and CAD processing.

---

## 📌 Ownership Summary

| Area               | Person 1 | Person 2 |
| ------------------ | -------- | -------- |
| Java / Spring Boot | **Lead** | Support  |
| Backend            | **Lead** | Support  |
| MySQL              | **Lead** | Support  |
| Quote calculations | **Lead** | Support  |
| PDF generation     | **Lead** | Support  |
| Python             | Support  | **Lead** |
| Web scraping       | Support  | **Lead** |
| Price data         | Support  | **Lead** |
| CAD / DXF          | Support  | **Lead** |
| Frontend           | Support  | **Lead** |
| Testing            | **Both** | **Both** |
| Product decisions  | **Both** | **Both** |
| Architecture       | **Both** | **Both** |

### General Rule

Each major area has **one primary owner**, but neither person works completely independently. The owner is responsible for implementation, while the other developer reviews, tests, and assists when needed.
