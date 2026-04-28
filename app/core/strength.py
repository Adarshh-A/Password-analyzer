def classify_strength(entropy, breached):
    if entropy < 40:
        return "Weak"
    elif entropy < 60:
        return "Medium"
    else:
        if breached:
            return "Medium"   # ⚠️ downgrade instead of forcing weak
        return "Strong"
