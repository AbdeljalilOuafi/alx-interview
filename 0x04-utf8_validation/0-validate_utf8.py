#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    UTF-8 Validation
    """
    available_bites = 0
    for b in data:
        if available_bites == 0:
            if len(str(bin(b))) == 10 and str(bin(b)).startswith('0b110'):
                available_bites = 1
            elif len(str(bin(b))) == 10 and str(bin(b)).startswith('0b1110'):
                available_bites = 2
            elif len(str(bin(b))) == 10 and str(bin(b)).startswith('0b11110'):
                available_bites = 3
            elif str(bin(b))[::-1][7] == '1':
                available_bites = 1
                break
        else:
            if not str(bin(b)).startswith('0b10'):
                available_bites = 1
                break
            available_bites -= 1
    return available_bites == 0
