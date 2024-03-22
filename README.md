# Simple Phonebook

### Overview

This is a simple phonebook web app created with Django framework.

### Features:
- User registration and login functionality
- Add, edit, and delete contacts
- User authentication and authorization

### Installation:
1. Clone this repository:
   ```
   git clone https://github.com/mobinbanikarim/django_phonebook.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```
   python manage.py migrate
   ```

4. Start the development server:
   ```
   python manage.py runserver
   ```

5. Access the web app at `http://127.0.0.1:8000/`

### URLs:
- Home (Contacts): `/`
- Add Contact: `/new-contacts/`
- Edit Contact: `/edit-contact/<CONTACT ID>`
- Delete Contact: `/delete-contact/<CONTACT ID>`
- Admin Panel: `/admin/`
- Login: `/login/`
- Logout: `/logout/`
- Register: `/register/`


## Login Detail
superuser: admin

pass: admin

## GitHub
- [MobinBanikarim](https://github.com/mobinbanikarim/django_phonebook)