#!/usr/bin/env python3
import os
import openai
import subprocess

# Get the OpenAI API key from the environment variable
openai.api_key = os.environ.get('AI_COMMIT_OPEN_AI_KEY')

def parse_git_diff():
    try:
        # Use subprocess to execute the `git diff --cached` command and capture the output
        diff_output = subprocess.check_output(['git', 'diff', '--cached'])
        diff_lines = diff_output.decode('utf-8').splitlines()

        # Filter out lines that start with '+', '-', '@@', and 'diff' to keep only the relevant changes
        filtered_diff_lines = [line for line in diff_lines if line.startswith(('+', '-', '@@'))]
        prompt = f"Generate a commit message based on these staged changes made:\n\n{diff_lines}\n\nComplete Git diff:\n\n{diff_output}\n\nGenerated Commit Message:"
    except subprocess.CalledProcessError:
        # If no staged changes, use `git diff` to capture all changes in the working directory
        diff_output = subprocess.check_output(['git', 'diff'])
        prompt = f"Generate a commit message based on the following changes made:\n\n{diff_output.decode('utf-8')}\n\nGenerated Commit Message:"

    return prompt

def generate_commit_message(prompt):
    # Use OpenAI API to generate the commit message based on the Git diff

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
    )
    return response['choices'][0]['text']

def main():
    git_diff = parse_git_diff()
    commit_message = generate_commit_message(git_diff)
    print(commit_message)

if __name__ == '__main__':
    main()
