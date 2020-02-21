class Poll:
    def __init__(self, poll_id, option_ids):
        self.poll_id = poll_id
        self.values = option_ids

    def __repr__(self):
        return str(self.__dict__)
