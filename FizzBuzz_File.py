import numpy as np

# --- 1. Bond Price Function ---
def getBondPrice(y, face, couponRate, m, ppy=1):
    r = y / ppy
    c = (face * couponRate) / ppy
    n = m * ppy
    periods = np.arange(1, n + 1)
    # Vectorized PV calculation
    bond_price = np.sum(c / (1 + r)**periods) + (face / (1 + r)**n)
    return bond_price

# --- 2. Bond Duration Function ---
def getBondDuration(y, face, couponRate, m, ppy=1):
    r = y / ppy
    c = (face * couponRate) / ppy
    n = m * ppy
    t = np.arange(1, n + 1)
    cf = np.full(n, c)
    cf[-1] += face
    pvcf = cf / (1 + r)**t
    bond_price = np.sum(pvcf)
    w = pvcf / bond_price
    # Annual duration = (Sum of weighted periods) / payments per year
    duration = np.sum(w * t) / ppy
    return duration

# --- 3. FizzBuzz Function (The one failing) ---
def FizzBuzz(start, finish):
    # Must include 'finish', so we use finish + 1
    numvec = np.arange(start, finish + 1)
    # Must use dtype=object to mix strings and ints
    objvec = np.array(numvec, dtype=object)
    
    # Create masks
    mask3 = (numvec % 3 == 0)
    mask5 = (numvec % 5 == 0)
    mask15 = (numvec % 15 == 0)
    
    # Apply replacements in specific order
    objvec[mask3] = "fizz"
    objvec[mask5] = "buzz"
    objvec[mask15] = "fizzbuzz"
    
    return objvec