# Blog Application

This is a simple web application for a blog. It allows users to register, login, create, update, and delete posts. 

## Installation and Setup

1. Install the dependencies:
   

       pip install -r requirements.txt
   

2. Initialize the database:
   

        python run.py
   

3. Run the application:
   
        flask run


## Usage

- Register a new account by visiting the `/register` page.
- Login to your account by visiting the `/login` page.
- Create a new blog post by visiting the `/post/new` page.
- View all blog posts on the homepage at `/`.
- View a specific blog post by clicking on its title.
- Update or delete a blog post if you are the author.
- Logout by visiting the `/logout` page.

## Structure

The blog application consists of the following files:

- `routes.py`: Contains the Flask routes for different pages and actions.
- `models.py`: Defines the database models for users and blog posts.
- `forms.py`: Defines the Flask-WTF forms for user registration, login, profile update, and post creation.
- `__init__.py`: Initializes the Flask application, database, bcrypt, and login manager.
- `run.py`: Runs the Flask application and creates the database tables if they don't exist.

## Dependencies

The project uses the following Python dependencies:

- Flask: a lightweight web framework for Python.
- Flask-WTF: a Flask extension for handling forms.
- Flask-Login: a Flask extension for managing user authentication.
- Flask-SQLAlchemy: a Flask extension for interacting with databases.
- Flask-Bcrypt: a Flask extension for hashing passwords.
- WTForms: a library for creating and validating forms in Python.


# برنامه وب وبلاگ

این یک برنامه وب ساده برای یک وبلاگ است. این به کاربران اجازه می دهد تا ثبت نام کنند ، وارد شوند ، مطلبی بسازند، به روز رسانی کنند و حذف کنند.

## نصب و راه‌اندازی

1. پکیج های لازم را از فایل requirements.txt نصب کنید:


```
pip install -r requirements.txt
```

2. پایگاه داده را اینیشیال کنید:


```
python run.py
```

3. برنامه را اجرا کنید:


```
flask run
```

## استفاده

- بازدید از صفحه `/register` برای ثبت نام حساب کاربری جدید.
- بازدید از صفحه `/login` برای ورود به حساب کاربری.
- بازدید از صفحه `/post/new` برای ساختن یک پست وبلاگ جدید.
- مشاهده تمام پست‌های وبلاگ در صفحه اصلی `/`.
- مشاهده یک پست خاص با کلیک بر روی عنوان آن.
- به روز رسانی یا حذف یک پست وبلاگ در صورتی که شما نویسنده آن باشید.
- خروج از حساب کاربری با بازدید از صفحه `/logout`.

## ساختار

برنامه وبلاگ شامل فایل‌های زیر است:

- `routes.py`: شامل مسیرهای Flask برای صفحات و عملیات مختلف است.
- `models.py`: مدل های پایگاه داده برای کاربران و پست های وبلاگ را تعریف می کند.
- `forms.py`: فرم های Flask-WTF برای ثبت نام کاربر ، ورود ، به روز رسانی پروفایل و ایجاد پست را تعریف می کند.
- `__init__.py`: برنامه Flask ، پایگاه داده ، bcrypt و مدیر ورود را مقداردهی اولیه می کند.
- `run.py`: برنامه Flask را اجرا کرده و جداول پایگاه داده را ایجاد می کند اگر وجود نداشته باشد.

## پکیج ها

این پروژه از پکیج های پایتون زیر استفاده می کند:

- Flask: یک چارچوب وب سبک برای پایتون.
- Flask-WTF: یک افزونه Flask برای کنترل فرم ها.
- Flask-Login: یک افزونه Flask برای مدیریت تأیید هویت کاربر.
- Flask-SQLAlchemy: یک افزونه Flask برای تعامل با پایگاه داده.
- Flask-Bcrypt: یک افزونه Flask برای هش کردن رمز عبور.
- WTForms: کتابخانه ای برای ایجاد و اعتبارسنجی فرم ها در پایتون.
### خروج

اگر وارد حساب کاربری خود شده‌اید، می‌توانید با استفاده از دکمه "logout" از حساب خود خارج شوید. با خروج از حساب، به صفحه اصلی هدایت می‌شوید و یک پیام موفقیت نشان داده می‌شود.

با استفاده از این برنامه، می‌توانید یک وبلاگ ساده راه‌اندازی کنید و به طور مداوم پست‌های جدید ایجاد کنید و ویرایش کنید. همچنین می‌توانید پست‌های دیگران را مشاهده کنید و پست‌های مورد علاقه خود را حذف کنید.
