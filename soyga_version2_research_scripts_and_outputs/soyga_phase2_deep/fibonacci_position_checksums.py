
FIB = [1,1,2,3,5,8]

def fib_checksum(positions, modulus=23):
    total = sum(FIB[i] * positions[i] for i in range(min(len(positions), 6)))
    return total, total % modulus

if __name__ == "__main__":
    samples = {
        "Nisram": (12,7,16,6,1,8),
        "Roeler": (9,15,2,11,4,1),
        "Iomiot": (1,14,8,12,17,4),
    }
    for name, pos in samples.items():
        print(name, fib_checksum(pos))
