# business_rules.py
# Author: Gia Nguyen

APPROVAL_LIMIT = 1000 # module level constant

def calculate_total(price: float, quantity: int) -> float:
    """Return total cost including 7% tax, """
    return price * quantity * 1.07

def requires_review(amount: float) -> bool:
    """Return True if amount exceeds approval limit, """
    return amount > APPROVAL_LIMIT

def get_approval_tier(amount: float) -> str:
    """Return the aproval routhing tier """
    if amount <= 500:
        return 'auto'
    elif amount <= 2000:
        return 'manager'
    else:
        return 'director'

def apply_discount(price: float, pct:float) -> float:
    """Return price after discount, pct is 0-100"""
    return price * (1 - pct / 100)

