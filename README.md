# ๐ฐ ๊ณ ๊ฐ ๊ฐ๊ณ๋ถ ์์ฑ ๋ฐ ๊ด๋ฆฌ ๊ธฐ๋ฅ ๊ตฌํ

โ `SECRET_KEY`, token ๋ฐ๊ธ์ ์ํ `ALGORITHM`, `DATABASES`๋ ๋ณด์์ ์ํด ๋ณ๋์ ํ์ผ `my_settings.py`์ ๋ณด๊ดํ์ต๋๋ค.

## ๐ก ERD

<img width="801" alt="แแณแแณแแตแซแแฃแบ 2021-11-18 แแฉแแฎ 6 11 49" src="https://user-images.githubusercontent.com/73830753/142385765-3852e733-d441-45ed-9563-89e4a745e655.png">

## ๐  ์ฌ์ฉ ๊ธฐ์  ๋ฐ ํด

> - Back-End : <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.1-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/MySQL 5.7 -4479A1?style=for-the-badge&logo=MySQL&logoColor=white"/>
> - Deploy : <img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC : <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

## ๐ฉโ๐ป ๊ตฌํ ๊ธฐ๋ฅ

### users

- ์ ์ ๋ ์ด๋ฉ์ผ๊ณผ ๋น๋ฐ๋ฒํธ ์๋ ฅ์ ํตํด ํ์๊ฐ์์ ํ  ์ ์์ต๋๋ค.
- ์ ์ ์ ๋น๋ฐ๋ฒํธ๋ฅผ db์ ์ํธํํ์ฌ ์์ ํ๊ฒ ์ ์ฅํ๊ธฐ ์ํด `bcrypt`๋ฅผ ์ฌ์ฉํ์ต๋๋ค.
- ์ ์ ๊ฐ ๋ก๊ทธ์ธ ์ token์ด ๋ฐ๊ธ๋ฉ๋๋ค.
  - token ๋ฐ๊ธ์ `jwt`๋ฅผ ์ฌ์ฉํ์ฌ ๋ฐ๊ธํ์์ต๋๋ค.
  - token์ ๋ก๊ทธ์์์ ์ํด ๋ฐ๊ธ์ db์ ์ ์ฅ๋ฉ๋๋ค.
- ์ ์  ๋ก๊ทธ์์ ์ db์์ ํ ํฐ์ ์ญ์ ํฉ๋๋ค.
  - ์๋น์ค ์ด์ฉ์ ์ญ์ ๋ ํ ํฐ์ธ์ง ์๋์ง ํ๋จํ ํ ์ญ์ ๋ ํ ํฐ์ผ ์ ์ ์ ๋ ์๋น์ค๋ฅผ ์ด์ฉํ  ์ ์์ต๋๋ค.
  - ์ฌ๋ก๊ทธ์ธ ์ ๋ค์ db์ ํ ํฐ์ด ์ ์ฅ๋๋ฏ๋ก ์ ์ ๋ ์ ์์ ์ผ๋ก ์๋น์ค๋ฅผ ์ด์ฉํ  ์ ์์ต๋๋ค.
  - ๐ค [jwt ๋ก๊ทธ์์์ ๋ํด ๊ณ ๋ฏผํ๋ฉฐ ์ด ๊ธ](https://rimi0108.github.io/django/jwt-logout/)

### moneybooks

- ์ ์ ๋ ๋ก๊ทธ์ธ ์ ๊ฐ๊ณ๋ถ ์๋น์ค๋ฅผ ์ด์ฉํ  ์ ์์ต๋๋ค.
  - ๋ก๊ทธ์ธ ํ์ง ์์ ์ ์๋ฌ๊ฐ ๋ฐ์ํฉ๋๋ค.
- ์ ์ ๋ ๊ฐ๊ณ๋ถ์ ์ฌ์ฉํ ๊ธ์ก, ๋์ ์๊ธ/์ถ๊ธ ์ฌ๋ถ, ๋ฉ๋ชจ, ์์ฐ์ ์ข๋ฅ(ํ๊ธ, ์นด๋ ๋ฑ), ๋ถ๋ฅ(์ผํ, ์๋น ๋ฑ), ๋ฉ๋ชจ๋ฅผ ๊ธฐ๋กํ  ์ ์์ต๋๋ค.
  - ์๋ชป๋ ๋ ์ง ํ์์ ์๋ ฅํ๊ฑฐ๋ ๋๋ฌด ํฐ ๊ธ์ก(16์๋ฆฌ ์ด์)์ ์๋ ฅํ๋ฉด ์๋ฌ๊ฐ ๋ฐ์ํฉ๋๋ค.
- ์ ์ ๋ ์์ ์ด ๊ธฐ๋กํ ๊ฐ๊ณ๋ถ ๋ฆฌ์คํธ๋ฅผ ์กฐํํ  ์ ์์ต๋๋ค.
  - ์ ์ ๋ ๋, ์, ์ผ์ ์ ํํด์ ๊ฐ๊ณ๋ถ ๋ฆฌ์คํธ๋ฅผ ์กฐํํ  ์ ์์ต๋๋ค.
  - ๋ง์ฝ ๋, ์, ์ผ ์ค ์๋ฌด๊ฒ๋ ์ ํํ์ง ์๋๋ค๋ฉด ํ์ฌ ๋ ์ง์ ๊ธฐ๋ก์ ์ถ๋ ฅํฉ๋๋ค.
  - ์ ์ ๊ฐ ์ ํํ ์ต์์ ๋ฐ๋ผ ํํฐ๋ง๋ ๊ฒฐ๊ณผ๊ฐ ์ถ๋ ฅ๋ฉ๋๋ค.
  - ํํฐ๋ง๋ ๊ฒฐ๊ณผ์ ํจ๊ป ์ ์ ๊ฐ ๊ธฐ๋กํ ์ด ๊ธ์ก์ด ์๊ธ๊ณผ ์ถ๊ธ ๊ธ์ก์ผ๋ก ๋๋์ด์ ธ ์ถ๋ ฅ๋ฉ๋๋ค.
- ์ ์ ๋ ์์ ์ด ๊ธฐ๋กํ ๋ฆฌ์คํธ ์ค ํ๋๋ฅผ ๊ณจ๋ผ ์์ธ ๊ธฐ๋ก์ ์กฐํํ  ์ ์์ต๋๋ค.
- ์ ์ ๋ ์์ ์ด ๊ธฐ๋กํ ๊ฐ๊ณ๋ถ์ ๋ด์ฉ์ ์๋ฐ์ดํธ ํ  ์ ์์ต๋๋ค.
- ์ ์ ๋ ์์ ์ด ๊ธฐ๋กํ ๊ฐ๊ณ๋ถ์ ๋ด์ฉ์ ์ญ์  ํ  ์ ์์ต๋๋ค. (soft delete๋ฅผ ์ฌ์ฉํ์ฌ ์ฌ์ฉ์๊ฐ ๋ณต์ ๊ฐ๋ฅํ๋๋ก ํ์์ต๋๋ค.)
  - ์ ์ ๊ฐ ๊ฐ๊ณ๋ถ๋ฅผ ์ญ์ ํ๋ฉด ํด๋น ๊ฐ๊ณ๋ถ์ is_deleted ํ๋๊ฐ True๋ก ๋ณํ๋ฉฐ ์ฌ์ฉ์๋ ํด๋น ๊ฐ๊ณ๋ถ๋ฅผ ์กฐํ, ๋ณ๊ฒฝํ  ์ ์๊ฒ ๋ฉ๋๋ค.
- ์ ์ ๋ ์์ ์ด ์ญ์ ํ ๊ฐ๊ณ๋ถ๋ฅผ ๋ค์ ๋ณต์ํ  ์ ์์ต๋๋ค.
  - ์ ์ ๊ฐ ๊ฐ๊ณ๋ถ๋ฅผ ๋ณต์ํ  ์ ํด๋น ๊ฐ๊ณ๋ถ์ is_deleted ํ๋๊ฐ False๋ก ๋ณํ๋ฉฐ ์ฌ์ฉ์๋ ๋ค์ ํด๋น ๊ฐ๊ณ๋ถ๋ฅผ ์กฐํ, ๋ณ๊ฒฝํ  ์ ์๊ฒ ๋ฉ๋๋ค.

## ๐ ์คํ ๋ฐฉ๋ฒ

1. ํฐ๋ฏธ๋์ ์ด์ฉํ์ฌ ์ํ๋ ํด๋์ ๋ค์ด๊ฐ์ ๋ฐ ๋ช๋ น์ด๋ฅผ ์๋ ฅํฉ๋๋ค.

```
git clone https://github.com/rimi0108/moneybook.git .
```

2. Docker ํ์ผ์ด ์๋ ์์น์์ ๋ฐ ๋ช๋ น์ด๋ฅผ ์๋ ฅํด Docker ํ๊ฒฝ์ ์คํํฉ๋๋ค.

```
docker-compose up --build
```

3. ์๋ฒ ์คํ์ ํ์ธํฉ๋๋ค.

```
django  | Starting development server at http://0.0.0.0:8000/
django  | Quit the server with CONTROL-C.
```

4. [Postman Docs](https://documenter.getpostman.com/view/16843855/UVCCeiac) ์ ์ ์ํ์ฌ์ 

<img width="266" alt="แแณแแณแแตแซแแฃแบ 2021-11-19 แแฉแแฎ 6 54 50" src="https://user-images.githubusercontent.com/73830753/142603983-19bd6606-5b51-4791-bf2a-213852157d39.png">

์ฐ์ธก ์๋จ์ `Run in Postman` ๋ฒํผ์ ๋๋ฅด๊ณ  ๋ก๊ทธ์ธ ํ ์ฌ์ฉํ  ์ํฌ์คํ์ด์ค๋ฅผ ๊ณ ๋ฆ๋๋ค.

<img width="269" alt="แแณแแณแแตแซแแฃแบ 2021-11-19 แแฉแแฎ 6 56 10" src="https://user-images.githubusercontent.com/73830753/142603629-0c9d5756-f7b0-4a11-a126-8fc55b6414ef.png">


<img width="265" alt="แแณแแณแแตแซแแฃแบ 2021-11-19 แแฉแแฎ 6 56 15" src="https://user-images.githubusercontent.com/73830753/142603640-f7e8d848-7d74-4e8c-8805-902cb97213cd.png">

ํฌ์คํธ๋งจ ํ๊ฒฝ์ No Environment์์ Local๋ก ๋ณ๊ฒฝํ๊ณ  ํต์ ์ ์์ํฉ๋๋ค.

โ mysql ํ๊ธ ์ธ์ฝ๋ฉ ์๋ฌ ์

<img width="617" alt="แแณแแณแแตแซแแฃแบ 2021-11-19 แแฉแแฎ 8 49 48" src="https://user-images.githubusercontent.com/73830753/142618734-5531a954-6500-45ff-9439-db8573ab522f.png">

```
apt-get update
```
```
apt-get install vim
```
```
vim /etc/mysql/my.cnf
```
์ ์ธ๊ฐ์ง ๋ช๋ น์ด๋ฅผ mysql ์ปจํ์ด๋์์ ์คํํฉ๋๋ค.
```
[client]
default-character-set=utf8

[mysql]
default-character-set=utf8

[mysqld]
collation-server = utf8_unicode_ci
init-connect='SET NAMES utf8'
character-set-server = utf8
```
my.cnf ํ์ผ์ ์ ์ฝ๋๋ฅผ ์ถ๊ฐํฉ๋๋ค.

<img width="694" alt="แแณแแณแแตแซแแฃแบ 2021-11-19 แแฉแแฎ 9 01 41" src="https://user-images.githubusercontent.com/73830753/142619710-250c4d21-987f-4021-af25-9d7ceee57409.png">

์ ์์ ์ผ๋ก ํ๊ธ์ด ๋จ๋ ๊ฒ์ ํ์ธํ์ค ์ ์์ต๋๋ค.

### unit test ์คํ๋ฒ

1. Docker `django` ์ปจํ์ด๋์ ์ ์ํ์ฌ `manage.py`ํ์ผ์ด ์๋ ์์น์์ ๋ฐ ๋ช๋ น์ด๋ฅผ ์๋ ฅํฉ๋๋ค.

```
python manage.py test
```

2. test ๊ฒฐ๊ณผ๋ฅผ ํ์ธํฉ๋๋ค.

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..............
----------------------------------------------------------------------
Ran 14 tests in 2.404s

OK
Destroying test database for alias 'default'...
```

์ ํ๋ฉด์ test ์ฑ๊ณต ์ ๋์ค๋ ํ๋ฉด์๋๋ค.

โ `Got an error creating the test database: (1044, "Access denied for user 'django'@'%' to database 'test_django'")`

์ ์๋ฌ ๋ฐ์ ์ mysql root์ ์ ์ํ์ฌ

```
mysql> GRANT ALL PRIVILEGES ON test_django.* TO 'django'@'%';
```
```
mysql> FLUSH PRIVILEGES;
```
์ ๋ช๋ น์ด๋ฅผ ์๋ ฅํด์ฃผ์ธ์.

## ๐ Postman Docs

https://documenter.getpostman.com/view/16843855/UVCCeiac
