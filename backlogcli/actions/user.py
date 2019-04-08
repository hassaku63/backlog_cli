class User(object):
    @classmethod
    def list(cls, api, namespace):
        return api.user.list()

    @classmethod
    def get(cls, api, namespace):
        return api.user.get(
            userId=namespace.user_id
        )

    @classmethod
    def add(cls, api, namespace):
        raise NotImplementedError

    @classmethod
    def update(cls, api, namespace):
        raise NotImplementedError
