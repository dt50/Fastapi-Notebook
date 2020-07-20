# Fastapi-Notebook

## Want to use this project?

Build the images and run the containers:

```sh
$ docker-compose up -d --build
```

Api URLS:

1. [http://localhost:8000/docs](http://localhost:8000/docs) - Api docs
1. [http://localhost:8000/create-user](http://localhost:8000/create-user) - Create a user account
1. [http://localhost:8000/create-user-note](http://localhost:8000/create-user-note) - Create note for user
1. [http://localhost:8000/get-user-notes](http://localhost:8000/get-user-notes) - Get all user notes
1. [http://localhost:8000/change-note/{id}](http://localhost:8000/change-note/{id}) - Change user note by id
1. [http://localhost:8000/delete-note/{id}](http://localhost:8000/delete-note/{id}) - Delete user note by id 