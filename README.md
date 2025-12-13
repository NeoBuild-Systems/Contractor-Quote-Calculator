# Contractor-Quote-Calculator

# Contractor Quote Calculator  
_A full-stack system for generating professional construction quotes with live price updates._

---

## Overview  
The Contractor Quote Calculator is a multi-technology project designed to help contractors quickly generate accurate, professional quotes.  
It includes:

- Java backend for calculations and business logic  
- Python scraper for live material cost updates  
- REST API layer for communication  
- Web/desktop frontend for contractors  
- PDF generation for client-ready quotes  

---

## Features  
### Core  
- Material + labour cost calculator  
- Automatic markup + VAT calculations  
- Saved items library  
- Quote templates  
- Multi-supplier price comparison  
- PDF export

### ✔Scraper  
- Pulls live pricing from supported stores  
- Stores historical pricing  
- Scheduled scraping  

###  Frontend  
- Web app for quoting workflow  
- Optional desktop version (Electron)

---

## Tech Stack  
### **Backend (Java)**  
- Spring Boot  
- JPA / Hibernate  
- MySQL or MongoDB  
- Apache PDFBox / iText  

### **Scraper (Python)**  
- BeautifulSoup4  
- Requests  
- Selenium (if JS rendering required)

### **Frontend**  
- React / Next.js  
- Tailwind or Material UI  

### **Deployment**  
- Docker  
- GitHub Actions CI/CD  

### **📂 Project File Structure**
Contractor-Quote-Calculator/
│
├── backend/
│   └── java/
│       ├── src/
│       │   ├── main/java/
│       │   │   ├── controller/
│       │   │   ├── service/
│       │   │   ├── repository/
│       │   │   └── model/
│       │   └── test/java/
│       ├── build.gradle / pom.xml
│       └── checkstyle.xml
│
├── scraper/
│   └── scraper-python/
│       ├── src/
│       │   ├── scrapers/
│       │   ├── parsers/
│       │   └── scheduler/
│       ├── tests/
│       ├── requirements.txt
│       └── main.py
│
├── frontend/
│   └── javafx/
│       ├── controllers/
│       ├── views/
│       ├── models/
│       └── Main.java
│
├── database/
│   ├── schema.sql
│   ├── seed-data.sql
│   └── erd-diagram.png
│
├── Research/
│   ├── person1/
│   ├── person2/
│   ├── person3/
│   ├── person4/
│   └── person5/
│
├── Tests/
│   ├── api/
│   └── integration/
│
├── .github/
│   ├── CODEOWNERS
│   ├── CONTRIBUTING.md
│   ├── pull_request_template.md
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── workflows/
│       └── ci.yml
│
├── .gitignore
├── docker-compose.yml
├── LICENSE
└── README.md



---

 
