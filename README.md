# 💰 고객 가계부 작성 및 관리 기능 구현

❗ `SECRET_KEY`, token 발급을 위한 `ALGORITHM`, `DATABASES`는 보안을 위해 별도의 파일 `my_settings.py`에 보관했습니다.

## 💡 ERD

<img width="801" alt="스크린샷 2021-11-18 오후 6 11 49" src="https://user-images.githubusercontent.com/73830753/142385765-3852e733-d441-45ed-9563-89e4a745e655.png">

## 🛠 사용 기술 및 툴

> - Back-End : <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.1-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/MySQL 5.7 -4479A1?style=for-the-badge&logo=MySQL&logoColor=white"/>
> - Deploy : <img src="https://img.shields.io/badge/AWS_EC2-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC : <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

## 👩‍💻 구현 기능

### users

- 유저는 이메일과 비밀번호 입력을 통해 회원가입을 할 수 있습니다.
- 유저의 비밀번호를 db에 암호화하여 안전하게 저장하기 위해 `bcrypt`를 사용했습니다.
- 유저가 로그인 시 token이 발급됩니다.
  - token 발급은 `jwt`를 사용하여 발급하였습니다.
  - token은 로그아웃을 위해 발급시 db에 저장됩니다.
- 유저 로그아웃 시 db에서 토큰을 삭제합니다.
  - 서비스 이용시 삭제된 토큰인지 아닌지 판단한 후 삭제된 토큰일 시 유저는 서비스를 이용할 수 없습니다.
  - 재로그인 시 다시 db에 토큰이 저장되므로 유저는 정상적으로 서비스를 이용할 수 있습니다.
  - 🤔 [jwt 로그아웃에 대해 고민하며 쓴 글](https://rimi0108.github.io/django/jwt-logout/)

### moneybooks

- 유저는 로그인 시 가계부 서비스를 이용할 수 있습니다.
  - 로그인 하지 않을 시 에러가 발생합니다.
- 유저는 가계부에 사용한 금액, 돈의 입금/출금 여부, 메모, 자산의 종류(현금, 카드 등), 분류(쇼핑, 식비 등), 메모를 기록할 수 있습니다.
  - 잘못된 날짜 형식을 입력하거나 너무 큰 금액(16자리 이상)을 입력하면 에러가 발생합니다.
- 유저는 자신이 기록한 가계부 리스트를 조회할 수 있습니다.
  - 유저는 년, 월, 일을 선택해서 가계부 리스트를 조회할 수 있습니다.
  - 만약 년, 월, 일 중 아무것도 선택하지 않는다면 현재 날짜의 기록을 출력합니다.
  - 유저가 선택한 옵션에 따라 필터링된 결과가 출력됩니다.
  - 필터링된 결과와 함께 유저가 기록한 총 금액이 입금과 출금 금액으로 나누어져 출력됩니다.
- 유저는 자신이 기록한 리스트 중 하나를 골라 상세 기록을 조회할 수 있습니다.
- 유저는 자신이 기록한 가계부의 내용을 업데이트 할 수 있습니다.
- 유저는 자신이 기록한 가계부의 내용을 삭제 할 수 있습니다. (soft delete를 사용하여 사용자가 복원 가능하도록 하였습니다.)
  - 유저가 가계부를 삭제하면 해당 가계부의 is_deleted 필드가 True로 변하며 사용자는 해당 가계부를 조회, 변경할 수 없게 됩니다.
- 유저는 자신이 삭제한 가계부를 다시 복원할 수 있습니다.
  - 유저가 가계부를 복원할 시 해당 가계부의 is_deleted 필드가 False로 변하며 사용자는 다시 해당 가계부를 조회, 변경할 수 있게 됩니다.

## 👀 설치 및 실행 방법

1. 터미널을 이용하여 원하는 폴더에 들어가서 밑 명령어를 입력합니다.

```
git clone https://github.com/rimi0108/moneybook.git .
```

2. Docker 파일이 있는 위치에서 밑 명령어를 입력해 Docker 환경을 실행합니다.

```
docker-compose up
```

3. 서버 실행을 확인합니다.

```
django  | Starting development server at http://0.0.0.0:8000/
django  | Quit the server with CONTROL-C.
```

### unit test 실행법

1. Docker `django` 컨테이너에 접속하여 `manage.py`파일이 있는 위치에서 밑 명령어를 입력합니다.

```
python manage.py test
```

2. test 결과를 확인합니다.

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..............
----------------------------------------------------------------------
Ran 14 tests in 2.404s

OK
Destroying test database for alias 'default'...
```

위 화면은 test 성공 시 나오는 화면입니다.

## Postman Docs

https://documenter.getpostman.com/view/16843855/UVCCeiac
