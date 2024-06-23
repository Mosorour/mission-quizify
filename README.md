# mission-quizify

## Webpage for Generating MCQs from PDF Documents

### Overview
This project is a web application that allows users to upload PDF documents and generates multiple-choice questions (MCQs) with four choices and detailed answer explanations. It is designed to help students and educators create study materials quickly and efficiently.

### Features
- **PDF Upload**: Users can upload PDF documents from which the application extracts text.
- **MCQ Generation**: Automatically generates multiple-choice questions based on the content of the uploaded PDF.
- **Answer Choices**: Provides four answer choices for each question.
- **Explanations**: Includes detailed explanations for each correct answer.

### Tools and Technologies Used
- **Streamlit**: A fast way to build and share data applications.
- **Python**: The programming language used for backend development.
- **Chroma Collection**: Used for storing and retrieving document embeddings.
- **Vertex AI**: Utilized for advanced machine learning model deployment and operations.
- **Google Cloud**: Cloud platform for hosting and other cloud services.
- **LangChain**: For building and managing the language model interactions.

### Prerequisites
- Python 3.8 or later
- A Google Cloud account with Vertex AI enabled
- API keys and service account credentials for Google Cloud services

### Installation
1. **Navigate to the directory**:

2. **Install the required Python packages**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up Google Cloud credentials**:
   Ensure you have your Google Cloud service account key file and set the environment variable:
   ```sh
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-file.json"
   ```

4. **Configure Vertex AI and Chroma Collection**:
   Follow the Google Cloud documentation to set up Vertex AI and Chroma Collection.

### Usage
1. **Run the Streamlit application**:
   ```sh
   streamlit run app.py
   ```

2. **Upload a PDF**:
   - Navigate to the local URL provided by Streamlit.
   - Use the file uploader to select and upload a PDF document.

3. **Generate MCQs**:
   - Once the PDF is uploaded, click the "Generate MCQs" button.
   - The application will process the document and display the generated MCQs with answer choices and explanations.

### File Structure
- `app.py`: Main application file for Streamlit.
- `requirements.txt`: List of Python dependencies.
- `README.txt`: This README file.
- `src/`: Directory containing the core logic for PDF processing, MCQ generation, and interactions with Chroma Collection and Vertex AI.

### Core Logic
- **PDF Processing**: Extracts text from the uploaded PDF.
- **MCQ Generation**: Utilizes Vertex AI to generate MCQs based on the extracted text.
- **Answer Choices and Explanations**: Uses LangChain to formulate answer choices and provide detailed explanations.

### Contribution
Contributions are welcome! Please fork the repository and create a pull request with your changes.


## Loom Video:
https://www.loom.com/share/58f570e3903b41209ec51ec394e524f0?sid=97ea0d2f-fa88-4ad1-aae0-9be1c17bdd53

## Pitch presentation:
https://pitch.com/v/quiz-generator-megr8z
