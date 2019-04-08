from urllib.parse import parse_qs

class Issue(object):
    @classmethod
    def list(cls, api, namespace):
        if namespace.query is not None:
            qs = namespace.query\
                .replace(' ', '')\
                .replace('\t', '')\
                .replace('\n', '')
            q = parse_qs(qs)
            return api.issue.list(**q)
        else:
            return api.issue.list()

    @classmethod
    def get(cls, api, namespace):
        return api.issue.get(
            issueIdOrKey=namespace.issue_id_or_key
        )

    @classmethod
    def add(cls, api, namespace):
        raise NotImplementedError

    @classmethod
    def update(cls, api, namespace):
        raise NotImplementedError

