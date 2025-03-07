from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)  # Enable CORS

# Set up Gemini API key
API_KEY = "AIzaSyCvYPF4FLCXw07_ebw63Z_WKOVhx1f8dT0"  # Replace with your actual Gemini API key
genai.configure(api_key=API_KEY)

@app.route('/generate-itinerary', methods=['POST'])
def generate_itinerary():
    data = request.json
    start_date = data.get('startDate')
    end_date = data.get('endDate')
    start_place = data.get('startPlace')
    destination = data.get('destination')
    budget = data.get('budget')
    special_activities = data.get('specialActivities')

    try:
        # Initialize the model with 'gemini-2.0-flash'
        model = genai.GenerativeModel('gemini-2.0-flash')

        # Create a detailed prompt for the AI
        prompt = f"""
        Create a detailed day-by-day travel itinerary for a trip from {start_place} to {destination}.
        - Start Date: {start_date}
        - End Date: {end_date}
        - Budget: {budget}
        - Special Activities: {special_activities}
        Include activities, transportation, accommodation, and food recommendations.
        Format the itinerary clearly with day-wise breakdowns.
        """

        # Generate the itinerary using Gemini AI
        response = model.generate_content(prompt)
        itinerary = response.text

        return jsonify({'itinerary': itinerary})
    except Exception as e:
        print(f"Error generating itinerary: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)