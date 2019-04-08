class Wiki(object):
    @classmethod
    def list(cls, api, namespace):
        return api.wiki.list(
            projectIdOrKey=namespace.project_id_or_key
        )

    @classmethod
    def get(cls, api, namespace):
        return api.wiki.get(
            wikiId=namespace.wiki_id
        )

    @classmethod
    def add(cls, api, namespace):
        raise NotImplementedError

    @classmethod
    def update(cls, api, namespace):
        raise NotImplementedError
