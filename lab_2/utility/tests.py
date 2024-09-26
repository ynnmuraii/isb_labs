import math
import mpmath

def frequency_bitwise_test(sequence: str) -> float:
    """
    This function implements a Frequency bitwise test.
    This test evaluates this proximity of the P-value to one

    Args:
        sequence (str): a string containing a sequence of 0 and 1

    Returns:
        float: the P-value for the frequency bitwise test
    """
    try:    
        sum_seq = sum(list(map(lambda x: 1 if x == '1' else -1, sequence)))
        s = abs(sum_seq) / math.sqrt(len(sequence))
        p_value = math.erfc(s / math.sqrt(2))
        
        return p_value
    except Exception as error:
        print("")