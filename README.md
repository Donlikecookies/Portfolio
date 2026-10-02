# Personal Portfolio & Management System (Django)

This repository contains a semester-long personal portfolio project, updated progressively through Quiz 1 to Quiz 6. It features a public-facing portfolio, dynamic project displays, inquiry forms, user testimonies, and a secure superuser-only management dashboard.

---

## Features & Highlights

- **Custom Woody/Academic Styling:** Fully customized frontend aesthetics paired with a tailored Django admin/dashboard theme.
- **Superuser-Only Authentication:** Custom sign-in security ensuring only authorized superusers can access management views.
- **Dynamic Management Dashboard:** Dedicated views to list, view, and create Projects and Tech Stacks dynamically.
- **Relational Data Management:** Tech stacks can be linked to multiple projects without duplication.
- **Cloud Deployment:** Live production deployment configured on PythonAnywhere.

---

## Prerequisites

Ensure you have the following installed on your local machine before getting started:
- **Python** (version 3.10 or higher recommended)
- **Git**

---

## Environment Variables Configuration

This project utilizes environment variables to protect sensitive configuration details. 

1. Locate the `.env.example` file in the root directory.
2. Create a copy of it and name the new file **`.env`**.
3. Update the values inside your `.env` file for your environment:

```env
SECRET_KEY=your_unique_secure_secret_key_here
DEBUG=True

Clone the Repository 
# 1. Clone the repository and navigate into the folder
git clone [https://github.com/donlikecookies/Portfolio.git](https://github.com/donlikecookies/Portfolio.git)
cd Portfolio

# 2. Set up and activate your virtual environment
python -m venv venv
# On macOS / Linux:
source venv/bin/activate
# On Windows (PowerShell / CMD):
# venv\Scripts\activate

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Run database migrations
python manage.py migrate

# 5. Create a superuser account for dashboard access
python manage.py createsuperuser

# 6. Start the local development server
python manage.py runserver
