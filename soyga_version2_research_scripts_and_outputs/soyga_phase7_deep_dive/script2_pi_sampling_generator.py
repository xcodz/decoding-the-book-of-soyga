alphabet = "ABCDEFGHIKLMNOPQRSTUXYZ"
idx = {c:i for i,c in enumerate(alphabet)}
inv = {i:c for i,c in enumerate(alphabet)}
q = len(alphabet)
def clean(s):
    import re
    return re.sub(r"[^A-Z]", "", s.upper())
def gen_table(seed, n=36):
    seed = "".join(c for c in clean(seed) if c in alphabet)
    row = (seed * ((n // len(seed))+1))[:n]
    table = [list(row)]
    for i in range(1,n):
        prev = table[-1]
        new = []
        for j in range(n):
            new.append(inv[(idx[prev[j]] + idx[prev[j-1]]) % q])
        table.append(new)
    return table