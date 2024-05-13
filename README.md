# Welcome to Project python-visitors!

## What is a project?

A project is meant to be represent a monorepo of applications that are related to each other.

See [Documentation](https://docs.codefly.dev/concepts/project/) for more information.

## Structure of the project

A project is structured as follows:
```shell
.
├── applications
│   └── foo
│       └── services
│           └── api
│           └── storage
│       └── ...
│   └── bar
│       └── services
│           └── web
│           └── auth
├── configurations
│   └── ...
├── deployments
│   └── ....
```
where `foo` and `bar` are applications of the project.

`configurations` contains the shared configurations of the project.

`deployments` contains the deployment manifests of the project for self-managed deployments.
