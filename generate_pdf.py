name: Generate PDF

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'  # Specify the Python version you want to use

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install reportlab

    - name: Run script
      run: |
        python generate_pdf.py

    - name: Upload PDF
      uses: actions/upload-artifact@v3
      with:
        name: generated-pdf
        path: Padaatik_Collaboration_Policy.pdf
