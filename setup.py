from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="1.0.0",
    description="A Python package for detecting emotions using Watson NLP API",
    author="Daniel A. Gallardo",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    python_requires=">=3.11",
)