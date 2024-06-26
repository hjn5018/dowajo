# 내일배움캠프 1주차 미니프로젝트

### 와이어 프레임

웹페이지 제작에 앞서 와이어 프레임을 만들어 보고 전체적인 컨셉을 정한다.

팀이름이 "도와조"인 만큼 컨셉에 맞춰 팀원들 간 도움을 주고받을 수 있는 웹 페이지를 기획했다

![main](https://github.com/kngslbm/study/assets/148850117/95f5aa2a-3c15-428a-b505-5b4fa7bf7d7c)

상단 nav 바에는 각 팀원의 이름이 있고 클릭 시 팀원 개별 페이지로 이동한다.

![crew](https://github.com/kngslbm/study/assets/148850117/1fc8b975-d60f-4301-9ab6-46790edb5747)
각 팀원의 페이지에는 프로필과 “도와조 리스트”가 있다.

“도와조” 버튼으로 리스트를 생성할 수 있으며 리스트는 프로필 당사자만 생성할 수 있어야 한다.

각 “도와조 리스트”에는 도움주기 버튼이 있고 이를 통해 답글을 달 수 있다. 해당 기능은 모든 사용자가 사용 가능하다.

---

### 1차 스케치

main 화면 모습
![demo_main](https://github.com/kngslbm/study/assets/148850117/c94fba5d-35c6-4bc7-9153-fc871087aea8)

부트스트랩을 사용하여 전체 틀을 잡았다.

상단 nav바 팀원이름 클릭시 각각 팀원개인 페이지 모습
![demo_member](https://github.com/kngslbm/study/assets/148850117/9b48cef2-bfc0-4c2d-a81a-fcba452b2383)
페이지는 오른쪽과 왼쪽으로 구역을 나누었고

왼쪽에는 각 팀원의 프로필을, 오른쪽에는 도움 리스트를 배치했다.

---

### 1차 완성본

이틀이라는 작업기한내에 완성하고 제출한 1차 완성본 main 화면이다.
![1차 완성본 index](https://github.com/kngslbm/study/assets/148850117/713108e9-5716-4c33-ab8b-1e8c9f022954)

상단 nav바의 라인을 없애고 색을 확실한 검정으로 했다.

<br>
<br>

각 팀원들의 페이지이다.
![1차완성본 Han](https://github.com/kngslbm/study/assets/148850117/d3f7d79c-4218-4e7a-a686-59d74c602f1b)
![1차완성본 Shin](https://github.com/kngslbm/study/assets/148850117/a379929d-69eb-424b-8445-ee8dd63b4505)
![1차완성본 Kim](https://github.com/kngslbm/study/assets/148850117/326b08d7-a81f-4e3c-b074-67df3c675cec)
![1차완성본 Kang](https://github.com/kngslbm/study/assets/148850117/7a5fccbd-9c54-4ebb-a818-3bc30294f228)

html과 CSS, 프론트엔드 쪽에 있어서는 검정색을 테마로 전체적으로 깔끔한 느낌을 살리려고 노력했다. 

어차피 제출기한 내에 (그리고 아직 부족한 나의 실력 내에서도) 구현할 수 있는 기능들이 제한적이고 그 양도 적을 테니,

"팀원들간에 도움을 요청하고 서로 도움을 줄 수 있는" 우리 프로젝트의 핵심 기능만을 중점으로

그 외에 다른 자잘한 기능이나 디자인적인 요소들은 배제하려고 했다. 

팀원들 제각각의 사진이었던 프로필의 이미지는 같은 형식의 캐릭터로 통일,

팀원들의 한 줄 소개글도 통일감을 줌.

<br>

오른쪽 아래의 "Home"을 클릭하면 다시 main 화면으로 돌아갈 수 있다.

각 페이지는 Python route 함수를 통해 팀원들 각각의 데이터를 가져와 만들어지게 작성했기 때문에

만약 팀원이 바뀐다고 해도 파이썬에서 데이터 값만 바꾸면 html을 건들지 않고 팀원의 프로필을 변경할 수 있다.

<br>

![HELPME 버튼 모달](https://github.com/kngslbm/study/assets/148850117/162a70c5-fbc5-4991-939d-087c337a0ab6)

도움 리스트 오른쪽 위의 "HELP ME" 를 클릭하면 리스트를 추가할 수 있는 modal 이 뜨고

입력한 데이터는 SQLite를 통해 Local DB 에 저장되어 관리된다.

각 팀원 페이지에서 입력한 data 를 알맞는 팀원 페이지에 리스트로 만들기 위해서는

먼저, 저장되는 data에 "어떤 페이지로 부터왔는지"에 대한 정보가 포함되어 있어야 했다.

이를 위해 url 의 마지막 부분을 가져와 username 이라는 값을 포함시켰다.

```py
# leader HELP ME 버튼 db 적용 
@app.route('/help/create/leader')
def helplist_create():
    # form으로 데이터 입력 받기
    helptitle_receive = request.args.get("helptitle")
    helpcontent_receive = request.args.get("helpcontent")
    username_receivee = request.url.split('/')[-1] # 현재 URL을 분석하여 username을 가져옴 여기선 leader -> 라고 기대했지만 "leader?helptitle=test&helpcontent=test" 이런 값을 가져와서
    username_receive = username_receivee.split('?')[0]  # 여기서 ? 기준으로 한번 더 나눴음 이제 username leader로 잘나옴

    # 데이터를 DB에 저장하기
    help = Help(title=helptitle_receive, content=helpcontent_receive, username=username_receive)
    db.session.add(help)
    db.session.commit()

    return redirect(url_for('leader'))
```
그 과정에서 위 코드의 주석으로 설명된 것과 같은 문제가 있었고 설명된 방법과 같이 해결을 하였다.

 <br>
 
![Helping버튼모달](https://github.com/kngslbm/study/assets/148850117/546bfb03-78d3-4106-8523-4e99aa5dc706)

각 리스트 내부에 있는 "Helping"을 클릭하면 리스트에 답글을 쓸 수 있는 modal 이 뜨고 마찬가지로 SQLite 를 통해 Local DB 에 저장된다.

도움 리스트를 생성하는 방법과 마찬가지의 방법으로 username 값을 포함시켜서 DB에 저장되게 하였다.




<br>
<br>
<br>

---


### 개발 관련 메모

아래 메모들은 팀원들과 작업을 하며 필요한 기능들과 개선점을 고민하며 공동으로 작성했던 리스트이다.

해결을 하면 줄을 그엇었다.

아직 해결하지 못해 줄이 그어지지 않은 리스트들도 있다.

우선순위에서 밀려 단순히 제출기한이 촉박해서 못한 것도 있고,

많은 시간을 쏟았음에도 지식이 부족해 프로젝트 기간동안 도저히 방법을 못찾은 리스트도 있다.

---

- ~~helpme 버튼 기능 필요~~ **해결**

- ~~helping버튼 도움주기 기능도 필요~~ **해결**

- ~~helping 모달창 내부 완성~~ **해결**

- ~~색깔 더 진한 검정으로. 지금 뭔가 누리끼리 검정.~~**해결**

- ~~nav 바 경계선 없는게 나을듯?~~**해결**

- ~~글씨체 힙하긴한데 좀 더 깔끔하면 좋을것 같아요..(전체적으로 색이나 요소들이 깔끔한 느낌으로 통일되면 좋을 것 같아요)~~ **해결**

- ~~개발과 관련된? 도와조 리스트를 몇 개 만들어놔야하지 않을까 싶어요..! 2~3개? -> 데이터베이스의 대답들이 모든 리스트에 중복됨 제대로 하려면 기능 추가 필요

- ~~개인설명중 TMI내용이 없는 것 같아 블로그주소 및 MBTI 적었던 곳에 TMI 칸도 만들어보겠습니다(하단에 칸 추가하면 간격 맞지 않아서 길이를 늘렸습니다)~~ **지저분해서 삭제**

- 각 팀원 페이지 들어갈때 상단 네브바에 해당 팀원 이름이 굵어 진다거나 표시가 필요 -> 굵어지게 만드니까 옆에 팀원들 이름 위치가 조금씩 밀리고, 거기서 오는 변화가 눈에 거슬리고 지저분해보임

- ~~리스트 오른쪽 상단 날짜.  맞게 들어가게 해야함~~ **지저분, 삭제하기로 함.**

- main 에서 팀 이름 밑으로 내용추가

- ~~helpme, helping 두버튼 모달이 따로 작동 안되는 문제~~  **해결**

- ~~입력값 db 연동 리스트 만들수 있게 하기~~ **해결**

- 팀원 페이지 별로 각각 해당 팀원 데이터만 가져올 수 있게 해야함 -> 도움 리스트는 해결, 도움 answer 해결 못함

- ~~각자 프로필 소개  사진 업로드 →이거 즉시 중단! db 적용 후에 각자 프로필 업로드할거임~~ **완료**

- ~~팀원 페이지에서 다시 홈으로 돌아가는 버튼 없음 ←**해결** -> 이거 가운데 말고 한쪽으로 미는게 나을듯? 저는 오른쪽 추천~~ **해결**

- ~~index에서 JS CDN이 없어서 토글 작동 안되던 오류~~**해결**

- ~~프로필 사진 각자 너무 다르고 지저분해서 그냥 zep 아바타 캡처로 통일하는거 어떰?~~ **해결**

---
