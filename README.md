# Invoice Reconciliation Backend

A backend service that matches uploaded invoices with payments from multiple sources.  
It resolves partial payments, split payments, mismatched names, and multi-channel transactions using rule based matching and fuzzy logic.

## Problem

Businesses receive payments through bank transfers, UPI, cash, and other channels.  
Amounts rarely match exactly.  
Names differ across sources.  
Customers often pay partially or split the amount across multiple methods.

Manual reconciliation takes hours and still introduces errors.

## Solution

This backend automates reconciliation by:

- Accepting invoices (CSV/JSON)
- Accepting payments (bank statements, cash entries, UPI logs)
- Matching payments to invoices using:
  - Exact amount rules
  - Partial payments
  - Split payments across multiple sources
  - Fuzzy name matching
  - Date proximity logic
- Returning a reconciliation summary with statuses:
  - **Paid**
  - **Partially Paid**
  - **Pending**
  - **Overpaid**

## Features (Backend)

- FastAPI REST API
- Invoice ingestion endpoint
- Payment ingestion endpoint
- Matching engine:
  - Exact match
  - Partial match
  - Multi source match
  - Fuzzy name match
- Reconciliation summary endpoint
- PostgreSQL database
- Docker support
- Modular service architecture

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pandas
- rapidfuzz (for fuzzy matching)
- Docker

<!-- ## High Level Architecture -->


<!-- ## API Endpoints (Planned)

- `POST /invoices/upload`
- `POST /payments/upload`
- `POST /reconcile`
- `GET /summary` -->
