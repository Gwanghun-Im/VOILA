# <img src="./VOILA.png" width="65px">VOILA

```sh
VOILA는 영화 커뮤니티 사이트 입니다.


```

<strong><span style="color:#705DA8">VOILA<span/>는 영화 커뮤니키 사이트 입니다.<strong/>

![image-20210527224101212](README.assets/image-20210527224101212.png)

## ✔GUIDE



### :package: ​시작하기

>  시작하기에 앞서 아래의 명령어를 실행합니다.

### Backend

```bash
$ cd server
$ python -m venv venv
$ source venv/Scripts/activate
$ python install -r requirements.txt
$ python manage.py loaddata genre.json
$ python manage.py runserver
```

### Frontend

```bash
$ cd client/client
$ npm install
$ npm run serve
```

### :pencil: SIGNUP

> 회원가입을 합니다.

![image-20210527211353906](README.assets/image-20210527211353906.png)

### :pencil2: LOGIN

> 로그인을 합니다.

![image-20210527211250969](README.assets/image-20210527211250969.png)

### :house: HOME

> `search` 검색창에 영화를 검색합니다.

> 검색창 아래의 메시지는 "프로필","추천","초성게임"이 랜덤으로 출력됩니다.
>
> - "영화제목" 을 검색하면 검색한 영화가 화면에 표시됩니다.
> - "프로필" 을 검색하면 프로필 페이지로 이동합니다.
> - "초성게임"을 검색하면 초성게임 페이지로 이동합니다.
> - "추천"을 검색하면 인기기반 추천영화가 표시됩니다.

![image-20210527211136723](README.assets/image-20210527211136723.png)

#### 1. 영화제목 검색

> 영화제목 결과가 있는경우

![image-20210527211914916](README.assets/image-20210527211914916.png)

> 영화제목 결과가 없는경우

![image-20210527212007080](README.assets/image-20210527212007080.png)

#### 2. 추천 검색

![image-20210527211832145](README.assets/image-20210527211832145.png)

###  :mag:DETAIL

> 영화 카드를 누르면 영화에대한 디테일 정보가 표시됩니다.

> 제목, 개봉년도, 장르, 평점, 줄거리가 표시되며, 평점은 :star:로 표시됩니다.
>
> `Like this`버튼을 눌러 이 영화에 좋아요를 누를 수 있습니다.

![image-20210527213333944](README.assets/image-20210527213333944.png)

### :newspaper:REVIEW

> DETAIL 에서 `리뷰보기`를 누르면 리뷰작성 양식과 함께 작성된 리뷰가 나옵니다. 

> - 작성된 리뷰에는 이 리뷰를 좋아한 사람의 수, 리뷰제목, 작성자, 리뷰작성자의 평점 정보가 함께 표시됩니다.

![image-20210527214718573](README.assets/image-20210527214718573.png)

### 💬 REVIEW&COMMENT

>  REVIEW페이지 에서 게시글을 작성하거나, 리뷰를 클릭하면 작성된 리뷰가 나옵니다.

> 영화제목, 리뷰제목, 내용, 별점, 작성자, 작성시간이 표시됩니다.
>
> :heart:를 누르면 리뷰에 좋아요를 할 수 있습니다. ,
>
> 댓글을 달 수 있습니다.

![image-20210527215433570](README.assets/image-20210527215433570.png)

### :blue_book: PROFILE

> 프로필에선 영화클라우드와 작성한 리뷰가 표시 됩니다.



####  :cloud:영화클라우드

> 영화클라우드는 자신이 좋아요표시를 누른 영화목록의 OVERVIEW를 모아 많이 등장한 단어를 화면에 표시해 줍니다.

![image-20210527215527215](README.assets/image-20210527215527215.png)

### :kr:초성게임

> HOME의 검색창에 초성게임을 입력하면 이동할 수 있습니다.

#### 메인페이지

> 초성게임의 메인페이지 입니다,

> `start`버튼을 눌러 게임을 시작할 수 있습니다.
>
> `TOP 10`을 눌러 순위를 확인할 수 있습니다.

#### 게임시작

> 게임을 시작하면 나오는 화면입니다.

> 게임스코어, 초성, 남은시간, 줄거리 가 표시됩니다.
>
> 정답을 입력할 수 있는 박스가 주어지고  버튼을 눌러 제출할 수 있습니다.
>
> 빨간색 버튼을 누르면 문제를 패스할 수 있습니다.

![image-20210527220338313](README.assets/image-20210527220338313.png)

#### PASS

> 문제를 패스합니다.

> 패스를하면 정답이 출력됩니다.
>
> 모든 패스기회를 소진하면 스코어가 감점되면서 패스를 할 수 있습니다.

![image-20210527220623167](README.assets/image-20210527220623167.png)

#### 게임종료

> 게임이 종료되면 알림이 뜹니다. 

> TOP 10테이블에 유저의 순위와, 이메일주소, 스코어가 표시됩니다.
>
> 본인이 한 경우 파란색 글씨로 표시됩니다.

![image-20210527221600677](README.assets/image-20210527221600677.png)

![image-20210527221620066](README.assets/image-20210527221620066.png)

### :date: ERD

![image-20210527223142795](README.assets/image-20210527223142795.png)

# DEVELOPER

SHIM CHANIN

IM GWANGHUN

<center>🙏Merci Beaucoup🙏