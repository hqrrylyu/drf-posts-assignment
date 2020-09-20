# drf-posts-assignment

[DEMO](https://boiling-cliffs-03671.herokuapp.com/)

[Postman collection](https://www.postman.com/collections/2655fc64dd609a8c0c6f)

## Getting started

### Prerequisites

- [docker](https://docs.docker.com/engine/install/)
- [docker-compose](https://docs.docker.com/compose/install/)

### Installation

Clone the repository:

`git clone https://github.com/hqrrylyu/drf-posts-assignment.git`

Provide `.env` file in the root folder:

```
DJANGO_SETTINGS_MODULE=config.settings.local
SECRET_KEY=randomsecretkey
ALLOWED_HOSTS=*
POSTGRES_PASSWORD=randompostgrespassword
DATABASE_URL=postgres://postgres:randompostgrespassword@db:5432/postgres
REDIS_URL=redis://redis:6379
```

Run the stack:

`docker-compose up`

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
