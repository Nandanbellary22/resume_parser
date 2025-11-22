import json
from pathlib import Path
import sys
import pandas as pd

# Ensure project root is on sys.path so `from src.parser import ResumeParser` works
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.parser import ResumeParser

IN = Path("tests/resumes")
OUT = Path("tests/outputs")
OUT.mkdir(parents=True, exist_ok=True)

parser = ResumeParser()
files = sorted(IN.glob("*.docx")) + sorted(IN.glob("*.pdf"))

for file in files:
    print("Parsing:", file)
    try:
        results = parser.parse_resume(file)
    except Exception as e:
        print(f"Error parsing {file}: {e}")
        continue

    # Save JSON (include file suffix to preserve separate outputs)
    suffix = file.suffix.lstrip('.')
    json_path = OUT / f"{file.stem}_{suffix}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    # Save CSV (flat)
    flat = {
        'file': file.name,
        'Skills': ", ".join(results.get('skills', [])),
        'Education': "; ".join(results.get('education', [])),
        'Experience': "; ".join(results.get('experience', [])),
        'Text': results.get('text', '')[:1000]
    }
    df = pd.DataFrame([flat])
    csv_path = OUT / f"{file.stem}_{suffix}.csv"
    df.to_csv(csv_path, index=False)

    print(f"Wrote: {json_path}, {csv_path}")

print("Done")