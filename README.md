
# portfolio-website
My personal portfolio website showcasing my skills, projects, experience, and contact information.
# Yaswanth Kumar — Portfolio (Full Stack)

Three pieces:

```
portfolio/    -> frontend  (HTML, CSS, JS) — the site itself
backend/      -> backend   (Django + Django REST Framework) — contact form API
database/     -> database  (raw MySQL schema, if you don't want to rely on Django's ORM)
```

## 1. Frontend

Nothing to install. Open `portfolio/index.html` in a browser, or serve it with
VS Code's "Live Server" extension. It's a static site — every section works
with no backend at all, except the contact form, which needs step 2.

**Your photo:** drop a square image into `portfolio/img/` (and `backend/static/img/`
if you're running the Django version) named `profile.jpg`. The hero section
already looks for it and will swap out the "YK" initials automatically —
no code changes needed.

**Project live demos:** the Projects section now links to two working demos:
- `portfolio/projects/focusnest/` — a functional task + habit tracker (saves to your browser's localStorage)
- `portfolio/projects/speed-controller/` — an animated simulation of the RF speed-zone system
Update the "GitHub" buttons on each project card with your real repo links whenever you push the code.

## 1b. Running everything as one Django app (recommended once the backend is set up)

Steps 2–3 below also make Django serve the frontend itself — so
`python manage.py runserver` gives you the whole site (pages + API + admin)
on one port, no separate server needed for the HTML. `backend/templates/`
and `backend/static/` already contain synced copies of the frontend for this.

## 2. Backend (Django + DRF)

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt

python manage.py migrate           # creates db.sqlite3 with the contact_message table
python manage.py createsuperuser   # so you can log in to /admin/ and read messages
python manage.py runserver         # starts everything at http://127.0.0.1:8000
```

With this running, `http://127.0.0.1:8000/` serves the portfolio itself
(Django renders `templates/index.html`), not just the API.

Endpoints:
- `POST /api/contact/` — used by the site's contact form (name, email, phone, subject, message)
- `GET /api/messages/` — lists all submissions (admin login required)
- `/admin/` — Django admin, the easiest place to read/manage submissions

With the server running, open `portfolio/index.html` and submit the contact
form — it POSTs straight to `http://127.0.0.1:8000/api/contact/`. If the
server isn't running, the form quietly falls back to opening an email draft
instead, so the form never dead-ends for a visitor.

## 3. Database

By default the backend uses **SQLite** (`backend/db.sqlite3`) — nothing to
install, it's created automatically by `migrate`.

If you'd rather use **MySQL**:
1. `pip install mysqlclient`
2. Run `database/schema.sql` in MySQL Workbench (or `mysql -u root -p < database/schema.sql`) to create `portfolio_db` and its table.
3. In `backend/config/settings.py`, swap the `DATABASES` block to the MySQL
   version shown in the comments right below it.
4. `python manage.py migrate` (Django will detect the table already exists,
   or you can skip this step since `schema.sql` already created it).

## Notes

- `CORS_ALLOW_ALL_ORIGINS = True` in settings.py is fine for local development
  but should be tightened to your real domain before deploying anywhere public.
- Change `SECRET_KEY` in settings.py before deploying.
- To deploy the API somewhere real (Render, Railway, PythonAnywhere), update
  `CONTACT_API_URL` in `portfolio/script.js` to point at the deployed URL.
