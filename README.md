# Personal AI Assistant

A lightweight personal AI assistant built with **Python, Streamlit, and the OpenAI API**. The application provides a simple web interface for interacting with an AI model while maintaining conversation history locally through a JSON-based memory system.

## Project Overview

This project demonstrates the development of a basic AI assistant that combines a web-based user interface, an external AI API, and local conversation persistence.

The application allows a user to:

* Enter a request through a Streamlit interface
* Send the request to an OpenAI language model
* Receive an AI-generated response
* Store the conversation locally
* Reload previous conversation history when the application starts

The project was designed as a practical introduction to integrating AI capabilities into a custom Python application.

## Architecture

```text
User
 │
 ▼
Streamlit Web Interface
 │
 │ User Input
 ▼
Python Application
 │
 ├── Load Local Memory
 │
 ├── OpenAI API Request
 │
 └── Save Conversation
 │
 ▼
OpenAI GPT-4.1 Mini
 │
 ▼
AI Response
 │
 ▼
Streamlit Interface
```

Conversation history is stored locally in `memory.json`.

## Key Features

### Streamlit Web Interface

The application uses Streamlit to provide a simple browser-based interface.

The interface includes:

* Application title
* Text input field
* Send button
* AI response display

### OpenAI API Integration

The application connects to the OpenAI API using the official Python client.

The model currently configured for the project is:

```python
model="gpt-4.1-mini"
```

The API key is loaded through an environment variable rather than being hard-coded into the source code.

### Local Conversation Memory

The assistant maintains conversation history using a local JSON file:

```text
memory.json
```

When the application starts, it checks whether the memory file exists.

If it exists, previous conversation messages are loaded. If it does not exist, the application starts with an empty conversation.

User and assistant messages are stored using a role/content structure:

```json
{
  "role": "user",
  "content": "Example question"
}
```

and:

```json
{
  "role": "assistant",
  "content": "Example response"
}
```

### Environment Variable Security

The OpenAI API key is retrieved through:

```python
os.getenv("OPENAI_API_KEY")
```

The actual API key is stored in a local `.env` file rather than being embedded directly in the Python source code.

The `.env` file is excluded from version control through `.gitignore`.

## Technologies Used

* Python
* Streamlit
* OpenAI API
* GPT-4.1 Mini
* python-dotenv
* JSON
* Git / GitHub

## Project Structure

```text
Personal-AI-Assistant/
│
├── .gitignore
├── .env.example
├── README.md
├── app.py
├── requirements.txt
│
└── screenshots/
```

### Core Files

**`app.py`**

The main application responsible for:

* Loading environment variables
* Initializing the OpenAI client
* Creating the Streamlit interface
* Loading conversation memory
* Sending messages to the OpenAI API
* Displaying AI responses
* Saving conversation history

**`requirements.txt`**

Contains the application's direct Python dependencies:

```text
streamlit
openai
python-dotenv
```

**`.env.example`**

Provides an example of the environment variable required by the application without exposing the actual API key.

**`memory.json`**

Stores local conversation history.

This file is intentionally excluded from the public repository because it can contain personal conversation data.

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd Personal-AI-Assistant
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the OpenAI API key

Create a local `.env` file based on `.env.example`:

```text
OPENAI_API_KEY=your_openai_api_key_here
```

Replace the placeholder with your own API key.

**Never commit the real `.env` file to GitHub.**

### 5. Run the application

```bash
streamlit run app.py
```

Streamlit will provide a local web address where the assistant can be accessed through a browser.

## Security and Privacy

The project uses environment variables to prevent API credentials from being hard-coded into the application.

The repository excludes:

* `.env` files
* API credentials
* Local conversation memory
* Virtual environments
* Python cache files
* Local editor configuration

The application's `memory.json` file can contain user conversations and therefore remains local rather than being published with the project.

## Screenshots

The `screenshots/` directory contains visual documentation of the project, including the application interface, AI interaction, conversation memory, and project workflow.

## Skills Demonstrated

This project demonstrates practical experience with:

* Python application development
* Streamlit web application development
* OpenAI API integration
* Large language model integration
* Environment variable management
* JSON data persistence
* Conversation memory
* API-based application architecture
* Virtual environments
* Dependency management
* Git/GitHub project organization

## Project Goals

The primary goal of this project was to build a functional AI assistant from the ground up while learning how to connect a Python application to a large language model.

The project also provided practical experience with maintaining conversation state and safely managing API credentials.

## Future Development

Potential future improvements include:

* More advanced conversation memory
* User-configurable assistant behavior
* Task and reminder management
* Improved conversation history controls
* Persistent user preferences
* Additional AI tools and capabilities
* Local LLM support
* More advanced Streamlit interface features

## Author

**Bradley Lueking**

Cybersecurity | AI | Security Operations | GRC

This project was developed as part of a hands-on technical portfolio demonstrating practical application development and AI integration.
