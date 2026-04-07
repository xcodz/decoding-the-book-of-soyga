import re, itertools
triples = [("AGLA","PRIMOGENITUS","ON")]
FIB = [1,1,2,3,5,8]
PI_DIGITS = [3,1,4,1,5,9]

def clean(s): return re.sub(r"[^A-Z]", "", s.upper())
def ordinal_extract(source, ords): return "".join(source[i-1] for i in ords)
def positions_for_target(source, target, cap=20000):
    pos_lists=[]
    for ch in target:
        pos=[i+1 for i,c in enumerate(source) if c==ch]
        if not pos: return []
        pos_lists.append(pos)
    seqs=[]
    for combo in itertools.product(*pos_lists):
        seqs.append(combo)
        if len(seqs)>=cap: break
    return seqs