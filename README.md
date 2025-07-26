# MSE_Chat_Bot
# 🎓 College MSE Exam Assistant Chatbot

An intelligent Flask-based chatbot designed to answer college Mid-Semester Examination (MSE) queries for Technical Education Semester V students. The chatbot provides instant access to exam schedules, timings, subject codes, and helpful exam preparation tips.

## 📋 Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### 🤖 Intelligent Query Processing
- **Natural Language Understanding**: Recognizes various ways of asking exam-related questions
- **Subject Recognition**: Supports both full names and abbreviations (AI, SE, SPCD, VLSI, etc.)
- **Branch-Specific Queries**: Handles Computer Engineering and Electronics & Telecommunication Engineering
- **Smart Matching**: Uses similarity algorithms to find closest matching subjects

### 📅 Comprehensive Exam Information
- **Real-time Schedule**: Displays actual MSE exam dates and times from official timetable
- **Subject Details**: Shows subject codes, duration, and branch information
- **Days Countdown**: Calculates and displays days remaining until exams
- **Motivational Messages**: Provides context-aware preparation tips

### 🎨 User-Friendly Interface
- **Modern Chat UI**: Clean, responsive design with smooth animations
- **Real-time Responses**: Instant chatbot responses with typing indicators
- **Mobile Responsive**: Works seamlessly on desktop and mobile devices
- **Professional Design**: Exam-themed interface with intuitive navigation

### 📚 Additional Features
- **Branch-wise Subject Listing**: View all subjects for specific engineering branches
- **Multiple Query Formats**: Supports various question patterns
- **Error Handling**: Helpful suggestions when queries aren't understood
- **24/7 Availability**: Always accessible for student queries

## 🚀 Demo

### Sample Queries You Can Try:
```
"When is AI exam?"
"Artificial Intelligence exam schedule"
"COMP subjects list"
"What time is Software Engineering exam?"
"EXTC subjects"
"When is my SPCD exam?"
"Help me with exam schedule"
```

### Sample Response:
```
📅 Artificial Intelligence Exam Details:

🏫 Branch: Computer Engineering
📊 Subject Code: CMPN501
🗓️ Date: 2025-07-28 (Tomorrow! ⚡)
⏰ Time: 10:15 AM - 11:00 AM
⏱️ Duration: 45 minutes

⚡ Exam is TOMORROW! Final revision time! 📖
```

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/college-faq-chatbot.git
cd college-faq-chatbot
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Install spaCy Model (Optional - for advanced NLP)
```bash
# For enhanced NLP features (recommended)
python -m spacy download en_core_web_md

# Or use smaller model if above fails
python -m spacy download en_core_web_sm
```

**Note**: If spaCy installation fails, the chatbot includes a fallback version that works without spaCy.

### Step 5: Run the Application
```bash
python app.py
```

Visit `http://localhost:5000` in your web browser.

## 📖 Usage

### Starting a Conversation
1. Open the chatbot interface
2. Type your exam-related query in the input field
3. Press Enter or click Send
4. Get instant responses with exam details

### Supported Query Types

#### 🎯 Specific Exam Queries
- `"When is [subject] exam?"`
- `"[Subject] exam schedule"`
- `"What time is [subject] exam?"`
- `"[Subject] exam date"`

#### 📚 Subject Listing
- `"COMP subjects"`
- `"EXTC subjects list"`
- `"Computer Engineering subjects"`

#### ℹ️ General Information
- `"Help"`
- `"What branches do you support?"`
- `"MSE exam information"`

### Subject Abbreviations
| Abbreviation | Full Subject Name |
|--------------|-------------------|
| AI | Artificial Intelligence |
| SE | Software Engineering |
| SPCD | System Programming and Compiler Design |
| DS | Distributed Systems |
| VLSI | Basic VLSI Design |
| CN | Computer Networks |
| DSP | Digital Signal Processing |

## 📁 Project Structure

```
college-faq-chatbot/
├── app.py                     # Main Flask application
├── templates/
│   └── chat.html             # Chat interface template
├── static/                   # CSS, JS, images (if any)
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── exam_schedule.py         # Exam data (optional separate file)
└── venv/                    # Virtual environment (not in git)
```

## 🛠️ Technologies Used

### Backend
- **Flask**: Web framework for Python
- **spaCy**: Natural Language Processing (optional)
- **Python**: Core programming language
- **difflib**: String similarity matching (fallback)

### Frontend
- **HTML5**: Structure and content
- **CSS3**: Styling and animations
- **JavaScript**: Interactive functionality
- **AJAX**: Asynchronous communication

### Data Storage
- **Python Dictionary**: In-memory exam data storage
- **JSON**: API response format

## 🔌 API Endpoints

### GET `/`
Returns the main chat interface.

### POST `/chat`
Processes user messages and returns bot responses.

**Request Body:**
```json
{
  "message": "When is AI exam?"
}
```

**Response:**
```json
{
  "response": "📅 Artificial Intelligence Exam Details:..."
}
```

## 🎓 Supported Branches & Subjects

### Computer Engineering (COMP/CSE)
- Artificial Intelligence (CMPN501)
- Software Engineering (CMPN502)
- System Programming and Compiler Design (CMPN503)
- Distributed Systems (CMPN504)
- Professional Elective-1 (CMPNPE1)
- MDM (CMPN505)
- E-waste and Environmental Management (CMPN506)

### Electronics & Telecommunication Engineering (EXTC)
- Basic VLSI Design (EXTC501)
- Computer Networks (EXTC502)
- Digital Signal Processing (EXTC503)
- Electromagnetics and Antenna (EXTC504)
- Professional Elective-1 (EXTCPE1)
- MDM (EXTC505)

## 🔧 Customization

### Adding New Subjects
Update the `exam_schedule` dictionary in `app.py`:

```python
"new_subject_name": {
    "date": "YYYY-MM-DD",
    "time": "HH:MM AM/PM - HH:MM AM/PM",
    "duration": "X minutes/hours",
    "code": "SUBJECT_CODE"
}
```

### Adding New Branches
Add new branch data to `exam_schedule` and update `branch_aliases`.

### Modifying Responses
Update the `faq_data` dictionary or modify the `format_exam_response` function.

## 🚀 Deployment Options

### Local Development
```bash
python app.py
```

### Production Deployment
- **Heroku**: Use `Procfile` and `requirements.txt`
- **AWS**: Deploy using Elastic Beanstalk or EC2
- **PythonAnywhere**: Simple drag-and-drop deployment
- **Docker**: Containerized deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- Add more engineering branches
- Implement database storage
- Add admin panel for updating schedules
- Enhance NLP capabilities
- Add voice input/output
- Create mobile app version

## 📝 Future Enhancements

- [ ] Database integration (SQLite/PostgreSQL)
- [ ] Admin panel for schedule updates
- [ ] User authentication and personalization
- [ ] Email/SMS notifications for upcoming exams
- [ ] Integration with college management systems
- [ ] Multi-language support
- [ ] Voice-based interaction
- [ ] Analytics dashboard
- [ ] Mobile application

## 🐛 Known Issues

- spaCy model installation may fail on some systems (fallback available)
- Limited to predefined exam schedules
- No user session persistence

**⭐ If this project helped you, please give it a star on GitHub!**

Made with ❤️ for students by students.
