class PasswordResult:
    def __init__(self, password, strength, entropy, feedback, reused, breached):
        self.password = password
        self.strength = strength
        self.entropy = entropy
        self.feedback = feedback
        self.reused = reused
        self.breached = breached

    def to_dict(self):
        return {
            "strength": self.strength,
            "entropy": self.entropy,
            "feedback": self.feedback,
            "reused": self.reused,
            "breached": self.breached
        }
