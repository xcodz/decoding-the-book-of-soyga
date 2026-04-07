import random, itertools, re
random.seed(7)
def clean(s): return re.sub(r"[^A-Z]", "", s.upper())
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