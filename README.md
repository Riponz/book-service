# Book Rental Microservice
[Live Demo](https://bookrental-murex.vercel.app)

---


## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Key Features](#key-features)

---

## Introduction

This project is a simple microservice-based Book Rental System built with FastAPI. It consists of two independent services:

    📘 Book Service: Manages books with full CRUD operations.

    👤 User Service: Manages users and their rental history, with the ability to rent books by communicating with the Book Service via REST APIs.

---

## Technologies Used

- **Frontend:** React
- **Backend:** FastAPI

---

## Installation

Provide step-by-step instructions on how to set up and run the project locally.

1. Clone the repository:
   ```bash
   git clone https://github.com/Riponz/book-service.git
   ```

2. Navigate to the admin directory:
  ```bash
  cd admin

  npm install
  
  npm run dev
  ```
3. Navigate to the frontend directory:
```bash
  cd front-end

  npm install
  
  npm run dev
  ```
4. To run the backend services either you can run it individually or use docker:
```bash
docker compose up --build
  ```

---



##Key Features

Create, read, update, and delete books and users

Input validation using Pydantic

Separate databases for each service (simulating true microservices)

Error handling and inter-service communication

JWT authentication and Docker support
