# Smart Resume Parser

A Python application that extracts structured information from resumes in PDF and DOCX formats using spaCy, PyMuPDF, and python-docx. The application provides a web interface built with Streamlit for easy interaction.

## Features

- Support for PDF and DOCX resume formats
- Extracts key information:
  - Skills
  - Education history
  - Work experience
- Clean and intuitive web interface
- Export parsed data to JSON or CSV formats

## Installation

1. Clone this repository:
```powershell
git clone <repository-url>
cd resume_parser
```

2. Install the required packages:
```powershell
pip install -r requirements.txt
```

3. Download the spaCy language model:
```powershell
python -m spacy download en_core_web_sm
```

## Usage

1. Start the Streamlit application:
```powershell
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Upload a resume in PDF or DOCX format

4. View the extracted information and export it in your preferred format

## Running tests (generate sample resumes)

To generate 5 sample DOCX resumes and run the parser against them (this will create JSON and CSV outputs in `tests/outputs`):

```powershell
# Generate 5 test resumes
python tests/generate_test_resumes.py

# Run the test runner to parse resumes and write outputs
python tests/run_tests.py
```

The outputs will be written to `tests/outputs` as `resume_1.json`, `resume_1.csv`, etc.

Note: outputs now include the input file suffix so DOCX and PDF parses won't overwrite each other. Example output names:

```
resume_1_docx.json
resume_1_docx.csv
resume_1_pdf.json
resume_1_pdf.csv
```

Parser improvements:
- Contact extraction: emails and phone numbers are now captured in the parsed output under the `contact` key.
- Skills: improved matching using spaCy PhraseMatcher for higher accuracy.
- Education and Experience: improved heuristics to capture degrees, institutions, and date-based experience blocks.

The Streamlit UI (`app.py`) was updated to show contact info and the parsed raw text, and export CSV/JSON that includes contact fields.

## Project Structure

```
resume_parser/
├── src/
│   └── parser.py      # Core resume parsing logic
├── tests/
│   ├── resumes/       # Generated test resumes (DOCX)
│   └── outputs/       # Generated parse outputs (JSON/CSV)
├── uploads/           # Temporary storage for uploaded files
├── app.py            # Streamlit web interface
└── README.md         # Project documentation
```

## Requirements

- Python 3.8+
- spaCy
- PyMuPDF
- python-docx
- Streamlit
- pandas

## Reproducible install

A `requirements.txt` file is included for easy environment setup. From the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

If you don't want to create a virtualenv, you can install packages system-wide, but a virtualenv is recommended.

CI
--
A GitHub Actions workflow is included at `.github/workflows/ci.yml` and runs `pytest` on push/PR. If you want a status badge in this README, replace `<owner>` and `<repo>` below with your repository information and add the markdown to the top of this file:

```
[![CI](https://github.com/<owner>/<repo>/actions/workflows/ci.yml/badge.svg)](https://github.com/<owner>/<repo>/actions/workflows/ci.yml)
```

