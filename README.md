# DJANGO BASIC
목차
1. [프로젝트 환경](#1-프로젝트-환경)
2. [프로젝트 생성하기](#2-프로젝트-생성하기)
3. [프로젝트 구성하기](#3-프로젝트-구성하기)
4. [코드작성하기](#4-코드-작성하기)
5. [서버 실행하기](#5-서버-실행하기)


## 1. 프로젝트 환경
1. 운영체제 : windows
2. IDE : Visual Studio Code
3. 언어 : python
4. Shell(Command) : Git bash  

**설치가 안되어있는 부분이 있다면 설치하고 진행해주세요. python을 웹사이트에서 설치 시 path추가에 체크하고 설치하셔야합니다!!**

- [목차로 돌아가기](#django-basic)

## 2. 프로젝트 생성하기

**_Git bash command_**
- Git bash가 설치되어 있다면 바탕화면이나 폴더안에서 우클릭 시 git bash here라고 나올거에요.
    이거 클릭하면 해당 경로에서 git bash 실행가능
1. **_mkdir (폴더이름)_** >> 프로젝트를 관리할 폴더 생성(windows에서 우클릭으로 폴더생성해도 됩니다.)
2. **_cd (경로입력)_** >> 폴더 안에 들어감
3. **_python -m venv (가상환경이름)_** >> 가상환경 생성
4. **_source (가상환경이름)/scripts/activate_** >> 가상환경 실행
5. **_pip install django_**   
**_pip install djangorestframework_** >> 기본적인 라이브러리 설치
6. **_mkdir (프로젝트이름)_** >> 프로젝트 폴더를 생성
7. **_cd (프로젝트 폴더)_** >> 프로젝트 폴더로 이동
7. **_django-admin startproject config ._**>> 프로젝트 생성  

이렇게 하면
<pre>
1.	폴더

  A.	프로젝트 폴더
  
        i. config
        
  B.	가상환경 폴더
</pre>
위와 같이 구성될 겁니다. 그리고 VScode로는 A를 여시면 됩니다.    
VScode에서 선택된 인터프리터가 가상환경의 python이 맞는지 확인!! 오른쪽 아래에 파란 상태창에서 확인가능

- [목차로 돌아가기](#django-basic)

## 3. 프로젝트 구성하기

1. VScode에서 프로젝트 폴더를 엽니다.
2. ctrl + shift + ` 로 터미널을 열고 Git bash를 선택합니다.
3. **_cd .._** >> venv는 상위폴더에 있기 때문에 상위폴더로 이동
4. **_source (가상환경이름)/scripts/activate_** >> 가상환경 실행
가상환경이 켜져있다면 Git bash 커맨드라인에 (가상환경이름) 이런식으로 뜰겁니다.
5. **_cd (프로젝트폴더)_** >> 다시 프로젝트 폴더로 이동해줍니다.

1. **_python manage.py startapp (테이블이름)_** >> 본인의 취향에 맞게 app을 하나씩 만듬   
	여기서 app은 DB의 테이블과 api, url 등을 관리하기 위한 친구라고 생각하세요
2. config/settings.py 의 installed_apps에 app을 추가해줘해요 그리구 설치한 라이브러리들 역시 여기에 명시해줘야합니다.

<pre>
- config/settings.py >> Django 기본 설정 파일   

- config/urls.py >> 요청 경로 설정 파일   

- (app)/urls.py >> 해당 경로와 api function 연결 파일

- (app)/views.py >> api 작성 파일

- (app)/models.py >> table 작성 파일
</pre>

여기서 원하는 기능을 작성 후 각각 파일을 저장한 뒤

1. **_python manage.py makemigrations_** >> migration 생성
2. **_python manage.py migrate_** >> 적용   

참고 **_python manage.py showmigrations_** >> 미리보기

- [목차로 돌아가기](#django-basic)

## 4. 코드 작성하기

### config

#### settings.py
1. django를 제외한 pip install 한 라이브러리들은 installed_apps에 추가해줘야합니다.
2. 생성한 app 역시 installed_apps에 추가해줘야합니다.
3. DB설정이나 IP접속허용 등 다양한 설정이 가능합니다.

```
#예시코드
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #djangorestframework
    'rest_framework',
    
    ## MY APPS
    '추가한app이름',
]
```

#### urls.py
- 호출 경로를 지정해줍니다. 여기서는 각 app의 url만 연결해주면됩니다.

```
#예시코드
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('요청경로/', include('app이름.urls')),
]
```

### app

#### models.py
- db table을 만드는 공간입니다.

#### views.py
- api를 작성하는 공간입니다.

```
#예시코드
from django.shortcuts import render
from django.http import response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def 예시_view(request):
    if request.method == 'GET':
        data = {
            "author" : "sangkyu",
            "content" : "he is studying django"
        }
        return response.JsonResponse(data)
    
```

#### urls.py
- api와 경로를 연결해줄 파일입니다.
- 처음엔 파일을 생성하고 작성합니다.

```
#예시코드
from django.urls import path
from . import views

urlpatterns = [
    path('요청경로이름', views.views에서_만든_api함수),
]

```

- [목차로 돌아가기](#django-basic)

## 5. 서버 실행하기

1. *python manage.py runserver*
2. api호출은 웹페이지에서 코드작성한 경로로 들어가면 기본적인 GET요청을 확인할 수 있습니다.
3. Postman등 http통신(CRUD)를 해볼 수 있는 소프트웨어도 있습니다. 나중에 다룰거에요

- [목차로 돌아가기](#django-basic)
<hr/>

### MEMO
git pull하실 때 *pip install corsheaders* 하고 실행하셔야 할거에요. 프론트랑 연결 시 필요해서 설치해둔 라이브러리에요!   

- [목차로 돌아가기](#django-basic)
