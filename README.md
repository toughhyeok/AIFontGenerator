# AI Font Generator

Welcome to the AI Font Generator! This web application allows you to generate unique font styles based on descriptive keywords. Leveraging the power of AI (simulated in this version), it provides a simple and intuitive interface to bring your font ideas to life.

This project was developed step-by-step as an educational tool to learn about web application development with Python and FastAPI, and to explore the integration of AI models.

## ✨ Features

-   **Keyword-Based Font Generation**: Select from a list of popular keywords (e.g., Modern, Elegant, Playful) or enter your own to define the style of the font you want.
-   **Instant Preview**: See a live preview of the generated font directly in your browser.
-   **Simple & Modern UI**: A clean and user-friendly interface built with Bootstrap.
-   **Extensible Backend**: The font generation logic is modular, making it easy to replace the current simulation with a real AI model in the future.

## 🛠️ Tech Stack

-   **Backend**: [Python](https://www.python.org/) with [FastAPI](https://fastapi.tiangolo.com/)
-   **Frontend**: HTML, [Bootstrap 5](https://getbootstrap.com/), JavaScript
-   **Templating**: [Jinja2](https://jinja.palletsprojects.com/)
-   **Server**: [Uvicorn](https://www.uvicorn.org/)

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### 1. Prerequisites

-   Python 3.8+
-   Git

### 2. Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/AIFontGenerator.git
    cd AIFontGenerator
    ```
    *(Note: Replace `YourUsername` with your actual GitHub username.)*

2.  **Create and activate a Python virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Add Base Fonts (Crucial Step!):**
    The AI needs base fonts to "learn" from. You need to provide them.
    -   Go to a free font provider like [Google Fonts](https://fonts.google.com/).
    -   Download `.ttf` or `.otf` files for various styles (e.g., a modern font, an elegant font, a playful font).
    -   Place them inside the `core/base_fonts/` directory.
    -   Rename the files to match the keywords you want to use, for example: `modern.ttf`, `elegant.ttf`, `playful.ttf`.

### 3. Running the Application

Once the setup is complete, you can start the web server:

```bash
uvicorn app:app --reload
```

The `--reload` flag makes the server automatically restart after you make code changes.

Open your web browser and navigate to **http://127.0.0.1:8000**. You should now see the AI Font Generator in action!

## 📝 How It Works (Simulation)

Currently, this project *simulates* AI-based font generation. Here's the process:
1.  The user selects keywords in the UI.
2.  The browser sends these keywords to the FastAPI backend.
3.  The backend looks for a font in `core/base_fonts/` that matches one of the keywords (e.g., `modern.ttf`).
4.  It copies the chosen base font to a temporary location in `static/fonts/` with a unique name.
5.  The path to this new font is sent back to the browser.
6.  The browser dynamically loads the new font and applies it to the preview text.

This setup allows the entire application flow to be tested and developed before a complex AI model is integrated.
