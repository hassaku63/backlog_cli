class Project(object):
    @classmethod
    def list(cls, api, namespace):
        """
        https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-project-list/

        # Arguments
        api: (bpl.backlog.base.BacklogAPI) Required
        namespace.archived: (bool) Optional. default = False

        :param namespace: argparse.namespace
        :return:
        """
        archived = namespace.archived if 'archived' in namespace else False

        return api.project.list(archived=archived)
    
    @classmethod
    def create(cls, api, namespace):
        raise NotImplementedError
    
    @classmethod
    def get(cls, api, namespace):
        return api.project.get(
            projectIdOrKey=namespace.project_id_or_key
        )

    @classmethod
    def update(cls, api, namespace):
        raise NotImplementedError

    @classmethod
    def list_users(cls, api, namespace):
        return api.project.list_users(
            projectIdOrKey=namespace.project_id_or_key,
            excludeGroupMembers=namespace.exclude_group_members
        )

    @classmethod
    def list_issue_types(cls, api, namespace):
        return api.project.list_issue_types(
            projectIdOrKey=namespace.project_id_or_key
        )

    @classmethod
    def add_issue_type(cls, api, namespace):
        raise NotImplementedError

    @classmethod
    def delete_issue_type(cls, api, namespace):
        raise NotImplementedError

    @classmethod
    def list_categories(cls, api, namespace):
        return api.project.list_categories(
            projectIdOrKey=namespace.project_id_or_key
        )

    @classmethod
    def add_category(cls, api, namespace):
        raise NotImplementedError

    @classmethod
    def update_category(cls, api, namespace):
        raise NotImplementedError
    
    def delete_category(cls, api, namespace):
        raise NotImplementedError

