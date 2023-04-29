# DJANGO BASIC

## 프로젝트 생성



*Git bash command*

1. 프로젝트를 관리할 폴더 생성
2. 폴더 안에 들어감 : *cd (경로입력)*
3. 가상환경 생성 : *python -m venv (가상환경이름)*
4. *source (가상환경이름)/scripts/activate* >> 가상환경 실행
5. *pip install django*   
*pip install djangorestframework* 등 기본적인 라이브러리 설치
6. 프로젝트 폴더 생성하고 그 안으로 이동
7. *django-admin startproject config .*>> 프로젝트 생성
이렇게 하면
<pre>
1.	폴더

  A.	프로젝트 폴더
  
        i. config
        
  B.	가상환경 폴더
</pre>
이렇게 구성될 겁니다. 그리고 Vscode로는 A를 여는거죠.


## 프로젝트 구성하기(source (가상환경이름)/scripts/activate 선행)
가상환경이 켜져있다면 Git bash 커맨드라인에 (가상환경이름) 이런식으로 뜰겁니다.
1. 본인의 취향에 맞게 app을 하나씩 만듬 : *python manage.py startapp (테이블이름)*    
	여기서 app은 DB의 테이블과 api, url 등을 관리하기 위한 친구라고 생각하세요
2. config/settings.py 의 installed_apps에 app을 추가해줘해요 그리구 설치한 라이브러리들 역시 여기에 명시해줘야합니다.

config/settings.py >> Django 기본 설정 파일
config/urls.py >> 요청 경로 설정 파일
(app)/urls.py >> 해당 경로와 api function 연결 파일
(app)/views.py >> api 작성 파일
(app)/models.py >> table 작성 파일

여기서 원하는 기능을 작성 후 각각 파일을 저장한 뒤

1. *python manage.py makemigrations* >> migration 생성
2. *python manage.py migrate* >> 적용   

참고 *python manage.py showmigrations* >> 미리보기

## 서버 켜는 법
1. *python manage.py runserver*
   

<hr/>

### 2023-04-26 진행 상황
config/settings.py   
config/urls.py   
apis/urls.py   
apis/views.py   
참고하시면 될거같습니다.   
만약 git pull해보실 거면 *pip install corsheaders* 하고 실행하셔야 될거에요 프론트랑 연결 시 필요해서 설치해둔 라이브러리에요!   
test.html도 신경안쓰셔도 됩니다. 다음주에 할 내용이에용

