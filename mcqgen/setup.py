from setuptools import setup, find_packages

setup(
    name="mcqgen",
    version="0.1.0",
    author="Sanjay Vishwakarma",
    author_email="sanjay.vishwakarma01072@gmail.com",
    description="A package for generating multiple-choice questions using OpenAI's GPT-3.5",
    install_requires=[
        "openai",
        "langchain",
        "streamlit",
        "python-dotenv",
        "pyPDF2",
    ],
    packages=find_packages(),
)