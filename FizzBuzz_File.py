import numpy as np

def FizzBuzz(start, finish):
    """
    Vectorized FizzBuzz implementation using NumPy.
    No loops allowed.
    """
    # 1. Create an array of numbers from start to finish (inclusive)
    # We use dtype=object so the array can hold both strings and integers
    numvec = np.arange(start, finish + 1)
    objvec = np.array(numvec, dtype=object)
    
    # 2. Define boolean masks for multiples of 3, 5, and 15
    is_fizz = (numvec % 3 == 0)
    is_buzz = (numvec % 5 == 0)
    is_fizzbuzz = (numvec % 15 == 0)
    
    # 3. Apply the replacements using the masks
    # Order matters: replace specific cases (15) after or alongside general cases
    objvec[is_fizz] = "fizz"
    objvec[is_buzz] = "buzz"
    objvec[is_fizzbuzz] = "fizzbuzz"
    
    return objvec

# --- Test the function ---
# Example: FizzBuzz from 31 to 45
result = FizzBuzz(31, 45)
print(result)