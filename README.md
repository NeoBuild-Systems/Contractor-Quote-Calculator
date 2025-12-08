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

---

 
