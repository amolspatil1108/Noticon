# Netflix Grid App Demo

A simple monorepo with:

- **Frontend:** React (Vite) Netflix-style white grid displaying WhatsApp, Telegram, Outlook, and Gmail cards
- **Backend:** Python Flask API serving the list of services

---

## Getting Started

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

By default, Flask runs on [http://localhost:5000](http://localhost:5000).

---

### Frontend

```bash
cd frontend
npm install
npm run dev
```

This will start Vite on [http://localhost:5173](http://localhost:5173).

---

## Directory Structure

```
netflix-grid-app/
  backend/
    app.py
    requirements.txt
  frontend/
    src/
      App.jsx
      App.css
      main.jsx
    index.html
    package.json
    vite.config.js
  README.md
```

---

## Notes

- The frontend fetches `/api/services` (proxied to Flask backend).
- Update logos or add more services as needed in `backend/app.py`.