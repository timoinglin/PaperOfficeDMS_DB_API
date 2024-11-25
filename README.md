# PaperOfficeDMS Database API


A FastAPI application for retrieving data from the PaperOfficeDMS database. This API provides endpoints to access categories, documents, contacts, accounts, and OCR data from the PaperOfficeDMS DB. It is designed for informational purposes and to facilitate integration with other software.

**Note:** This is not an official API for PaperOfficeDMS.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [Categories](#categories)
  - [Documents](#documents)
  - [Documents OCR](#documents-ocr)
  - [Contacts](#contacts)
  - [Accounts](#accounts)
- [API Documentation](#api-documentation)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

---

## Features

- **Retrieve Documents**: Fetch documents with pagination, search by name and retrieve individual documents by ID.
- **Access OCR Data**: Retrieve OCR text data for documents, supporting multiple pages per document.
- **Retrieve Categories**: Access categories (folders) displayed in the PaperOfficeDMS UI with pagination support.
- **Access Contacts and Accounts**: Retrieve information about contacts and PaperOfficeDMS accounts.
- **Authentication**: Secure API endpoints using Bearer token authentication.
- **Configurable Settings**: Easily configure database and server settings via a `config.ini` file.

## Requirements

- **Python 3.7 or higher**
- **Access to the PaperOfficeDMS Database Server**
  - Ensure that you have network access to the database server.
  - Database credentials with sufficient permissions for read operations.
- **MySQL/MariaDB Connector**
  - The application uses SQLAlchemy with a MySQL connector to interact with the database.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/timoinglin/PaperOfficeDMS_DB_API.git
   cd PaperOfficeDMS_DB_API
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - On **macOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

4. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Configure Database and Server Settings**

   Edit the `config.ini` file to include your database credentials and server configurations.

   ```ini
   [database]
   host = localhost
   port = 3306
   username = your_db_username
   password = your_db_password
   database_name = your_PaperOffice_database_name

   [server]
   host = 0.0.0.0
   port = 8000
   development = true

   [auth]
   token = your_secure_token
   ```

   - **Database Section**: Replace `your_db_username`, `your_db_password`, and `your_PaperOffice_database_name` with your actual database credentials.
   - **Server Section**: Adjust the `host` and `port` if necessary.
   - **Auth Section**: Set `token` to a secure value that will be used for Bearer token authentication.

2. **Ensure Database Access**

   - Verify that the machine running the API has network access to the database server.
   - Confirm that the provided database credentials have sufficient permissions for read operations.

## Usage

1. **Start the API Server**

   ```bash
   python main.py
   ```

   - The server will start using the host and port specified in the `config.ini` file.
   - If `development` is set to `true`, the server will run with automatic reload enabled.

2. **Access the API**

   - Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the Swagger UI documentation.
   - Visit [http://localhost:8000/redoc](http://localhost:8000/redoc) for ReDoc documentation.

3. **Make API Requests**

   - All endpoints require authentication via Bearer token.
   - Include the token specified in the `config.ini` file in the `Authorization` header.

   **Example using `curl`:**

   ```bash
   curl -X GET "http://localhost:8000/categories/?limit=10&offset=0" -H "Authorization: Bearer your_secure_token"
   ```

   **Example using Python `requests` library:**

   ```python
   import requests

   headers = {
       "Authorization": "Bearer your_secure_token"
   }

   response = requests.get("http://localhost:8000/categories/?limit=10&offset=0", headers=headers)
   data = response.json()
   print(data)
   ```

## API Endpoints

### Authentication

- **All requests must include the `Authorization` header with the Bearer token specified in your `config.ini` file.**

```http
Authorization: Bearer your_secure_token
```

**Example with Headers:**

```bash
curl -X GET "http://localhost:8000/documents/?name=contract" \
     -H "Authorization: Bearer your_secure_token"
```

### Categories

- **GET** `/categories/`

  - Retrieve a list of categories with pagination.
  - **Query Parameters:**
    - `limit` (int): Number of categories to return. Default is 10.
    - `offset` (int): Number of categories to skip. Default is 0.

- **GET** `/categories/{category_id}`

  - Retrieve a category by its ID.


### Documents

- **GET** `/documents/`

  - Retrieve a list of documents with pagination. Optionally search for documents by name.
  - **Query Parameters:**
    - `limit` (int): Number of documents to return. Default is 10.
    - `offset` (int): Number of documents to skip. Default is 0.
    - `name` (str, optional): A string to search for in document names.

  **Example Requests:**

  - **Retrieve all documents with default pagination:**

    ```bash
    curl -X GET "http://localhost:8000/documents/" -H "Authorization: Bearer your_secure_token"
    ```

  - **Retrieve documents with custom pagination:**

    ```bash
    curl -X GET "http://localhost:8000/documents/?limit=20&offset=40" -H "Authorization: Bearer your_secure_token"
    ```

  - **Search for documents by name:**

    ```bash
    curl -X GET "http://localhost:8000/documents/?name=invoice" -H "Authorization: Bearer your_secure_token"
    ```

  - **Search for documents by name with pagination:**

    ```bash
    curl -X GET "http://localhost:8000/documents/?name=report&limit=5&offset=10" -H "Authorization: Bearer your_secure_token"
    ```

  **Notes:**

  - The `name` parameter allows you to search for documents whose names contain the specified string. The search is case-insensitive.
  - If `name` is not provided, the endpoint returns all documents according to the pagination parameters.

- **GET** `/documents/{document_id}`

  - Retrieve a document by its ID.
  - **Path Parameters:**
    - `document_id` (int): The ID of the document to retrieve.

  **Example Request:**

  ```bash
  curl -X GET "http://localhost:8000/documents/123" -H "Authorization: Bearer your_secure_token"
  ```

  **Notes:**

  - Replace `123` with the actual document ID you wish to retrieve.
  - If the document with the specified ID does not exist, a `404 Not Found` error is returned.


### Documents OCR

- **GET** `/documents_ocr/{document_id}`

  - Retrieve OCR data for a specific document.
  - Returns all OCR entries associated with the document ID (supports multiple pages).

### Contacts

- **GET** `/contacts/`

  - Retrieve a list of contacts with pagination.
  - **Query Parameters:**
    - `limit` (int): Number of contacts to return. Default is 10.
    - `offset` (int): Number of contacts to skip. Default is 0.

- **GET** `/contacts/{contact_id}`

  - Retrieve a contact by its ID.

### Accounts

- **GET** `/accounts/`

  - Retrieve a list of PaperOfficeDMS accounts with pagination.
  - **Query Parameters:**
    - `limit` (int): Number of accounts to return. Default is 10.
    - `offset` (int): Number of accounts to skip. Default is 0.

- **GET** `/accounts/{account_id}`

  - Retrieve an account by its ID.


## API Documentation

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

The API documentation provides detailed information about each endpoint, including parameters, responses, and example requests.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This is **not** an official API for PaperOfficeDMS. It is an independent project intended for retrieving data from the PaperOfficeDMS database for informational purposes and integration with other software. Use it at your own risk.

For more information:
- Official PaperOffice Website: https://www.paperoffice.com/
- Official PaperOffice API Documentation: https://help.paperoffice.com/articles/category/automation-api_interface

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

   Click the "Fork" button at the top right corner of this page to create a copy of this repository under your GitHub account.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/timoinglin/PaperOfficeDMS_DB_API.git
   cd PaperOfficeDMS_DB_API
   ```

3. **Create a Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes**

   Implement your feature or bug fix.

5. **Commit and Push**

   ```bash
   git add .
   git commit -m "Add your commit message here"
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**

   Open a pull request on the original repository to merge your changes.

## Acknowledgments

- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **SQLAlchemy**: A powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Uvicorn**: A lightning-fast ASGI server implementation for Python.
- **PaperOfficeDMS**: The database schema is based on the PaperOfficeDMS DB.

---

**Note:** Ensure that you comply with all applicable licenses and terms of service when accessing and using data from the PaperOfficeDMS database.

If you have any questions or need assistance, feel free to open an issue or contact the repository maintainers.