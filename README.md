# Resume Genie

Resume Genie is a web application designed to extract and process resume information from uploaded documents using OCR and LLM technologies. The application features a user-friendly frontend for uploading resumes and displaying structured data extracted from them.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [API Documentation](#api-documentation)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

- Upload resumes in PDF and Word formats.
- Extract relevant information such as name, contact details, education, skills, and experience.
- Display the structured data in a visually appealing format.

## Technologies Used

- **Backend:** 
  - FastAPI
  - OCR (Optical Character Recognition)
  - Python
- **Frontend:**
  - React
  - Bootstrap
  - Axios

## Installation

### Prerequisites

- Python 3.7 or higher
- Node.js and npm

### Backend Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AjayKuchhadiya/ResumeGenie.git
   cd ResumeGenie/backend
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server:**
   ```bash
   cd src
   python main.py
   ```

5. **The backend will be accessible at `http://127.0.0.1:8000`.**

### Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd ../frontend
   ```

2. **Install the required packages:**
   ```bash
   npm install
   ```

3. **Run the React application:**
   ```bash
   npm start
   ```

4. **The frontend will be accessible at `http://localhost:3000`.**

## API Documentation

### Upload Endpoint

- **POST** `/upload`
- **Request Body:** 
  - `file`: The resume file (PDF or Word document).
- **Response:**
  - Returns a JSON object containing the structured data extracted from the resume.

### Example Request
```http
POST /upload
Content-Type: multipart/form-data

file: [your resume file]
```

### Example Response
```json
{
    "First Name": "AJAY",
    "Last Name": "KUCHHADIYA",
    "Email Address": "kuchhadiyaajay86kn@gmail.com",
    "Phone Number": "+91-7457878864",
    "Education History": "B.Tech, Computer Science, 7.07 CGPA, 2020 - 2024, Hindustan College of Science and Technology, Farah, Uttar Pradesh",
    "Experience Summary": "Trainee Associate Software Engineer at Walking Tree Technologies, Data Science Intern at Foxmula, and worked on personal projects CrewAI Health Advisor and FashionAI: An AI-based Fashion Platform",
    "Skills": [
        "Python",
        "C/C++",
        "Scikit-learn",
        "TensorFlow",
        "Pandas",
        "SQL",
        "NoSQL",
        "Matplotlib",
        "Seaborn",
        "LLM",
        "RAG",
        "Autogen",
        "Vector Store",
        "Hugging Face",
        "Flask",
        "FastAPI",
        "RestfulAPI",
        "PostgreSQL",
        "MongoDB"
    ],
    "Current Position": "Trainee Associate Software Engineer",
    "Years of Experience": 0.5
}
```

## Usage

1. Open the frontend application in your browser.
2. Upload a resume file using the upload form.
3. The extracted structured data will be displayed in a table format.

## Contributing

Contributions are welcome! If you have suggestions for improvements or features, please fork the repository and submit a pull request.
