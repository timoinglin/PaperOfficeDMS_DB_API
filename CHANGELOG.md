# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), 
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-11-27
### Added
- **Core Features**:
  - Ability to retrieve documents with pagination, search by name, and fetch individual documents by ID.
  - OCR data retrieval for documents, supporting multiple pages per document.
  - Access to categories (folders) with pagination support.
  - Retrieval of contact information and PaperOfficeDMS accounts with pagination and ID-based queries.
- **Authentication**:
  - Secured API endpoints with Bearer token authentication.
- **Configuration**:
  - Flexible configuration using `config.ini` for database and server settings.
  - Authentication token setup for secure access.
- **API Documentation**:
  - Interactive Swagger UI at `/docs` and ReDoc at `/redoc`.
- **Developer Features**:
  - Python-based API built on FastAPI.
  - SQLAlchemy integration with MySQL/MariaDB connectors for database interaction.
- **Installation Instructions**:
  - Detailed setup guide for creating a virtual environment and configuring the API.

---

## How to Use This Changelog

- **Added**: New features introduced.
- **Changed**: Updates or improvements to existing features.
- **Deprecated**: Features that will be removed in future releases.
- **Removed**: Features removed from this version.
- **Fixed**: Bug fixes.
- **Security**: Security updates.
