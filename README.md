Mood Tracker - Sentiment Analysis
A web app that analyzes journal entries and provides personalized recommendations using AI.

How to Run the Project
1. Clone the Repository bash

git clone https://github.com/syedahajra/SentimentAnalysis.git
cd SentimentAnalysis

2. Set Up Backend (Flask)
Install Dependencies:
Create a virtual environment and activate it:
bash

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

Install the required packages:
pip install -r requirements.txt

Set Up Environment Variables:
Create a .env file in the root directory and add:
makefile

GEMINI_API_KEY=your-gemini-api-key

Run the Flask App:
python app.py
The backend will be available at http://127.0.0.1:5000.

3. Set Up Frontend
Serve the Frontend:
Open index.html in a browser or use a local server:
python -m http.server 8000
The frontend will be available at http://127.0.0.1:8000.

4. Use the App
Go to the frontend in your browser.
Enter a journal entry and click "Analyze Mood".
View the analysis and recommendations below.
