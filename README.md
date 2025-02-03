# Clinic Management System

A comprehensive clinic management system designed to manage doctor and patient information. The system allows administrators to add and remove doctors, store patient history, and provides search functionality for quick access to records.

## Features

- **Doctor Management:**
  - Add new doctors to the system.
  - Remove doctors from the system when needed.
  - Store doctor details such as name, specialization, contact information, and availability.

- **Patient History Management:**
  - Store patient details including personal information, medical history, and current treatments.
  - Maintain a history of past appointments, diagnoses, and prescriptions.

- **Search Functionality:**
  - Quickly search for doctors by name, specialization, or contact details.
  - Search for patients by name or ID and view their medical history.

- **User Authentication (Admin Role):**
  - Only authorized admins can add or remove doctors and manage patient records.

## Technologies Used

- **Frontend:**
  - [HTML5](https://html.spec.whatwg.org/)
  - [CSS3](https://www.w3.org/Style/CSS/)
  - [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  
- **Backend:**
  - [Python](https://www.python.org/) with [Django](https://www.djangoproject.com/) for backend development.
  - [SQLite](https://www.sqlite.org/) for database management (can be replaced with other DB systems).

- **User Authentication:**
  - [Django Authentication](https://docs.djangoproject.com/en/stable/topics/auth/)

## Features Overview

### 1. Doctor Management
- Admins can add doctors with details like:
  - Full Name
  - Specialization (e.g., Cardiologist, Pediatrician, etc.)
  - Contact Information (Phone, Email)
  - Availability (Timings, Days of the week)

- Admins can remove doctors from the system.

### 2. Patient History Management
- Patient profiles include:
  - Personal Details (Name, Age, Gender, Address, etc.)
  - Medical History (Previous treatments, conditions)
  - Current and Past Appointments with doctors
  - Diagnoses and Prescriptions

### 3. Search Functionality
- **Doctor Search**: Users can search for doctors by:
  - Name
  - Specialization
  - Availability

- **Patient Search**: Users can search for patients by:
  - Name
  - Patient ID
  - Medical History

### 4. User Authentication
- Admins have secure login to manage the system.
- Only authenticated admins can add/remove doctors and access/edit patient history.

## Getting Started

### 1. Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/yourusername/clinic-management-system.git
cd clinic-management-system
```

### 2. Set up the Environment

#### Install Dependencies

Ensure you have Python installed on your system. You can check if Python is installed by running:

```bash
python --version
```

Install the necessary Python packages using pip:

```bash
pip install -r requirements.txt
```

This will install the required packages for Django, SQLite, and any other dependencies.

### 3. Database Setup

- Run migrations to set up the database schema:

```bash
python manage.py migrate
```

### 4. Create a Superuser

To access the admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up an admin username, email, and password.

### 5. Run the Development Server

Start the development server:

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000/` in your browser.

### 6. Admin Panel Access

To access the admin panel and manage doctors and patients, visit:

```
http://127.0.0.1:8000/admin
```

Log in with the superuser credentials you created earlier.

## Usage

1. **Login**: As an admin, log into the admin panel.
2. **Add Doctor**: Navigate to the "Doctor" section in the admin panel to add new doctors.
3. **Remove Doctor**: Select a doctor and remove their information if they are no longer part of the clinic.
4. **Add Patient**: Add new patients and record their medical history, current treatments, and appointments.
5. **Search for Doctors and Patients**: Use the search feature to find doctors or patients quickly based on their names, specialization, or medical history.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push the branch to your fork (`git push origin feature-name`).
5. Submit a pull request.
