# ماژول اشتراک پریمیوم (فعلاً غیرفعال ولی آماده)
class PremiumUser:
    def __init__(self, user_id):
        self.user_id = user_id
    def is_active(self):
        return False  # future