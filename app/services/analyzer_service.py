from app.core.entropy import calculate_entropy
from app.core.strength import classify_strength
from app.security.reuse import is_reused, save
from app.security.breach import is_breached
from app.models.password_model import PasswordResult
from app.utils.logger import log_event


def analyze(password):
    entropy = calculate_entropy(password)
    breached = is_breached(password)
    strength = classify_strength(entropy, breached)
    reused = is_reused(password)

    feedback = []

    if entropy < 50:
        feedback.append("Increase length and complexity")
    if breached:
        feedback.append("Password found in breach database")
    if reused:
        feedback.append("Password was used before")

    if not reused:
        save(password)

    result = PasswordResult(
        password,
        strength,
        entropy,
        feedback,
        reused,
        breached
    )

    # 🔥 IMPORTANT: must be inside function
    log_event(password, result.to_dict())

    return result
