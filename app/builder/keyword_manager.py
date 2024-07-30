class KeywordManager:
    def __init__(self):
        self.keywords = {
            "Environmental": ["temperature", "humidity", "air quality"],
            "Resource": ["library", "cafeteria", "study rooms"],
            "Academic": ["assignments", "classes", "grades"],
            "Event": ["campus events", "clubs", "workshops"],
            "Health": ["wellness tips", "fitness", "mental health"]
        }

    def get_keywords(self):
        return self.keywords

    def add_keyword(self, category, keyword):
        if category in self.keywords:
            self.keywords[category].append(keyword)
        else:
            self.keywords[category] = [keyword]

    def remove_keyword(self, category, keyword):
        if category in self.keywords and keyword in self.keywords[category]:
            self.keywords[category].remove(keyword)
