import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    """
    Calculates the bond price using vectorized operations.
    
    Parameters:
    y          : annual yield to maturity (e.g., 0.03)
    face       : face value of the bond (e.g., 2000000)
    couponRate : annual coupon rate (e.g., 0.04)
    m          : years to maturity (e.g., 10)
    ppy        : payments per year (default is 1)
    """
    
    # Calculate periodic parameters
    r = y / ppy
    c = (face * couponRate) / ppy
    n = m * ppy
    
    # Create an array of periods [1, 2, 3, ..., n]
    periods = np.arange(1, n + 1)
    
    # Calculate the present value of all coupon payments
    # PV = Coupon / (1 + r)^t
    coupon_pvs = c / (1 + r)**periods
    
    # Calculate the present value of the face value (lump sum at the end)
    # PV_face = Face / (1 + r)^n
    face_pv = face / (1 + r)**n
    
    # Total Bond Price = Sum of PV of coupons + PV of face value
    bond_price = np.sum(coupon_pvs) + face_pv
    
    return bond_price

# --- Test Cases based on your image ---

# Case 1: Annual payments (ppy=1)
# Expected result: ~$2,170,604.06
price_annual = getBondPrice(y=0.03, face=2000000, couponRate=0.04, m=10, ppy=1)
print(f"Annual Payment Price: {price_annual:,.2f}")

# Case 2: Semi-annual payments (ppy=2)
# Expected result: ~$2,171,686.39
price_semiannual = getBondPrice(y=0.03, face=2000000, couponRate=0.04, m=10, ppy=2)
print(f"Semi-annual Payment Price: {price_semiannual:,.2f}")