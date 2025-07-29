# 🌐 Personal Portfolio Website

This is a personal portfolio website built using **Django**, HTML, CSS, and JavaScript. It showcases my skills, projects, resume, contact information, and more in a professional and interactive way.

---

## 🔧 Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS (custom styles with glowing purple aesthetic), JavaScript
- **Database**: SQLite (default)
- **Deployment**: GitHub + PythonAnywhere

---

## 📁 Project Structure

portfolio-site/
├── main/ # Main Django app
│ ├── migrations/
│ ├── static/ # Static files (CSS, JS, icons)
│ │ └── main/
│ │ ├── css/
│ │ ├── js/
│ │ └── img/
│ ├── templates/
│ │ └── main/
│ ├── models.py
│ ├── views.py
│ └── urls.py
├── portfolio/ # Django project folder
│ └── urls.py
├── db.sqlite3 # SQLite database
├── manage.py
└── README.md

---

## 🧠 Features

- ✅ Home, About Me, Skills, Projects, Resume, Contact sections
- ✅ Theme Toggle: 🌙 Dark Mode / ☀️ Light Mode with animated gradients
- ✅ Responsive navbar with icons + dropdowns
- ✅ Interactive skills section with click-to-expand descriptions
- ✅ Separate pages for:
  - Personal Information
  - Education (with maps & images)
  - Personal Skills (with icons)
  - Certifications & Internships
  - Personal Projects (Tic Tac Toe, Quiz Game)
- ✅ Functional Resume PDF download button
- ✅ Django Admin support for dynamic content
- ✅ Media files rendered from database (profile pics, education images)

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/imcharan3/my-django-portfolio.git
cd my-django-portfolio

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

---

🌍 Live Deployment Hosted on: [imcharan3.pythonanywhere.com](https://imcharan3.pythonanywhere.com)


---


