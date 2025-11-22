import sys
from pathlib import Path
import pytest

# ensure project root is importable
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.parser import ResumeParser

DATA_DIR = ROOT / 'tests' / 'resumes'

@pytest.fixture(scope='module')
def parser():
    return ResumeParser()

def test_parse_docx_basic(parser):
    file = DATA_DIR / 'resume_1.docx'
    assert file.exists(), f"Test file missing: {file}"
    results = parser.parse_resume(file)
    # basic keys
    assert 'text' in results
    assert 'skills' in results
    assert 'education' in results
    assert 'experience' in results
    assert 'contact' in results
    # expect python to be detected in resume_1
    skills = [s.lower() for s in results.get('skills', [])]
    assert any('python' in s for s in skills), f"Expected python in skills, got: {skills}"

def test_parse_pdf_basic(parser):
    file = DATA_DIR / 'resume_1.pdf'
    assert file.exists(), f"Test file missing: {file}"
    results = parser.parse_resume(file)
    assert 'text' in results and results['text']
    assert isinstance(results.get('contact'), dict)

if __name__ == '__main__':
    pytest.main(['-q', str(Path(__file__) )])