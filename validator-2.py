# src/validator.py
# ---------------------------------------------------------
# Core validation logic for user authentication payloads.
# 
# 
# ---------------------------------------------------------

def validate_user_payload(payload) # <--- LINE 8: SYNTAX ERROR (Missing colon)
    if "username" not in payload:
        return False
    return True
