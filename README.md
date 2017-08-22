# docker-etude

Build Docker Compositions, Especially For Local Development

[![Circle CI](https://circleci.com/gh/globality-corp/docker-etude/tree/develop.svg?style=svg)](https://circleci.com/gh/globality-corp/docker-etude/tree/develop)

## Developing locally

* `mkvirtualenv -p python3 dockeretude`
* `pip install tox`
* `pip install -e .`

## Example

LocalStack:

```
etude localstack > docker-compose.yml
```

ECS:

```
etude ecs > docker-compose.yml
```


# TODO:

 -  Mutation: extension/transformation
 -  Module System (for sources, mutations)
 -  Environment editing abstraction
 -  CLI configuration
