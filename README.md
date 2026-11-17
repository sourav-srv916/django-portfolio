# 🚀 Django Developer Portfolio

A modern, responsive, and dynamic personal portfolio website built using **Python and Django**.

This portfolio showcases my technical skills, professional experience, and development projects through a clean user interface, interactive components, and developer-themed animations.

The application features dynamic content management using Django Admin, a functional contact form, email notifications, and secure production deployment.

## 🌐 Live Demo

🔗 **Live Portfolio:** https://souravp.pythonanywhere.com/

🔗 **GitHub Repository:** https://github.com/sourav-srv916/django-portfolio

---

## ✨ Key Features

- 🎨 Modern and professional user interface
- 📱 Fully responsive design for mobile, tablet, and desktop
- ⚡ Smooth animations and interactive UI components
- 💻 Developer-themed animated section backgrounds
- 🛠️ Dynamic skills management through Django Admin
- 💼 Professional experience timeline
- 📂 Dynamic project showcase with a dedicated projects page
- 📧 Functional contact form with email notifications
- 🛡️ Contact form validation and spam protection
- 📄 Downloadable resume
- 🔍 SEO-friendly sitemap and robots.txt
- 🔐 Secure environment-based configuration
- 🌐 Production deployment with HTTPS

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| Backend | Python, Django |
| Frontend | HTML5, CSS3, JavaScript |
| Database | MySQL (Local Development), SQLite (Production) |
| Email Integration | Gmail SMTP (Local Development), Brevo API (Production) |
| Version Control | Git, GitHub |
| Deployment | PythonAnywhere |
| Icons | Font Awesome, Devicon |
| SEO | XML Sitemap, robots.txt, Google Search Console |

---

## 📂 Portfolio Sections

### 🏠 Home

A modern developer introduction featuring animated backgrounds, interactive elements, and navigation to important portfolio sections.

### 👨‍💻 About

An overview of my professional background, development experience, technical interests, and career journey.

### 🧠 Skills

A dynamically managed collection of technical skills displayed using interactive cards and technology-related visual elements.

### 💼 Experience

A professional experience timeline showcasing job roles, organizations, responsibilities, and career progression.

### 🚀 Projects

A collection of development projects featuring:

- Project descriptions
- Technology information
- Project images
- GitHub repository links
- Dedicated projects listing page

### 📬 Contact

A functional contact section that allows visitors to send messages.

Features include:

- Server-side form validation
- Spam protection
- Database message storage
- Email notifications using Brevo API in production

---

## 📁 Project Structure

```text
django-portfolio/
│
├── main/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── sitemaps.py
│   └── robots.txt
│
├── portfolio/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Local Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sourav-srv916/django-portfolio.git
cd django-portfolio
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```powershell
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root.

Configure the environment variables required by `portfolio/settings.py`, including:

- Django secret key
- Debug configuration
- Allowed hosts
- Database settings
- Email provider configuration
- Email credentials or API keys

**Important:** Never commit your `.env` file or sensitive credentials to GitHub.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create an Admin Account

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser:

http://127.0.0.1:8000/

**Note:** Local development requires a correctly configured database and environment variables.

---

## 🛡️ Security Features

The portfolio implements several security practices:

- Environment-based secret management
- Django CSRF protection
- Server-side form validation
- Spam-prevention mechanisms
- HTTPS in production
- Secure session and CSRF cookies
- Production debug mode disabled
- Restricted access to sensitive configuration files

---

## 🌐 Deployment

The portfolio is deployed using **PythonAnywhere**.

### Production Configuration

- **Hosting:** PythonAnywhere
- **Framework:** Django
- **Database:** SQLite
- **Static Files:** Django collectstatic
- **Media Files:** PythonAnywhere media configuration
- **Email Service:** Brevo API
- **Version Control:** GitHub
- **HTTPS:** Enabled

### Updating the Live Website

After making and testing changes locally:

```bash
git add .
git commit -m "Update portfolio"
git push origin main
```

On PythonAnywhere:

```bash
cd /home/souravp/django-portfolio
git pull origin main
python manage.py collectstatic --noinput
```

Finally, reload the web application from the PythonAnywhere dashboard.

> Review `git status` before staging files. Database migrations are only required when the database schema changes.

---

## 🔍 SEO Integration

The portfolio includes:

- XML sitemap generation using Django
- robots.txt configuration
- Google Search Console ownership verification
- Sitemap submission to Google
- Homepage and projects page indexing requests

**Sitemap:** https://souravp.pythonanywhere.com/sitemap.xml

**Robots.txt:** https://souravp.pythonanywhere.com/robots.txt

---

## 🔮 Future Enhancements

- Additional development projects
- Improved accessibility
- Performance optimizations
- Enhanced interactive components
- Further responsive design improvements

---

## 👨‍💻 Author

**Sourav P**

Python & Django Developer

🌐 **Portfolio:** https://souravp.pythonanywhere.com/

💻 **GitHub:** https://github.com/sourav-srv916

---

## ⭐ Support

If you find this project useful, consider giving the repository a star.

**Built with Python, Django, and a passion for web development.**