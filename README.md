 # Gemini Mobile App

**Harness the power of Gemini AI on your mobile device**

This project brings the capabilities of the Gemini AI model to a mobile app, enabling users to interact with it through a user-friendly interface. It's built with a Flutter frontend for a seamless cross-platform experience and a Flask backend to handle the AI interactions.

## Features

- **Interactive text generation:** Engage in conversations, create stories, translate languages, and more.
- **Code generation:** Generate code in various programming languages based on your instructions.
- **Personalized experiences:** Tailor responses to your preferences and past interactions.
- **Seamless cross-platform compatibility:** Works on both Android and iOS devices.

## Tech Stack

- **Frontend:** Flutter
- **Backend:** Flask
- **AI Model:** Gemini

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SohamDesai1/gemini-model-mobile-app.git
   ```

2. **Install dependencies:**
   ```bash
   cd frontend
   flutter pub get
   ```

3. **Set up backend:**
   - Create a virtual environment and install required packages:
     ```bash
     python -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     ```
   - Configure Gemini API credentials:
     - Obtain your API key from the Gemini console.
     - Set the `GEMINI_API_KEY` environment variable.

4. **Run the app:**
   - Start the backend server:
     ```bash
     python app.py
     ```
   - Start the Flutter app:
     ```bash
     flutter run
     ```

## Contributing

We welcome contributions! Please refer to the `CONTRIBUTING.md` file for guidelines.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or feedback, feel free to reach out to us at <your-email>.
