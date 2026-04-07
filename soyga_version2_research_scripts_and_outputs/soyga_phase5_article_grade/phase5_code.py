import re, itertools

FIB = [1,1,2,3,5,8]

def clean(s):
    return re.sub(r"[^A-Z]", "", s.upper())

def ordinal_extract(source, ords):
    return "".join(source[i-1] for i in ords)

def find_sequences_for_target(source, target, cap=500):
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
    diffs = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    return {
        "span": max(seq) - min(seq),
        "direction_changes": sum((diffs[i]*diffs[i-1] < 0) for i in range(1,len(diffs))),
        "fib_checksum": sum(a*b for a,b in zip(seq,FIB)),
        "fib_mod23": sum(a*b for a,b in zip(seq,FIB)) % 23,
        "sum_mod23": sum(seq) % 23,
    }