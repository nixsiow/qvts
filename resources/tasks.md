# Project Tasks

## Task 1: Set Up the Django Project

- [x] **Create a new Django project**
  - [x] Initialize a new Django project and set up the basic configuration.
- [x] **Create a new Django app**
  - [x] Create a new apps within the project to handle the ship and harbour management.

## Task 2: Implement Models

- [x] **Create the User model**
  - [x] Define the model for users with appropriate fields to represent the users of the system.
- [x] **Create the ContactPerson model**
  - [x] Define the model for contact persons with appropriate fields to model the contact details of a operating company.
- [x] **Create the OperatingCompany model**
  - [x] Define the model for operating companies with appropriate fields to represent the ship operating companies.
- [x] **Create the Ship model**
  - [x] Define the model for ships with appropriate fields and relationships to represent the ships.
- [x] **Create the Location model**
  - [x] Define the model for locations with appropriate fields to represent locations of harbours.
- [x] **Create the Harbour model**
  - [x] Define the model for harbours with appropriate fields.
- [x] **Create the ShipMovement model**
  - [x] Define the model to track ship movements in and out of harbours.
- [x] **Create the VTSCentre model**
  - [x] Define the model for Vessel Traffic Service (VTS) centres with appropriate fields to represent the centres.
- [x] **Create the Operator model**
  - [x] Define the model for operators with appropriate fields to represent the operators of VTS centres.

## Task 3: Set Up Django Admin

- [x] **Register User model in admin**
  - [x] Customize the admin interface for users.
- [x] **Register ContactPerson model in admin**
  - [x] Customize the admin interface for contact persons.
- [x] **Register OperatingCompany model in admin**
  - [x] Customize the admin interface for operating companies.
- [x] **Register Ship model in admin**
  - [x] Customize the admin interface for ships.
- [x] **Register Location model in admin**
  - [x] Customize the admin interface for locations.
- [x] **Register Harbour model in admin**
  - [x] Customize the admin interface for harbours.
- [x] **Register ShipMovement model in admin**
  - [x] Customize the admin interface for ship movements.
- [x] **Register VTSCentre model in admin**
  - [x] Customize the admin interface for VTS centres.
- [x] **Register Operator model in admin**
  - [x] Customize the admin interface for operators.

## Task 4: Develop REST Endpoints for CRUD Operations

- [x] **Create API endpoint to add a new ship**
  - [x] Implement the endpoint to create a new ship record.
- [x] **Create API endpoint to add a new harbour**
  - [x] Implement the endpoint to create a new harbour.
- [x] **Create API endpoint to record ship entry to harbour**
  - [x] Implement the endpoint to record the date and time when a ship enters a harbour.
- [x] **Create API endpoint to record ship exit from harbour**
  - [x] Implement the endpoint to record the date and time when a ship leaves a harbour.
- [x] **Create API endpoint to update ship details**
  - [x] Implement the endpoint to update the details of an existing ship.

## Task 5: Develop REST Endpoints for Data Retrieval

- [x] **Create API endpoint to list all ships**
  - [x] Implement the endpoint to list all ships, including their details and age.
- [x] **Create API endpoint to list all harbours**
  - [x] Implement the endpoint to list all harbours with limited details (id, name, maximum berth depth).
- [x] **Create API endpoint to get harbour details**
  - [x] Implement the endpoint to get detailed information about a specific harbour, including ships currently in the harbour.
- [x] **Create API endpoint to get ship's harbour visits**
  - [x] Implement the endpoint to get details about all the harbours a particular ship has visited, including entry and exit times.

## Task 6: Implement Bonus Features

- [ ] **Add search functionality for ships**
  - [ ] Implement a system to search for ships by name.
- [ ] **Add filtering functionality for ships by type**
  - [ ] Implement filtering options for ships by type.
- [x] **Protect endpoints with token-based authentication**
  - [x] Secure the API endpoints using token-based authentication.
- [x] **Create OpenAPI (Swagger) documentation**
  - [x] Generate API documentation using OpenAPI.

## Task 7: Write Unit Tests

- [ ] **Write tests for models**
  - [ ] Create unit tests to ensure the models are working as expected.
- [ ] **Write tests for API endpoints**
  - [ ] Create unit tests to ensure the API endpoints are working as expected.

## Task 8: Dockerize the Application

- [x] **Create a Dockerfile**
  - [x] Write a Dockerfile to containerize the Django application.
- [x] **Create a docker-compose file**
  - [x] Set up a `docker-compose.yml` file to run the application and any required services (e.g., database).

## Task 9: Documentation and Setup Instructions

- [x] **Write a README file**
  - [x] Include instructions on how to set up, run, and test the application.
- [x] **Provide setup and deployment instructions**
  - [x] Ensure the README file includes steps to build and run the Docker container.

## Task 10: Code Submission

- [x] **Push the code to a Git repository**
  - [x] Ensure all code and documentation are pushed to a public or private Git repository.
