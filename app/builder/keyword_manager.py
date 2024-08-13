class KeywordManager:

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
