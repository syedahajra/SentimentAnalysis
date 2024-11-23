from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Enable CORS for the entire app, allowing all origins (adjust this for security if needed)
CORS(app)

# Get the Gemini API key from the environment variable
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
# Configure the Google Generative AI library
genai.configure(api_key=GEMINI_API_KEY)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')
    
    # Generate a detailed prompt for sentiment and emotional analysis
    prompt = f"your role is of psychologist/therapist. Analyze following journal entry: '{text}'. Provise analysis as therapist on this."

    try:
        # Use Gemini API to generate the analysis and recommendations
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        
        # Debug: Print the full response to inspect
        print("Gemini API Response:", response)

        # Extract the generated analysis from the response
        analysis_text = response.candidates[0].content.parts[0].text

        # Now create a new prompt for generating recommendations based on the analysis
        recommendation_prompt = f"Based on the following analysis, generate personalized recommendations for the person: '{analysis_text}'. Provide therapeutic or psychological advice and suggestions."
        
        recommendation_response = model.generate_content(recommendation_prompt)
        
        # Extract the recommendations from the response
        recommendations_text = recommendation_response.candidates[0].content.parts[0].text

        return jsonify({
            "text": text,
            "analysis": analysis_text,
            "recommendations": recommendations_text
        })

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500



@app.route("/")
def home():
    return "Hello, Azure!"

if __name__ == "__main__":
    app.run(debug=True)
