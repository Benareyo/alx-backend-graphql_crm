# ALX Backend GraphQL CRM

A **Customer Relationship Management (CRM)** backend powered by **GraphQL**.  
This project is part of the **ALX Software Engineering Backend track**, focusing on building modern, efficient APIs that go beyond REST.

---

## 📝 Project Overview

This repository demonstrates how to design and implement a **GraphQL backend service** for a CRM system.  
Instead of multiple REST endpoints, GraphQL provides a **single entry point** for flexible and efficient data access.

With this project, we:

- Build a **GraphQL schema** to handle customers, products, and orders.  
- Implement **queries and mutations** for seamless interaction.  
- Use **Django** as the backend framework with **SQLite** as the database.  
- Explore how **GraphQL improves efficiency** and developer experience in API design.  

---

## 🛠 Tech Stack

- **Python 3**  
- **Django**  
- **Graphene-Django** (GraphQL for Django)  
- **SQLite3** (default DB)  

---

## ✨ Key Features

- **GraphQL Queries** – Retrieve customer and order data flexibly.  
- **GraphQL Mutations** – Add, update, or delete customers and products.  
- **Single API Endpoint** – No more juggling multiple REST endpoints.  
- **Scalable Structure** – Easy to extend with more models and features.  

---

## 🔍 Example GraphQL Usage

### Query all customers with their orders
```graphql
{
  allCustomers {
    id
    name
    email
    orders {
      id
      product
      amount
    }
  }
}
Add a new customer
mutation {
  createCustomer(name: "John Doe", email: "john@example.com") {
    customer {
      id
      name
      email
    }
  }
}

💡 Why GraphQL?

Unlike REST, GraphQL allows the client to ask for exactly what it needs, reducing problems of over-fetching and under-fetching.
This makes it perfect for CRM systems, where data relationships are rich and queries need flexibility.

📌 About

This project was built as part of the ALX Backend Specialization.
It highlights modern API design principles while reinforcing backend development skills with Django and GraphQL.
