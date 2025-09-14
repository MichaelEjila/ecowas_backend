ECOWAS Backend API

Django REST Framework backend for the ECOWAS website, providing APIs for Members, Gallery, “Did You Know,” Member States, Contact Info, and user management with role-based access control.

Features

JWT Authentication

Role-based access: Admin / Editor / Viewer

CRUD APIs for Members, Did You Know, Gallery, Member States, Contact Info

Stats endpoint /api/stats/

Green-themed Django admin dashboard

Setup
# Clone repo
git clone <repo-url>
cd <repo-folder>

# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Initialize user roles
python manage.py init_roles

# Run server
python manage.py runserver

API Endpoints

Auth: /api/auth/token/, /api/auth/token/refresh/

Users (Admin): /api/users/

Members: /api/members/

Did You Know: /api/didyouknow/

Gallery: /api/gallery/sections/, /api/gallery/images/, /api/gallery/videos/

Member States: /api/memberstates/

Contact Info: /api/contactinfo/

Stats: /api/stats/

Admin Dashboard

URL: /admin/

Green-themed via django-admin-interface

Manage all models: User, Member, DidYouKnow, Gallery, MemberState, ContactInfo
