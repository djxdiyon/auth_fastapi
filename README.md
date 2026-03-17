# FastAPI Auth API

A simple authentication API built with FastAPI, SQLAlchemy, SQLite, JWT, and bcrypt password hashing.

## Features

- User registration
- User login
- JWT access tokens
- Protected `/me` route
- Password hashing with bcrypt

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Passlib
- Python-JOSE

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload