
from pypdf import PdfReader
import re
from itertools import product

PDF_PATH = "The Book of Soyga - Jane Kupin.pdf"

def sanitize(s: str) -> str:
    return ''.join(ch for ch in s.upper() if ch.isalpha())

def extract_rows(reader):
    txt = reader.pages[549].extract_text()
    lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
    start = lines.index("Agla Primogenitus On")
    rows = []
    for ln in lines[start:start+23]:
        parts = ln.replace('{Ely}','').replace('{Eloy}','').split()
        rows.append(parts[:3])
    return rows

def extract_table_specs(reader):
    text = ' '.join((reader.pages[i].extract_text() or '') for i in range(550, 555))
    text = re.sub(r'\s+', ' ', text)
    matches = list(re.finditer(r'take the ([^\.]{10,180}?) and join them in one.*?table ([A-Za-z]+)', text))
    specs = []
    for idx, m in enumerate(matches, start=1):
        nums = [int(x) for x in re.findall(r'(\d+)(?:st|nd|rd|th)', m.group(1).split('{')[0])]
        specs.append({"index": idx, "ocr_ordinals": nums, "table_name": m.group(2)})
    return specs

def best_combo(source, target, approx):
    pos_lists = [[i+1 for i,c in enumerate(source) if c == ch] for ch in target]
    if any(not pl for pl in pos_lists):
        return None
    best = None
    for combo in product(*pos_lists):
        m = min(len(combo), len(approx))
        score = sum(abs(combo[i] - approx[i]) for i in range(m)) + 10 * abs(len(combo) - len(approx))
        if best is None or score < best[0]:
            best = (score, combo)
    return best[1]

if __name__ == "__main__":
    reader = PdfReader(PDF_PATH)
    rows = extract_rows(reader)
    specs = extract_table_specs(reader)
    concat = [''.join(r).upper() for r in rows]
    for row, spec in zip(concat, specs):
        combo = best_combo(row, sanitize(spec["table_name"]), spec["ocr_ordinals"])
        print(spec["index"], spec["table_name"], combo)
