import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    """
    Calculates the bond duration using vectorized operations.
    No loops allowed.
    """
    # 1. Basic periodic parameters
    periodic_yield = y / ppy
    periodic_coupon = (face * couponRate) / ppy
    total_periods = m * ppy
    
    # 2. Create an array of time periods [1, 2, ..., n]
    t = np.arange(1, total_periods + 1)
    
    # 3. Create cash flow vector
    # All periods get the coupon, last period gets the face value added
    cf = np.full(total_periods, periodic_coupon)
    cf[-1] += face
    
    # 4. Calculate Present Value of each cash flow (Vectorized)
    pvcf = cf / (1 + periodic_yield)**t
    
    # 5. Calculate Total Bond Price
    bond_price = np.sum(pvcf)
    
    # 6. Calculate weights (w = pvcf / total_price)
    w = pvcf / bond_price
    
    # 7. Calculate Duration (weighted average of time)
    # Divided by ppy to convert periodic duration back to annual duration
    duration = np.sum(w * t) / ppy
    
    return duration

# --- Test values from your image ---
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1

bond_duration = getBondDuration(y, face, couponRate, m, ppy)
print(f"Bond Duration: {bond_duration:.2f}") 
# Expected Output: 8.51