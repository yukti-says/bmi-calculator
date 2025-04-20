# BMI Calculator - Flask Web App

A simple web application that calculates Body Mass Index (BMI) based on user input (weight and height). The app provides the BMI value and a message indicating whether the user is underweight, normal weight, overweight, or obese.

## Features

- Input weight (kg) and height (m).
- Calculates BMI based on the formula: `BMI = weight / (height ** 2)`.
- Provides a message based on the calculated BMI:
  - Underweight (BMI < 18.5)
  - Normal weight (18.5 ≤ BMI < 24.9)
  - Overweight (25 ≤ BMI < 29.9)
  - Obese (BMI ≥ 30)

## Tech Stack

- **Backend**: Flask (Python)
- **Web Server**: Gunicorn
- **Frontend**: HTML, CSS (PureCSS)
- **Deployment**: Render (can be deployed to other platforms like Heroku or Railway)

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/yukti-says/bmi-calculator.git
cd bmi-calculator
2. Set up a virtual environment (optional but recommended):
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
3. Install the dependencies:
pip install -r requirements.txt
4. Run the Flask app locally:
python main.py
