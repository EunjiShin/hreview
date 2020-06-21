# HREVIEW
> 2020년 1학기 나스리디노프 아지즈 교수님 오픈소스 웹 소프트웨어 과목 term project <br>
! 이 프로젝트는 django와 Python 등 개발환경이 갖춰져있다는 전제 하에 사용할 수 있습니다. !

<hr>
# 0. 실행
## + hreview
## | \ + hreview
## |   | \ + forms.py
## |   |   + settings.py
## |   |   + urls.py
## |   |   + wsgi.py
## |   |   + asgi.py
## | \ + hyuzi
## |   | \ + static
## |   | \ + templates
## |   | + admin.py
## |   | + context_processors.py
## |   | + models.py
## |   | + urls.py
## |   | + views.py
## | \ + media
## | \ + static
## | \ + templates
## | + manage.py
## + README.md


# 1. 프로젝트 계층
## 1-1. 프로젝트 폴더
### 장고 프로젝트는 크게 프로젝트-앱으로 구성됩니다. 
<img width="171" alt="hyuzi" src="https://user-images.githubusercontent.com/38103085/81608709-a6ae0a00-9411-11ea-971d-18747c4069f8.png">

현재 프로젝트 폴더 hreview 안에 임의로 만든 앱 hyuzi가 들어있습니다.
<br> CBV 방식으로 로그인과 회원가입을 구현한 상태로, 앱 hyuzi에서 메인, 상품, 장바구니 등 실질적인 페이지들을 구현하게 될 겁니다. <br> 또는 새로운 앱을 추가하게 될 수도 있어요. <br>
hreview 안에 있는 파일들에 대해선 아래에서 설명하겠습니다. <br>
<hr> <br>

# 2. 장고 동작
## 2-1. 장고란?
### Django는 python으로 작성된 오픈소스 웹 프레임워크입니다. 
<br>
공식문서에서 대부분의 튜토리얼과 사용법을 설명해주므로, 혹시 찾아볼 것이 있다면 아래 링크를 참고하세요.<br>
https://docs.djangoproject.com/ko/3.0/

## 2-2. MTV 패턴
웹을 개발할 때 효율적이고 안전한 개발을 위해 데이터 / 사용자 / 데이터 처리하는 로직을 구분하여 한 요소가 다른 요소에 영향을 주지 않도록 설계 방식을 정해두곤 합니다. <br> 
일반적으로 MVC 패턴이라고 일컫는 방식이지만, 장고에선 똑같은 방식을 이름만 바꾸어 MTV 패턴이라고 부릅니다. <br><br>
<img width="609" alt="mtv" src="https://user-images.githubusercontent.com/38103085/81602304-4ade8380-9407-11ea-9665-5734c2e347e3.png"><br>
* M : Model - DB에 저장되는 데이터
* T : Template - 사용자에게 보여지는 영역들
* V : View - 로직이 수행한 결과를 Template로 전달(CBV는 class 기반 뷰, FBV는 function 기반 뷰)

쉽게 말하자면 필요한 데이터를 모델로 정리하고, 뷰로 이러쿵저러쿵 하여 템플릿을 통해 보여주는 방식입니다. 
<br><br>

## 2-3. Template
위에서 설명한 것과 같이, MTV패턴에 맞추어 작업을 해야합니다. <br>
프로젝트를 클론해서 받으면 templates 라는 폴더가 몇 개 보일겁니다. <br> 
django 가이드라인에 따르면 각각의 app 폴더들은 개별적인 templates 서브폴더를 가져야합니다.<br> 
결과적으로 **app/templates/app/html파일들** 의 구조가 되어야합니다. 
<br> templates 폴더 안에 app 이름의 폴더를 하나 더 만드는 이유는 폴더 구조가 복잡해질 때 더 쉽게 찾기위한 관습적인 방법입니다. <br><br>
<img width="170" alt="hyuzi" src="https://user-images.githubusercontent.com/38103085/81603792-e113a900-9409-11ea-9d62-8ae3592753b8.png"><br><br>
지금 올린 프로젝트로 예를 들면, hyuzi 앱에 templates/hyuzi/main.html파일이 있는 걸 확인할 수 있습니다. <br>
hyuzi 앱의 view에서 main.html으로 가라고 하면, hyuzi 앱 안에는 templates/hyuzi/main.html이 있어야한다는 뜻이에요. <br>
만약 개발 중 서버를 돌렸는데 노란 화면이 나오면서 TemplateDoesNotExist 에러가 떳다면,
경로에 해당 템플릿이 없다는 에러이므로, 내가 파일 이름에 오타를 치진 않았는지, template 경로가 올바른지 확인해보도록 합시다. 
<br> 더 자세한 설명은 아래 링크를 참고하세요! <br> 
Link : [Template](http://pythonstudy.xyz/python/article/307-Django-%ED%85%9C%ED%94%8C%EB%A6%BF-Template)

<br><br>

## 2-4. base.html

<img width="169" alt="base" src="https://user-images.githubusercontent.com/38103085/81604361-bc6c0100-940a-11ea-9cc3-426c25d71751.png">
<br> 이 base.html은 뭔가요?
=> 템플릿마다 공통적으로 반복되는 부분을 묶어둔 파일입니다. <br>
예를 들어, nav바나 footer같이 모든 페이지에 공통적으로 들어갈 요소를 html 파일마다 적는 건 불필요한 작업이고, 코드도 길어지게 됩니다.
그래서 이런 반복되는 것들을 묶어 base.html이라는 파일에 넣고, 이후 다른 template들엔 이 base.html을 로드하는 형식으로 작업하여 작업 능률을 높일 수 있습니다. <br>
물론 base가 아니라 다른 이름으로 해도 됩니다! 만든 후, 템플릿 제일 상단에 {% extends "base.html" %} 처럼 추가하는 형식을 기억해주세요.<br>
현재 navbar만 추가된 상태로, 이후 점점 추가하면 됩니다. bootstrap을 쓰기위한 링크들도 전부 여기 있습니다.

<hr>

# 3. 웹 서버
## 3-1. manage.py

manage.py는 사이트 관리를 도와주는 역할을 하는 스크립트입니다. 이 스크립트로 별다른 설치 없이 컴퓨터에서 바로 웹서버를 시작할 수 있어요. <br>
프로젝트 폴더 안에, 그러니까 app 폴더와 동일한 경로에 있습니다. 현재 hreview 안에, 앱 hyuzi와 동일 경로에 있습니다. <br>
app을 새로 생성하거나 model에 변경사항이 생겨 migrate를 해줘야할 때, run server을 할 때 모두 이 manage.py 파일을 사용합니다. <br>

## 3-2. runserver

우리가 작업한 것들이 제대로 적용되었는지 확인하기 위해서 직접 웹 서버를 돌려볼 수 있습니다. <br>
콘솔창에서 manage.py와 동일한 경로로 이동해, **python manage.py runserver** 명령을 입력해주세요. <br>
꼭 manage.py와 같은 위치여야 작동합니다. 제대로 실행됬다면, <br>
<img width="408" alt="runserver" src="https://user-images.githubusercontent.com/38103085/81605995-487f2800-940d-11ea-925f-4a58afc80aaa.png"> <br>
콘솔에 이런 화면이 뜰 거에요. 만약 에러가 뜨면 해당 에러를 참고하여 오류를 고쳐주세요. <br> 
정상적으로 작동되었다면, 쓰여진 그대로 http://127.0.0.1:8000으로 가서 확인하면 되고, 만약 서버를 종료하고 싶다면 Ctrl + C를 누르면 됩니다. <br>
http://127.0.0.1:8000 는 요건 project의 settings.py에서 ALLOWED_HOSTS를 따로 설정해주지 않아서 자동으로 유효한 호스트로 설정된 것 입니다. <br>
이제 프로젝트와 앱들의 urls.py에 우리가 설정해둔 url들을 참고하여 웹 서비스를 이용할 수 있습니다. <br>
현재 메인 페이지는 ** http://127.0.0.1:8000/hyuzi/ ** 입니다.<br>

## 3-3. 배포

그렇다면 이 프로젝트를 굳이 클론받거나 개발환경을 갖추지않아도 url만 입력하면 우리 웹사이트에 접속할 수 있나요?
<br> 아니요! 그러려면 배포 과정을 거쳐야합니다. <br>
하지만 이번 프로젝트 요구사항에 배포 과정이 생략되었으므로, 저희는 제외하도록 하겠습니다. <br>
만약 관심이 있다면 aws나 Heroku 등을 이용할 수 있으니 참고해주세요. <br>

<hr>

# 4. 관리자 페이지
## 4-1. django admin

urls.py를 보면 **path('admin/', admin.site.urls)** 라는 admin 경로가 있습니다. <br>
제가 만든게 아니라 프로젝트 urls.py에 처음부터 있던 경로로, 장고가 지원하는 관리자 페이지를 나타냅니다.<br>
이 관리자 페이지에서 모델에 데이터를 추가하거나 삭제, 수정하는 등의 작업을 할 수 있습니다.<br>
해당 페이지가 한글로 보이도록 설정해 둔 상태이니 필요할 경우 url대로 http://127.0.0.1:8000/admin을 입력해서 접속해주세요.<br>
단 해당 관리자 페이지를 사용하기 위해선 관리자 권한이 필요합니다.<br>

<img width="321" alt="super" src="https://user-images.githubusercontent.com/38103085/81607209-48802780-940f-11ea-8fab-eb238556923b.png"><br>

runserver 했던 것 처럼, manage.py 경로로 이동해서 **python manage.py createsuperuser** 명령어를 입력해서 관리자 계정을 만들 수 있습니다.<br>
사진처럼 새로운 관리자 계정을 생성한 후 admin 페이지에 접속하면 관리자 페이지를 사용할 수 있습니다.
