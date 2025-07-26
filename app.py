from flask import Flask, render_template, request, jsonify
import spacy
from datetime import datetime, timedelta

# Load spaCy model
nlp = spacy.load("en_core_web_md")

app = Flask(__name__)

# Real exam schedule data from your PDF
exam_schedule = {
    "computer_engineering": {
        "artificial intelligence": {
            "date": "2025-07-28",
            "time": "10:15 AM - 11:00 AM",
            "duration": "45 minutes",
            "code": "CMPN501"
        },
        "software engineering": {
            "date": "2025-08-04",
            "time": "10:15 AM - 11:00 AM",
            "duration": "45 minutes",
            "code": "CMPN502"
        },
        "system programming and compiler design": {
            "date": "2025-08-11",
            "time": "10:15 AM - 11:00 AM",
            "duration": "45 minutes",
            "code": "CMPN503"
        },
        "distributed systems": {
            "date": "2025-08-18",
            "time": "10:15 AM - 11:00 AM",
            "duration": "45 minutes",
            "code": "CMPN504"
        },
        "professional elective-1": {
            "date": "2025-08-25",
            "time": "09:15 AM - 10:00 AM",
            "duration": "45 minutes",
            "code": "CMPNPE1"
        },
        "mdm": {
            "date": "2025-08-25",
            "time": "10:00 AM - 11:00 AM",
            "duration": "1 hour",
            "code": "CMPN505"
        },
        "e-waste and environmental management": {
            "date": "2025-09-08",
            "time": "09:15 AM - 10:00 AM",
            "duration": "45 minutes",
            "code": "CMPN506"
        }
    },
    "electronics_and_telecommunication_engineering": {
        "basic vlsi design": {
            "date": "2025-07-28",
            "time": "10:15 AM - 11:00 AM",
            "duration": "45 minutes",
            "code": "EXTC501"
        },
        "computer networks": {
            "date": "2025-08-04",
            "time": "10:15 AM - 11:00 AM",
            "duration": "45 minutes",
            "code": "EXTC502"
        },
        "digital signal processing": {
            "date": "2025-08-11",
            "time": "10:15 AM - 11:00 AM",
            "duration": "45 minutes",
            "code": "EXTC503"
        },
        "electromagnetics and antenna": {
            "date": "2025-08-18",
            "time": "10:15 AM - 11:00 AM",
            "duration": "45 minutes",
            "code": "EXTC504"
        },
        "professional elective-1": {
            "date": "2025-08-25",
            "time": "09:15 AM - 10:00 AM",
            "duration": "45 minutes",
            "code": "EXTCPE1"
        },
        "mdm": {
            "date": "2025-08-25",
            "time": "10:00 AM - 11:00 AM",
            "duration": "1 hour",
            "code": "EXTC505"
        }
    }
}

# Enhanced subject aliases based on your actual subjects
subject_aliases = {
    "ai": "artificial intelligence",
    "se": "software engineering",
    "spcd": "system programming and compiler design",
    "compiler design": "system programming and compiler design",
    "system programming": "system programming and compiler design",
    "ds": "distributed systems",
    "pe1": "professional elective-1",
    "professional elective": "professional elective-1",
    "elective": "professional elective-1",
    "vlsi": "basic vlsi design",
    "cn": "computer networks",
    "networks": "computer networks",
    "dsp": "digital signal processing",
    "signal processing": "digital signal processing",
    "antenna": "electromagnetics and antenna",
    "electromagnetics": "electromagnetics and antenna",
    "e-waste": "e-waste and environmental management",
    "environmental management": "e-waste and environmental management"
}

# Enhanced branch aliases
branch_aliases = {
    "cse": "computer_engineering",
    "cs": "computer_engineering", 
    "comp": "computer_engineering",
    "computer": "computer_engineering",
    "extc": "electronics_and_telecommunication_engineering",
    "etc": "electronics_and_telecommunication_engineering",
    "electronics": "electronics_and_telecommunication_engineering",
    "telecommunication": "electronics_and_telecommunication_engineering",
    "ece": "electronics_and_telecommunication_engineering",
    "ec": "electronics_and_telecommunication_engineering"
}

def clean_input(text):
    """Clean and preprocess user input"""
    doc = nlp(text.lower())
    cleaned_tokens = []
    for token in doc:
        if not token.is_stop and token.is_alpha:
            cleaned_tokens.append(token.lemma_)
    return " ".join(cleaned_tokens)

def extract_subject_and_branch(user_input):
    """Extract subject and branch from user input with improved matching"""
    user_input_lower = user_input.lower()
    
    found_subject = None
    found_branch = None
    
    # Check for subject aliases first
    for alias, full_name in subject_aliases.items():
        if alias in user_input_lower:
            found_subject = full_name
            break
    
    # If no alias found, search for full subject names and partial matches
    if not found_subject:
        for branch_data in exam_schedule.values():
            for subject in branch_data.keys():
                # Check exact match first
                if subject in user_input_lower:
                    found_subject = subject
                    break
                # Check if any significant words from subject are in input
                subject_words = subject.split()
                significant_words = [word for word in subject_words if len(word) > 3]
                if len(significant_words) >= 2:  # For multi-word subjects
                    matches = sum(1 for word in significant_words if word in user_input_lower)
                    if matches >= 2:  # At least 2 significant words match
                        found_subject = subject
                        break
                elif len(significant_words) == 1 and significant_words[0] in user_input_lower:
                    found_subject = subject
                    break
            if found_subject:
                break
    
    # Check for branch aliases
    for alias, full_name in branch_aliases.items():
        if alias in user_input_lower:
            found_branch = full_name
            break
    
    # If no alias found, search for full branch names
    if not found_branch:
        for branch in exam_schedule.keys():
            branch_words = branch.replace('_', ' ').split()
            if any(word in user_input_lower for word in branch_words):
                found_branch = branch
                break
    
    return found_subject, found_branch

def get_exam_info(subject, branch=None):
    """Get specific exam information"""
    if not subject:
        return None, None
    
    # If branch is specified, look in that branch first
    if branch and branch in exam_schedule:
        if subject in exam_schedule[branch]:
            return exam_schedule[branch][subject], branch
    
    # If no branch specified or not found, search all branches
    for branch_name, branch_data in exam_schedule.items():
        if subject in branch_data:
            return branch_data[subject], branch_name
    
    return None, None

def calculate_days_until_exam(exam_date):
    """Calculate days until exam"""
    try:
        exam_datetime = datetime.strptime(exam_date, "%Y-%m-%d")
        today = datetime.now()
        days_diff = (exam_datetime - today).days
        
        if days_diff < 0:
            return f"This exam was {abs(days_diff)} days ago"
        elif days_diff == 0:
            return "Today! 🚨"
        elif days_diff == 1:
            return "Tomorrow! ⚡"
        else:
            return f"In {days_diff} days"
    except:
        return ""

def format_exam_response(exam_info, branch, subject):
    """Format the exam information response with enhanced details"""
    if not exam_info:
        return f"Sorry, I couldn't find exam information for '{subject}'. Please check the subject name or ask about available subjects."
    
    branch_display = branch.replace('_', ' ').title()
    subject_display = subject.title()
    
    days_until = calculate_days_until_exam(exam_info['date'])
    
    response = f"📅 {subject_display} Exam Details:\n\n"
    response += f"🏫 Branch: {branch_display}\n"
    response += f"📊 Subject Code: {exam_info['code']}\n"
    response += f"🗓️ Date: {exam_info['date']}"
    if days_until:
        response += f" ({days_until})"
    response += f"\n⏰ Time: {exam_info['time']}\n"
    response += f"⏱️ Duration: {exam_info['duration']}\n\n"
    
    # Add helpful tips based on days until exam
    if "today" in days_until.lower():
        response += "🚨 Exam is TODAY! Good luck! 🍀"
    elif "tomorrow" in days_until.lower():
        response += "⚡ Exam is TOMORROW! Final revision time! 📖"
    elif "days" in days_until and int(days_until.split()[1]) <= 7:
        response += "⏰ Exam is coming up soon! Time to intensify your preparation! 💪"
    else:
        response += "📚 Good luck with your exam preparation!"
    
    return response

def get_all_subjects_for_branch(branch):
    """Get all subjects for a specific branch"""
    if branch in exam_schedule:
        subjects = list(exam_schedule[branch].keys())
        return subjects
    return []

def get_response(user_input):
    """Get chatbot response using NLP and exam data"""
    user_input_lower = user_input.lower()
    
    # Check for branch-specific subject listing
    if "subjects" in user_input_lower or "list" in user_input_lower:
        subject, branch = extract_subject_and_branch(user_input)
        if branch:
            subjects = get_all_subjects_for_branch(branch)
            branch_display = branch.replace('_', ' ').title()
            if subjects:
                response = f"📚 Subjects for {branch_display}:\n\n"
                for i, subj in enumerate(subjects, 1):
                    response += f"{i}. {subj.title()}\n"
                response += f"\nAsk me about any specific subject's exam schedule!"
                return response
    
    # Check if user is asking about specific exam
    exam_keywords = ['exam', 'test', 'schedule', 'when', 'date', 'time']
    if any(keyword in user_input_lower for keyword in exam_keywords):
        subject, branch = extract_subject_and_branch(user_input)
        
        if subject:
            exam_info, found_branch = get_exam_info(subject, branch)
            return format_exam_response(exam_info, found_branch, subject)
    
    # General FAQ responses
    faq_data = {
        # General greetings
        "hello": "Hi! I can help you with MSE exam schedules for TE Semester V (2025-26 odd sem). Ask me about specific subjects like 'When is Artificial Intelligence exam?' 🎓",
        "hi": "Hello! Ask me about your MSE exam schedule. I can tell you dates, times, and details for any subject.",
        "help": "I can help you with:\n• Specific exam dates and times\n• Subject codes and durations\n• Branch-wise exam schedules\n• Days remaining until exams\n\nTry asking: 'When is my AI exam?' or 'EXTC subjects list'",
        
        # Branch info
        "branches": "I have exam data for:\n• Computer Engineering (COMP/CSE)\n• Electronics & Telecommunication Engineering (EXTC)\n\nAsk about specific subjects or type '[branch] subjects' to see all subjects!",
        
        # General exam info
        "mse exam": "MSE stands for Mid-Semester Exam. Most MSE exams are 45 minutes duration. Ask me about specific subjects to get exact schedules!",
        "exam duration": "Most MSE exams are 45 minutes, except MDM which is 1 hour. Ask about a specific subject for exact details.",
        "exam timing": "Most exams start at 10:15 AM, some at 9:15 AM. Ask about a specific subject for exact timing!",
        
        # Today's exam info
        "today exam": "Let me check today's exam schedule for you! What's your branch?",
        "tomorrow exam": "Let me check tomorrow's exam schedule! Which branch are you in?",
        
        "bye": "Goodbye! Best of luck with your Mid-Semester Exams! 📚🎓"
    }
    
    # Use semantic similarity for general FAQ
    user_input_cleaned = clean_input(user_input)
    user_doc = nlp(user_input_cleaned)
    
    best_match = None
    highest_score = 0.0
    
    for question, answer in faq_data.items():
        question_cleaned = clean_input(question)
        question_doc = nlp(question_cleaned)
        
        if user_doc.vector_norm and question_doc.vector_norm:
            similarity = user_doc.similarity(question_doc)
        else:
            similarity = 0.0
            
        if similarity > highest_score:
            highest_score = similarity
            best_match = answer
    
    if highest_score > 0.6:
        return best_match
    else:
        return "I'm not sure about that. Try asking about specific exam schedules like 'When is AI exam?' or 'COMP subjects list' or type 'help' for more options."

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    bot_response = get_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)