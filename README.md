🏦 Nepali Currency Detector 🇳🇵
A Nepali Currency Note Classification and Fake Currency Detection System using Deep Learning (CNN) and Streamlit.

This app allows users to upload images of Nepali banknotes and determine:

The denomination (100, 500, 1000)

Whether the note is Real or Fake

🚀 Project Overview
This project uses Convolutional Neural Networks (CNN) trained on the Nepali Currency Dataset from Kaggle.
The Streamlit app (app.py) provides an easy-to-use interface that runs locally on your machine via your browser.

🗄️ Dataset
Nepali Currency Dataset:
Kaggle Link → Click Here

Classes:

Class	Meaning
100	100 Rupee (Real)
500	500 Rupee (Real)
1000	1000 Rupee (Real)
fake 100	100 Rupee (Fake)
fake 500	500 Rupee (Fake)

📂 Project Structure
graphql
Copy
Edit
Nepali-Currency-Detector/
│
├── app.py                  # Streamlit application (Run this file)
├── FCD.ipynb                # Model Training Notebook (Optional for retraining)
├── currency_detector.h5     # Pre-trained CNN Model (Included)
├── README.md                # Project Documentation (This file)
└── requirements.txt         # Python dependencies (recommended to create)
🛠️ Installation Guide
Step 1: Clone the Repository
Open Command Prompt or Terminal:

bash
Copy
Edit
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Step 2: Install Python Packages
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
Install dependencies:

bash
Copy
Edit
pip install streamlit tensorflow pillow numpy
Or use:

bash
Copy
Edit
pip install -r requirements.txt
Note: If requirements.txt is not provided, you can create one by running:
pip freeze > requirements.txt

Step 3: Run the Application
In Command Prompt, execute:

bash
Copy
Edit
streamlit run app.py
Step 4: Access the App
After running the above command:

Streamlit will automatically open your default web browser.

If it doesn't, copy the URL shown in the terminal (usually:
http://localhost:8501) and paste it into your browser.

🖼️ How to Use the App
1️⃣ Upload Image
Click "Choose an image..." and upload a Nepali currency image (jpg, png, jpeg).

2️⃣ Classification
The model will process the image and output:

Output	Meaning
Real Currency	If the note is real (100, 500, 1000)
Fake Currency	If the note is fake (fake 100, fake 500)

3️⃣ View Confidence
See how confident the model is in its prediction (percentage).

🔍 Example Workflow
Start the App:

bash
Copy
Edit
streamlit run app.py
Upload this image:



Output:

yaml
Copy
Edit
Status: Real Currency
Classified as: 1000 Rupee Note
Confidence: 98.75%
🧠 Model Information
Model Type: Convolutional Neural Network (CNN)

Input Size: 224x224 pixels

Framework: TensorFlow / Keras

Classes:
['100', '500', '1000', 'fake 100', 'fake 500']

The trained model is saved as currency_detector.h5 (already included).

🏗️ Training the Model (Optional)
If you want to retrain the model:

Download the dataset from Kaggle.

Run FCD.ipynb (Fake Currency Detector notebook).

Save the model as currency_detector.h5.

🐛 Troubleshooting
Issue	Solution
ModuleNotFoundError	Run pip install streamlit tensorflow pillow numpy
Browser does not open	Copy the localhost link from Command Prompt and paste it into your browser manually
File not found: currency_detector.h5	Make sure the currency_detector.h5 is in the same folder as app.py

⚙️ System Requirements
Python: 3.7 or above

TensorFlow: 2.x

Streamlit: 1.x

Works on Windows, Mac, and Linux

📄 License
This project is licensed under the MIT License.
Free to use, modify, and share.

🙋‍♂️ Support
If you have questions, feel free to:

Open an Issue on GitHub

Connect with me on Kaggle: Prapanna Dhungel

