# Backend Technical Assessment
## Introduction
This is a simple backend application that provides a RESTful API for validating Egyptian National Id numbers, and extract possible data from the Id number such:
- Birth Date
- Birth Governerate
- Birth Date Unique Serial Number
- Gender

## Technologies
- Python 3.11
- FastAPI
- Pydantic
- Uvicorn
- Docker

## How to run the application
### Setup Repo
1. Clone the repository
```bash
git clone git@github.com:abd0123/shahry-task.git
```
2. Navigate to the project directory
```bash
cd shahry-task
```


### Running the application using Docker
1. Run the following command to build the docker image
```bash
docker build -t validate-nid .
```
2. Run the following command to run the docker container
```bash
docker run -it -p 8000:8000 validate-nid
```
5. The application should be running on http://localhost:8000


### Running the application using Uvicorn
1. Run the following command to install the required dependencies
```bash
pip install -r requirements.txt
```
2. Run the following command to start the application
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
5. The application should be running on http://localhost:8000

#### Note
- You need python 3.11 installed on your machine to run the application (Feel free to create virtual environment)

## API Endpoint
### Description

This endpoint validates a given national ID and extracts information such as birth date, birth governorate, serial number, and gender.

### URL
``
POST /validate-nid
``
### Request Body
```json
{
  "national_id": "29001011234567"
}
```
#### Fields
- national_id: The national ID to be validated and decomposed.

### Responses
#### Valid National ID
**Status Code: ``200 OK``**
```json
{
  "valid": true,
  "data": {
    "birth_date": "1990-01-01",
    "birth_governerate": "Dakahlia",
    "birth_date_serial": "3456",
    "gender": "Female"
  }
}
```

#### Invalid National ID
**Status Code: ``200 OK``**
```json
{
  "valid": false,
  "message": "Invalid National ID"
}
```
The message should be discriptive enough to explain why the national ID is invalid.

## Logic
The application uses the following logic to validate and extract information from the national ID:
1. Check if the national ID is all digits.
2. Check if the national ID is 14 digits long.
3. Check if the first 7 digits represent a valid birth date, and extracts it.
   1. digit 1 is century digit (2 for 20th century, 3 for 21st century)
   2. digits 2-3 birth year
   3. digits 4-5 birth month
   4. digits 6-7 birth day
4. Check if the next 3 digits represent a valid governorate code, and extracts the governorate name.
5. Check if the 13th digit is not 0, and based on whether it is odd (1, 3, 5, 7) or even (2, 4, 6, 8) extracts the gender as ``Male`` or ``Female`` respectively.
6. Extract the digits 10-13 as the unique serial number for this person on this birth date in this governorate.
7. If all the above checks pass, the national ID is considered valid, and the extracted information is returned.
8. If any of the checks fail, the national ID is considered invalid, and an appropriate message is returned.