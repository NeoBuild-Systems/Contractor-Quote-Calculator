# Contractor Quote Calculator

## Rough Outline

A construction-focused application designed to help contractors create accurate, professional quotes more efficiently.

The long-term goal is to combine **quote building, construction pricing, material data, CAD-based quantity takeoffs, and automated price updates** into one system.

---

## Project Structure

```text
contractor-quote-calculator/
│
├── README.md
├── .gitignore
├── LICENSE
│
├── research/
│   │
│   ├── market/
│   │   ├── competitors/
│   │   │   ├── competitor-comparison.md
│   │   │   ├── buildxact.md
│   │   │   ├── joist.md
│   │   │   ├── tradify.md
│   │   │   ├── buildertrend.md
│   │   │   └── kwikquote.md
│   │   │
│   │   ├── contractors/
│   │   │   ├── contractor-workflow.md
│   │   │   ├── pain-points.md
│   │   │   ├── interview-questions.md
│   │   │   └── interview-results.md
│   │   │
│   │   ├── construction/
│   │   │   ├── common-job-types.md
│   │   │   ├── materials.md
│   │   │   ├── labour.md
│   │   │   └── equipment.md
│   │   │
│   │   ├── pricing/
│   │   │   ├── competitor-pricing.md
│   │   │   ├── customer-pricing.md
│   │   │   └── proposed-pricing.md
│   │   │
│   │   └── legal/
│   │       ├── quote-requirements.md
│   │       ├── vat-requirements.md
│   │       └── terms-and-conditions.md
│   │
│   └── technical/
│       ├── architecture/
│       │   ├── system-architecture.md
│       │   ├── java-vs-python.md
│       │   └── technology-decisions.md
│       │
│       ├── backend/
│       │   ├── spring-boot.md
│       │   ├── rest-api.md
│       │   ├── json-handling.md
│       │   └── authentication.md
│       │
│       ├── database/
│       │   ├── mysql-vs-nosql.md
│       │   ├── database-design.md
│       │   ├── indexing.md
│       │   └── price-history-storage.md
│       │
│       ├── calculations/
│       │   ├── material-calculations.md
│       │   ├── labour-calculations.md
│       │   ├── markup.md
│       │   ├── vat.md
│       │   └── unit-conversions.md
│       │
│       ├── pdf/
│       │   ├── pdfbox-vs-itext.md
│       │   ├── quote-layout.md
│       │   └── pdf-generation.md
│       │
│       ├── scraping/
│       │   ├── scraping-methods.md
│       │   ├── java-vs-python-scraping.md
│       │   ├── html-structure.md
│       │   ├── scheduling.md
│       │   └── caching.md
│       │
│       ├── cad/
│       │   ├── autocad-workflow.md
│       │   ├── dwg-vs-dxf.md
│       │   ├── dxf-processing.md
│       │   └── quantity-takeoff.md
│       │
│       ├── frontend/
│       │   ├── frontend-options.md
│       │   ├── ui-ux-research.md
│       │   └── user-flow.md
│       │
│       └── testing/
│           ├── testing-strategy.md
│           ├── unit-testing.md
│           └── integration-testing.md
│
├── project-planning/
│   ├── project-scope.md
│   ├── mvp.md
│   ├── requirements.md
│   ├── user-stories.md
│   ├── feature-priority.md
│   ├── api-specification.md
│   ├── database-specification.md
│   ├── calculation-specification.md
│   ├── architecture.md
│   ├── ui-wireframes/
│   ├── diagrams/
│   │   ├── erd.png
│   │   ├── architecture.png
│   │   └── user-flow.png
│   └── decisions/
│       └── decision-log.md
│
├── backend/
│   └── spring-boot/
│
├── scraper/
│   └── python/
│
├── cad/
│   └── python/
│
├── frontend/
│
├── database/
│   ├── schema.sql
│   ├── seed.sql
│   └── migrations/
│
├── pdf/
│   └── templates/
│
└── tests/
    ├── backend/
    ├── scraper/
    ├── cad/
    └── integration/
```

---

## Folder Overview

### `research/`

Contains all research completed before and during development.

#### `market/`

Research about the construction industry, contractors, competitors, pricing, and legal requirements.

* **competitors/** — Research on competing products and their features.
* **contractors/** — Contractor workflows, pain points, interviews, and user research.
* **construction/** — Common construction jobs, materials, labour, and equipment.
* **pricing/** — Competitor pricing, customer willingness to pay, and our proposed pricing.
* **legal/** — Legal and business requirements related to quotes and VAT.

#### `technical/`

Research into the technologies and technical problems involved in building the system.

* **architecture/** — Overall system design and technology decisions.
* **backend/** — Spring Boot, REST APIs, JSON, authentication, etc.
* **database/** — MySQL, NoSQL, schema design, indexing, and price history.
* **calculations/** — Construction estimating and quote calculation logic.
* **pdf/** — PDF generation and quote document design.
* **scraping/** — Web scraping, scheduling, caching, and price extraction.
* **cad/** — AutoCAD, DWG/DXF, drawing processing, and quantity takeoffs.
* **frontend/** — UI/UX and frontend technology research.
* **testing/** — Testing strategy and automated testing.

---

### `project-planning/`

Contains decisions and plans based on the research.

This is where we define **what we're actually going to build**.

Includes:

* Project scope
* MVP
* Requirements
* User stories
* Feature priorities
* API specification
* Database specification
* Calculation rules
* System architecture
* UI wireframes
* Diagrams
* Major project decisions

---

### `backend/`

Contains the main Java/Spring Boot application.

Responsible for:

* API
* Quote logic
* Database communication
* Users
* Clients
* Materials
* Labour
* Quotes
* PDF generation

---

### `scraper/`

Contains the Python scraping and price-data system.

Responsible for:

* Supplier price collection
* Product information
* Price updates
* Price history
* Data cleaning
* Scheduled scraping

---

### `cad/`

Contains CAD/drawing-related processing.

Potential responsibilities:

* DXF processing
* Drawing measurements
* Area calculations
* Length calculations
* Object counting
* Quantity takeoff

---

### `frontend/`

Contains the user-facing application.

Potential screens include:

* Dashboard
* Create Quote
* Materials
* Labour
* Clients
* Quote History
* Quote Preview
* CAD/Takeoff tools

---

### `database/`

Contains database setup and changes.

* `schema.sql` — Main database structure
* `seed.sql` — Test/default data
* `migrations/` — Database changes over time

---

### `pdf/`

Contains quote PDF templates and related PDF-generation resources.

---

### `tests/`

Contains testing for the different components.

* **backend/** — Java backend tests
* **scraper/** — Scraping tests
* **cad/** — CAD processing tests
* **integration/** — Tests between multiple components

---

## Development Direction

The project will be developed in stages.

### Phase 1 — MVP

Focus on:

* Materials
* Labour
* Quote creation
* Calculations
* Quote history
* PDF generation

### Phase 2 — Automated Pricing

Add:

* Supplier data
* Price scraping
* Price history
* Automatic material price updates

### Phase 3 — CAD / Quantity Takeoff

Add:

* DXF support
* Drawing measurements
* Area/length calculations
* Material quantity estimation

### Phase 4 — Advanced Features

Potential future features:

* Client management
* Team accounts
* Online quote approval
* Price alerts
* Advanced analytics
* Automated estimating
* More advanced CAD/takeoff features

---

## Development Principle

The project should be built **from simple to complex**.

The first goal is to create a reliable quote generator.

Scraping, CAD processing, automation, and advanced features should build on top of the core system rather than becoming dependencies for the MVP.

---

## Current Status

**Stage:** Research → Planning → Development

The immediate goal is to finish planning, finalize the MVP, confirm the architecture, and begin development.
