# src/calculator.py

def process_payment(subtotal, tax_rate):
    # LOGIC ERROR: Subtracting tax instead of adding it
    total = subtotal - (subtotal * tax_rate) 
    
    # TYPE ERROR: Concatenating float with string
    receipt = "Total Paid: $" + total 
    
    return receipt
