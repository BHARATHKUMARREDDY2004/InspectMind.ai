# InspectMind.ai : Construction Site Inspection Report Generator

## Overview

This application captures construction site videos with or without narration and images, then generates detailed inspection reports from these media files. The project leverages Assembly AI's Speech-to-Text API for audio transcription, OpenAI GPT-4 for image analysis and report generation, Flask as the backend, and HTML, CSS, and JavaScript for the frontend.

## Features

- **Video and Image Capture:** Capture construction site videos and images.
- **Speech-to-Text:** Convert narration in videos to text using Assembly AI's API.
- **Image Analysis:** Analyze images using OpenAI's GPT-4.
- **Report Generation:** Generate detailed inspection reports from analyzed media.
- **Web Interface:** User-friendly web interface for uploading media and viewing reports.

## Technologies Used

- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **APIs:** 
  - Assembly AI Speech-to-Text
  - OpenAI GPT-4
- **Version Control:** GitHub

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Assembly AI API Key
- OpenAI GPT-4 API Key

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/BHARATHKUMARREDDY2004/InspectMind.ai.git
   cd InspectMind.ai
   ```

2. **Create a virtual environment and activate it:**

   ```sh
    python -m venv myenv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Flask server:**

   ```sh
   flask run
   ```

2. **Open your browser and navigate to:**

   ```
   http://localhost:5000
   ```

### Usage

1. **Upload Videos/Images/audios:** Use the web interface to upload videos and images of the construction site.
2. **Specified sample:** it also takes sample report,It will generate in that form.
3. **Generate Report:** The application will process the media, analyze them, and generate a detailed inspection report.
4. **View Report:** View and download the generated report from the web interface.

## Project Structure

```
InspectMind/
├── frames/
├── audios/
├── videos/
├── models/
├── templates/
├── static/
├── myenv
├── app.py
├── .git/
└── README.md
├── requirements.tx
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Contact

For any questions or suggestions, feel free to open an issue or contact me directly at vemireddybharathreddy90@gmail.com.
---
Thank you for using the InspectMind!
