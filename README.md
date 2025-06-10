# 🌴 Club Service Admin – VacationVault Chatbot (Python Version)

![Deployed to AWS](https://img.shields.io/badge/Deployed-AWS-FF9900?logo=amazonaws&logoColor=white&style=for-the-badge)
![Made with Flask](https://img.shields.io/badge/Made%20with-Flask-000?logo=flask&logoColor=white&style=for-the-badge)
![Formspree Enabled](https://img.shields.io/badge/Formspree-Enabled-brightgreen?logo=formspree&logoColor=white&style=for-the-badge)
![Deployed to GitHub Pages](https://img.shields.io/badge/Deployed-GitHub%20Pages-blueviolet?logo=github&logoColor=white&style=for-the-badge)




Welcome to the **VacationVault Club Chatbot**, a fun and tropical-themed web chatbot built using Python and Flask. This interactive bot helps guide users through common requests like booking trips, joining membership plans, or reaching out to a concierge—all while staying chill with a relaxing island vibe. 🏖️

![Chatbot Preview](https://vacationvault-chat.s3.amazonaws.com/vacation_header.png)

---

## 🚀 Features

- ✅ Lightweight HTML + CSS UI with tropical branding
- 💬 Intelligent chatbot responses to common phrases and questions
- 📧 Lead capture (name, email, phone) integrated with [Formspree](https://formspree.io/)
- ✈️ Quick-action buttons for Membership, Booking, Contact, and more
- 🔄 Typing animations for realistic bot feel
- 📱 Mobile-responsive design

---

## 📂 Project Structure

VacationVault_TropicalChatbot_FinalUI/
├── index.html # Chatbot UI (deployed to S3)
├── main.py # Flask backend (for Python version)
├── static/ # Static assets (images, optional CSS)
├── templates/ # Jinja2 templates (if used in Python version)
├── .venv/ # Virtual environment (not pushed to GitHub)
└── README.md # This file


---

## ⚙️ Local Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/EHale24/club-service-vacationvault-chatbot-python.git
cd club-service-vacationvault-chatbot-python

## 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # On Mac/Linux

3. Install dependencies

pip install flask

4. Run the chatbot locally

python main.py


Then open http://127.0.0.1:5000/ in your browser.


🧠 How It Works
The chatbot UI is a floating interface with quick-action buttons and typing animations.

User input is matched against a set of keywords (e.g. "book", "join", "agent").

If triggered, the bot collects user name, email, and phone using a friendly conversation flow.

Data is sent via Formspree POST request to notify concierge staff.

🌐 Live Web Version
The HTML-only version is deployed and accessible via:

🔗 http://vacationvault-chat.s3-website-us-east-1.amazonaws.com

💡 This version runs without Flask and is embedded into the VacationVaultClub.com website.

✨ Screenshots


📬 Contact
Need help customizing or deploying your own branded bot?
Reach out at: https://vacationvaultclub.com/Contact

🤝 Contributing
Pull requests and forks are welcome! If you’d like to suggest improvements or submit bug fixes:

Fork the repo

Create a new branch

Submit a PR with a clear description

🏷️ Tags
chatbot • flask • html • python • lead generation • vacation club • formspree • tropical • customer service • web widget

Made with ☀️ and coconut vibes by Evelyn Hale

