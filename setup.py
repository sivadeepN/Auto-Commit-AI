from setuptools import setup

setup(
    name='ai-commit',
    version='1.0.0',
    description='Auto-generate commit messages using OpenAI GPT-3.',
    author='Sivadeep Nallana',
    packages=[''],
    install_requires=[
        'openai',
        # Add any other dependencies required by your script
    ],
    entry_points={
        'console_scripts': [
            'ai-commit = app:main',
        ],
    },
)
