# 과제에 치이는 당신들을 위한 짧은 매뉴얼
> 'beautiful하고 perfect한 웹 사이트를 만들어보세요' - 교수님 <br>
! 이 프로젝트는 django와 Python 등 개발환경이 갖춰져있다는 전제 하에 사용할 수 있습니다. !

<hr>

# 1. 프로젝트 계층
## 1-1. 프로젝트 폴더
### 장고 프로젝트는 크게 프로젝트-앱으로 구성됩니다. 
<img width="175" alt="project" src="https://user-images.githubusercontent.com/38103085/81601679-3ea5f680-9406-11ea-9156-ec1a0eeec50c.png">

현재 hyuzi라는 제일 상위폴더 안에 프로젝트 폴더 hreview가 들어있으며, hreview 안에 임의로 만든 앱 hyuzi가 들어있습니다.
<br> CBV 방식으로 로그인과 회원가입을 구현한 상태로, 앱 hyuzi에서 메인, 상품, 장바구니 등 실질적인 페이지들을 구현하게 될 겁니다. <br> 또는 새로운 앱을 추가하게 될 수도 있어요. <br>
hreview 안에 있는 다른 친구들에 대해선 아래에서 설명하겠습니다. <br>
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
근데 언니 이걸 왜 설명해줘요?? 
=> html 파일들의 위치가 중요하기때문입니당! 
프로젝트를 클론해서 받으면 templates 라는 폴더가 여러개 있는게 보일거에요. <br> 
django 가이드라인에 따르면 각각의 app 폴더들은 개별적인 templates 서브폴더를 가져야합니다.<br> 
결과적으로 **app/templates/app/html파일들** 의 구조가 되어야해요. 
<br> templates 폴더 안에 app 이름의 폴더를 하나 더 만드는 이유는 폴더 구조가 복잡해질 때 더 쉽게 찾기위한 관습적인 방법입니다. <br><br>
<img width="170" alt="hyuzi" src="https://user-images.githubusercontent.com/38103085/81603792-e113a900-9409-11ea-9d62-8ae3592753b8.png"><br><br>
지금 올린 프로젝트로 예를 들면, hyuzi 앱에 templates/hyuzi/main.html파일이 있는 걸 확인할 수 있습니다. <br>
hyuzi 앱의 view에서 main.html으로 가라고 하면, hyuzi 앱 안에는 templates/hyuzi/main.html이 있어야한다는 뜻이에요. <br>
만약 쟉이들이 서버를 돌렸는데 노란 화면이 나오면서 TemplateDoesNotExist 에러가 떳다? <br>
경로에 해당 템플릿이 없다는 에러이므로, 내가 파일 이름에 오타를 치진 않았는지, template 경로가 올바른지 확인해보도록 합시다. 
<br> 더 자세한 설명은 아래 링크를 참고하세요! <br> 
Link : [Template](http://pythonstudy.xyz/python/article/307-Django-%ED%85%9C%ED%94%8C%EB%A6%BF-Template)

<br><br>

## 2-4. base.html

<img width="169" alt="base" src="https://user-images.githubusercontent.com/38103085/81604361-bc6c0100-940a-11ea-9cc3-426c25d71751.png">
<br> 언니 근데 이 base.html은 뭐에요??
=> 템플릿마다 공통적으로 반복되는 부분을 묶어둔 파일입니당! <br>
예를 들어, nav바나 footer같이 모든 페이지에 공통적으로 들어갈 요소를 html 파일마다 적는건 귀찮고 코드도 길어지게 됩니다.
그래서 이런 반복되는 것들을 묶어 base.html이라는 파일에 넣고, 이후 다른 template들엔 이 base.html을 로드하는 형식으로 작업하면 깔끔해집니다. <br>
물론 base가 아니라 다른 이름으로 해도 됩니다! 만든 후, 템플릿 제일 상단에 {% extends "base.html" %} 처럼 추가만 해주면 돼요.<br>
현재 navbar만 추가된 상태로, 이후 점점 추가하면 됩니다. bootstrap을 쓰기위한 링크들도 전부 여기에 넣어뒀어요.

<hr>

# 3. 웹 서버
## 3-1. manage.py

manage.py는 사이트 관리를 도와주는 역할을 하는 스크립트입니다. 이 스크립트로 별다른 설치 없이 컴퓨터에서 바로 웹서버를 시작할 수 있어요. <br>
프로젝트 폴더 안에, 그러니까 app 폴더와 동일한 경로에 있습니다. hreview 안에, hyuzi와 동일 경로에 있는 게 보일거에요. <br>
app을 새로 생성하거나 model에 변경사항이 생겨 migrate를 해줘야할 때, run server을 할 때 모두 이 manage.py 파일을 사용합니다. <br>

## 3-2. runserver

우리가 작업한 것들이 제대로 적용되었는지 확인하기 위해서 직접 웹 서버를 돌려봐야겠죠? <br>
콘솔창에서 manage.py와 동일한 경로로 이동해, **python manage.py runserver** 명령을 입력해주세요. <br>
꼭 manage.py와 같은 위치여야 작동합니다! 제대로 실행됬다면, <br>
<img width="408" alt="runserver" src="https://user-images.githubusercontent.com/38103085/81605995-487f2800-940d-11ea-925f-4a58afc80aaa.png"> <br>
콘솔에 이런 화면이 뜰 거에요. 에러가 뜨면 고쳐야하구...^,^ 쓰여진 그대로 http://127.0.0.1:8000으로 가서 확인하면 되고, 만약 서버를 종료하고 싶다면 Ctrl + C를 누르면 됩니다. <br>
http://127.0.0.1:8000 <- 요건 project의 settings.py에서 ALLOWED_HOSTS를 따로 설정해주지 않아서 자동으로 유효한 호스트로 설정된거에요. <br>
이제 프로젝트와 앱들의 urls.py에 우리가 설정해둔 대로 url을 조정해주면 됩니다~~~ 짱쉽죠? <br>
지금은 ** http://127.0.0.1:8000/hyuzi/ ** 가 메인 페이지로, 여기로 가서 상단 nav바의 로그인 회원가입 로그아웃 기능을 시험해볼 수 있는 상태입니다.<br>

## 3-3. 배포

앗 구럼 이 프로젝트를 굳이 클론받거나 개발환경을 갖추지않아도 url만 입력하면 우리 웹사이트에 접속할 수 있나요?! 
<br> 아니요! 그러려면 배포 과정을 거쳐야합니다. <br>
근데 센빠이들이 동영상 촬영으로 실행화면을 제출했다하셔서 배포를 할 진..모르겟슈.... 필요하면 합시당 <br>

<hr>

# 4. 관리자 페이지
## 4-1. django admin

그런데 urls.py를 보면 **path('admin/', admin.site.urls)** 라는 admin 경로가 하나 있을거에요. <br>
요건 제가 만든게 아니라 프로젝트 urls.py에 처음부터 있던 친구입니당. 장고는 관리자 페이지를 통해서 모델을 보고 업데이트하고 삭제할 수 있게 해줘요. <br>
settings.py에서 한글로 보이도록 수정해두었습니당. 프론트만 만질거면 쓸 일이 없긴 할건데 혹시 궁금할까바 적어둡니다~ <br>
url대로 http://127.0.0.1:8000/admin을 입력하면 들어갈 수 있는데, 아마 관리자 권한이 필요할거에요. <br>

<img width="321" alt="super" src="https://user-images.githubusercontent.com/38103085/81607209-48802780-940f-11ea-8fab-eb238556923b.png"><br>

runserver 했던 것 처럼, manage.py 경로로 이동해서 **python manage.py createsuperuser** 명령어를 입력해서 관리자 계정을 만들 수 있어요.<br>
보이는 것처럼 성공적으로 생성된 후 admin 페이지에 접속하면 들어갈 수 있을겁니당. 


<hr>
대충 프로젝트 실행할 때 필요할 것 같은 것들을 적어뒀는데, 혹시 궁금한게 있으면 카톡하면 댑니당~~ <br>
근데 새벽에 뇌빼고 적고있어서ㅋㅋㅋㅋ 오타잇음 미안..... 잘 안돼면 언제든 무러바..... <br>
구럼 우리 모두 화이팅합시다~~ 안뇽안뇽!
