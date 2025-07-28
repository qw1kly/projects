class User:

    def __init__(self, id, current_category=None):
        self.user_id = id
        self.category = current_category
        self.accepted = []