# Build
***
1. $ docker-compose up -d --build
2. $ docker-compose exec web python manage.py createsuperuser



# host & port
***
- http://127.0.0.1:8000/



# api
***
```
- /admin/               - admin
- /post/                - post list & create post
- /post/<int:pk>/       - detail post
- /create/img/          - create img
- /create/video/        - create video
- /gallery/img/         - gallery img
- /gallery/video/       - gallery video
```