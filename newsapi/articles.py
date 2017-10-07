from newsapi.base_news import BaseNews

class Articles(BaseNews):
    def __init__(self, API_KEY):
        super(Articles, self).__init__(API_KEY)

    @property
    def endpoint(self):
        return "https://newsapi.org/v1/articles"

    def get(self, source, sort_by="top", attributes_format=True):
        self.payload['source'] = source
        self.payload['sortBy'] = sort_by

        return super(Articles, self).get(attributes_format)

    def get_by_top(self, source):
        return self.get(source, sort_by="top")

    def get_by_latest(self, source):
        return self.get(source, sort_by="latest")

    def get_by_popular(self, source):
        return self.get(source, sort_by="popular")
