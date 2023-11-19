class Post:
    """Stores all information for a post"""
    def __init__(self, post_id, title, subtitle, body):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body