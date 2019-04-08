# backlog_cli
Python3製のBacklog CLI

# Usage

Installation

```bach
git clone git@github.com:hassaku63/backlog_cli.git
cd /path/to/this/package
pip install .

# or
pip install git+git://github.com/hassaku63/backlog_cli@<BRANCH_NAME>
```

## Credential

APIの認証情報は `--conf CONF` で指定するか、環境変数で定義する

```yaml
# conf.yml
backlog:
  space: space
  api_key: api_key
``` 

```bash
# env
BACKLOG_SPACE=space
BACKLOG_API_KEY=api_key
```

# Example

```
$ backlog -h
usage: backlog [-h] [--conf CONF] {project,user,issue,iss,wiki} ...

Backlog CLI (beta)

positional arguments:
  {project,user,issue,iss,wiki}

optional arguments:
  -h, --help            show this help message and exit
  --conf CONF
```

```
$ backlog project list | jq -r '.[0]'
{
  "id": 0123456789,
  "projectKey": "TEST_PROJECT",
  "name": "HOGE",
  "chartEnabled": true,
  "subtaskingEnabled": true,
  "projectLeaderCanEditProjectLeader": false,
  "useWikiTreeView": false,
  "textFormattingRule": "backlog",
  "archived": false,
  "displayOrder": 0123456789
}
```

```
$ backlog wiki get --wiki-id 0123456789 | jq -r '.content'
# README
（wiki id = 0123456789 の本文）
```


# See also

https://github.com/hassaku63/pbl

|key|value|
|:---|:---|
|Slack internal team|#ext-dev-backlog-util @hashimoto|
|Twitter|https://twitter.com/hassaku_63|
