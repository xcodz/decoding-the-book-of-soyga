import re, itertools

triples = [
    ("AGLA","PRIMOGENITUS","ON"),
    ("REDEMPTOR","ELOY","ELY"),
    ("IUSTORUM","GENITOR","BON"),
    ("MESSYAS","PANTO","OS"),
    ("VERITAS","THEON","SPIRITUS"),
    ("AGIOS","PARACLITUS","ALPHA"),
    ("DAMADAIS","TRINUS","SACERDOS"),
]

targets = [
    "NISRAM","MARSIN",
    "ROELER","IOMIOT","RAOSAC","RSADUA","SDUOLO","ADAMIS","ILIOSU","OYNIND"
]

FIB = [1,1,2,3,5,8]

def clean(s):
    return re.sub(r"[^A-Z]", "", s.upper())

def ordinal_extract(source, ords):
    return "".join(source[i-1] for i in ords)

def find_sequences(source, target, cap=2000):
    pos_lists = []
    for ch in target:
        pos = [i+1 for i,c in enumerate(source) if c == ch]
        if not pos:
            return []
        pos_lists.append(pos)
    seqs = []
    for combo in itertools.product(*pos_lists):
        seqs.append(combo)
        if len(seqs) >= cap:
            break
    return seqs

def seq_features(seq):
    diffs = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    direction_changes = sum((diffs[i] * diffs[i-1] < 0) for i in range(1, len(diffs)))
    return {
        "sum_mod23": sum(seq) % 23,
        "span": max(seq) - min(seq),
        "direction_changes": direction_changes,
        "fib_mod23": sum(a*b for a,b in zip(seq, FIB)) % 23,
    }