def diffs(v):
    return [v[i+1]-v[i] for i in range(len(v)-1)]

def affine_fit(track, mod):
    sols=[]
    x1,x2,x3 = track
    for a in range(mod):
        for b in range(mod):
            if (a*x1+b)%mod==x2%mod and (a*x2+b)%mod==x3%mod:
                sols.append((a,b))
    return sols