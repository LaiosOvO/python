

#### roadmap
https://naemazam.medium.com/step-by-step-python-django-roadmap-for-one-year-along-with-learning-resources-eb5138d8278f


#### first app

```bash
mkdir djangotutorial

django-admin startproject mysite djangotutorial

# 创建项目
cd djangotutorial
python manage.py runserver

# 创建app
python manage.py startapp polls


# 数据迁移
python manage.py makemigrations polls

python manage.py migrate

python manage.py sqlmigrate polls 0001

# 管理页面
python manage.py createsuperuser

```


