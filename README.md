## 🍗치킨푸드 프로젝트 소개
<div align=center><img src="https://i.ibb.co/3vH3Qrm/chickenfood-logo-2.png"></div>

**<div align=center> 오리지널 푸드 코스메틱 브랜드 스킨푸드 클론 프로젝트</div>**
<div align=center> 짧은 프로젝트 기간동안 개발에 집중해야 하므로 디자인/기획 부분만 클론했습니다.<br>
개발은 초기 세팅부터 전부 직접 구현했으며, 아래 데모 영상에서 보이는 부분은<br>
모두 백앤드와 연결하여 실제 사용할 수 있는 서비스 수준으로 개발한 것입니다.<br></div>

<br>

## 개발 인원 및 기간

- 개발기간 : 2021/8/2 ~ 2021/8/13
- 개발 인원 : 프론트엔드 4명, 백엔드 2명

<br>

## Modeling✏️
![](https://i.ibb.co/vdvZtj1/2021-08-13-6-05-44.png)

상기 모델링 중에서 브랜드(brands), 타입(types), 제품(products), 옵션(options),<br>
장바구니(inventorys), 찜하기(likes), 사용자(users)를 구현했습니다.

짧은 프로젝트 기간으로 인해, 쿠폰, 별도이미지 기능은 구현하지 못한 점이 아쉽습니다.

## 구현 페이지

### [시연 영상](https://www.youtube.com/watch?v=mMQE_7ZBouc)

### 메인/상품
![](https://i.ibb.co/b7Zz4Zc/2.gif)
![](https://i.ibb.co/zxs3VJy/image.gif)
![](https://i.ibb.co/JKqMtx9/image.gif)

### 로그인/회원가입
![](https://i.ibb.co/VSfcNNf/image.gif)
![](https://i.ibb.co/HHmS9zw/image.gif)

### 장바구니/찜하기
![](https://i.ibb.co/bv9BGq9/image.gif)

## **구현기능💻**


### **Members**

- 로그인 / 회원가입 / 아이디 중복 확인
- 정규표현식을 이용한 유효성 검사
- bcrypt 라이브러리를 이용한 암호화
- PyJwt 라이브러리를 이용한 사용자 인가
- 하나의 값으로 아이디, 전화번호 판단

### **Products**

- 브랜드, 타입 정보 호출
- quary parameter를 이용한 상품 필터링(브랜드별, 타입별, 인기순, 최신순)
- 상품 상세 정보 확인

### **Inventorys**

- 장바구니 담기 / 보기 / 삭제 / 변경
- 장바구니에 이미 있는 품목은 추가되는 만큼 수량 증가
- 장바구니 단일 품목 삭제, 선택 품목 삭제, 전체 품목 삭제

### **Likes**

- 찜하기 추가, 확인, 삭제 기능
- 회원 / 비회원별 다른 엔드포인트 지정
<br>
              
커머스의 기본적인 기능들을 다룰 수 있어서 전반적인 플로우를 알게 되어서 많은 것을 배울 수 있었고,<br>
비로그인 시에도 장바구니와 위시리스트를 이용할 수 있는 기능, 더욱 많은 조건과 정렬이 필요한 필터를 이용하지 못해서 아쉬움이 많았습니다.

<br>

## **사용 기술👍**

Backend : Python, Django, MySql, bcrypt, pyJWT, POSTMAN, linux


<br>

## **커뮤니케이션🤝**

우리 치킨푸드 팀은 3개의 Tool을 이용해서 원활한 커뮤니케이션 문화를 형성했습니다

<br>

### Trello
![](https://i.ibb.co/NFXB0Fk/2021-08-13-6-18-57.png)

- Front/Back/Together/Urgency로 라벨을 분류하고, 티켓 담당자를 표기해서 직관적으로 확인
- 미팅 기록을 간략하게 정리해서 로그에 저장
- 원활한 프-백간 통신을 위해 IP 주소는 메일 업데이트

<br>

### [Google Slides(Sketch)](https://docs.google.com/presentation/d/1rFAAUbpBN3LFsGWKH9x7yeRiELLk9Oc73x-uMjkLBgU/edit#slide=id.ge7965d3393_1_41)

- 각 페이지별 컴포넌트 분류하여 간략하게 도식화
- 컴포넌트마다 어떤 위치에 어떤 API를 사용하는지 직관적으로 확인 가능

<br>

### [Google Spreadsheet(API정의서)](https://docs.google.com/spreadsheets/d/1wxZXsXDVgNXm-ydtbAfFVf14YDt2or09lRiM9pgLmP4/edit#gid=0)

- API별 기능, Method, URI, Request 및 Response 정리
<br>

### Reference

- 이 프로젝트는 스킨푸드 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
