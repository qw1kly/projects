class Basket:

    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def delete_item(self):
        pass