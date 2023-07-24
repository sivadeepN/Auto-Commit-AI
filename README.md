# AI Commit CLI Tool

## Overview

The AI Commit CLI tool is a command-line utility that automatically generates commit messages using OpenAI GPT-3. It helps developers quickly create descriptive and accurate commit messages based on their Git changes.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your_username/ai-commit.git
Navigate to the project directory:
    
`cd ai-commit
`
Create a virtual environment (optional but recommended):

`python3 -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
``
Install the required dependencies using pip:


`pip install -r requirements.txt
`
Make the script executable:
`chmod +x app.py
`Set up your OpenAI API key:

To use the AI Commit CLI tool, you need an OpenAI API key. You can obtain an API key by signing up for the OpenAI service and creating an API key in the OpenAI web interface. See OpenAI API Keys for details.

Once you have your API key, set it as an environment variable in your shell:
`export AI_COMMIT_OPENAI_KEY=your_openai_api_key_here
`
or add it in your.bashrc or .zshrc
Replace AI_COMMIT_OPENAI_KEY with your actual OpenAI API key. Alternatively, you can add this line to your shell's configuration file (e.g., .bashrc, .zshrc) to set the API key permanently.
