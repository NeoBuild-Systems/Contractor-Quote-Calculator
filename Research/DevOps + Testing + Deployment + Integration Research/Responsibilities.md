- Enable automatic branch deletion after merge

---

## 3. Containerization (Docker)

**Goal:** Make the system reproducible and easy to run anywhere.

### Tasks
- Create Dockerfile for:
- Java backend
- Python scraper
- Create `docker-compose.yml` to run:
- Backend service
- Scraper service
- MySQL database
- MongoDB database (optional)

---

## 4. Testing Infrastructure

### Backend (Java)
- JUnit tests for:
- Quote and calculation logic
- Integration tests for:
- REST APIs
- Optional:
- Test database using Testcontainers

### Python Scraper
- PyTest tests for scraper functions
- Mock HTML responses
- Validate parsing and extraction logic

### End-to-End Testing
- Create Postman test collection
- Run Postman tests in CI using `newman`

---

## 5. Deployment

**Goal:** Ensure the application runs reliably in staging or production.

### Tasks
- Set up a staging environment (local or cloud)
- Create and manage `.env` files
- Store secrets using GitHub Secrets
- Ensure all services run together without crashing

### Possible Deployment Targets
- Local Docker stack
- Railway.app (free tier)
- Render.com
- VPS (low-cost option)

---

## 6. Monitoring & Logging

**Goal:** Observe system health and detect issues early.

### Tasks
- Centralize logs using Docker logging
- Optional: Set up Grafana dashboard to monitor
- Scraper execution frequency
- API request count
- Database usage

---

## 7. Cross-Team Integration & Support

**Goal:** Ensure all system components work together smoothly.

### Responsibilities
- Ensure scraper pushes updated prices into the database
- Ensure backend APIs read from the database correctly
- Ensure frontend can communicate with backend
- Configure CORS and network access correctly
- Assist in resolving merge conflicts across teams

---

## Ownership Summary

This role owns:
- CI/CD reliability
- Test enforcement
- Deployment stability
- Docker infrastructure
- Integration sanity across teams
