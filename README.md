<br>

## **🚩 향해99 최종 프로젝트 Delight**
<div align="center">
  <a href="https://delight99.co.kr">
  <img src="https://images.velog.io/images/zpswl45/post/769180e5-fb06-46aa-b553-07a68338945a/%E1%84%80%E1%85%B5%E1%86%BA%E1%84%92%E1%85%A5%E1%84%87%E1%85%B3%20%E1%84%85%E1%85%B5%E1%84%83%E1%85%B3%E1%84%86%E1%85%B5%E1%84%8B%E1%85%AD%E1%86%BC%20%E1%84%85%E1%85%A9%E1%84%80%E1%85%A9.png"/>
  </a>
  <br>
  👆👆 클릭 시 해당 서비스를 이용할 수 있습니다.
</div>

<br>

- 밥씨는 한끼 선택이 어려운 고객들 위하여<br>
  **"한끼 추천 기능을 통한 만족스러운 식사를 제공하여 즐거움과 기쁨을 드리고자 개발 된 서비스입니다."**


<br>
<br>

## **🚩 Delight 머신러닝 서버**
<br>
 🔹 [인스타그램 DB 구축]

- 음식이 가지고 있는 정보는 <br>
  인스타그램 크롤링을 통해 얻은 **인스타그램DB**와 음식이 가지는 고유의 특징인, **재료DB**로 이루어져 있습니다.

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;👉 <a href=""> 머신러닝에 사용할 DB를 인스타그램과 음식재료로 선정한 이유 📝</a><br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;👉 <a href=""> RDS가 아닌 CSV로 DB를 관리하는 이유 📝</a>

  <br>
- 인스타그램 DB 구축을 위해 <br>
  **Selenuim 라이브러리를 활용**하여 1개 음식당 200개의 인스타그램 게시글을 크롤링하였습니다.

<br>
<br>
🔹 [모델링]

- 추천 모델은 비지도학습(Unsupervised learning) 중 하나인<br>
  **협업필터링**(Collaborative Filtering, CF) 모델을 사용하였습니다.
  
  <br>
- 사용자 기반 협업필터링(User Based CF, UBCF)이 아닌<br>
  **컨텐츠 기반 협업필터링**(Contents Based CF, CBCF)을 사용하였습니다.
  <br>
  <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;👉 <a href="">UBCF가 아닌 CBCF를 선정한 이유 📝</a>
  
  <br>
- 음식이 가지고 있는 정보를 벡터로 표현하고, 각 음식들간의 코사인 유사도를 구해<br>
  **가장 유사도가 높은 음식을 3종을 추천**하고 있습니다.
  <br>
  <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;👉 <a href="">여러개의 음식을 Input으로 할 때 유사도가 가장 높은 음식 3종에 대한 선택기준 📝</a>
  
  <br>
- 추천 모델의 성능개선을 위해 **별도의 가중치**를 적용하였습니다.<br>
  가중치 적용 결과 전체 130종 음식중 106종의 음식이 추천되는 결과를 얻었습니다.<br>
  (적용 전: ??종의 음식 추천 이루어 짐)

<br>
<br>
🔹 [Flask 서버와 성능 개선]

- Java서버를 통해 유저가 선택한 음식 리스트를 받습니다.<br>
  받은 음식 리스트를 Input으로하며, **CBCF의 결과인 추천할 음식 3종류를 Java 서버로 보냅니다.(POST)**

  <br>
- 대용량 트래픽에 대비해 아래와 같은 방법으로 성능 개선을 하였습니다.<br>
  비동기처리를 위한 미들웨어인 **gunicorn을 적용**하였고 로드밸린싱을 위해 앞단에 **Nginx를 적용**하였습니다.
  <br>
  <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;👉 <a href="">스트레스 테스트로 알아보는 Nginx와 gunicorn 적용에 따른 성능차이 📝</a>

<br>
<br>

  ## **🚩 Requirements**
<br>

- python 3.7.10<br>
- scikit-learn 0.24.2<br>
- flask 2.0.1<br>
- flask-cors 3.0.10<br>
- pandas 1.3.0<br>
- konlpy 0.5.2<br>
- selenium 3.141.0

<br>
<br>

## 🚩 **Git - flow Branch 전략을 적용**
![](https://images.velog.io/images/zpswl45/post/7ecffd87-3dde-4abc-b7e3-9971b3a75dd9/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2021-07-30_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.48.33.png)


```
master  : 테스트 서버에서 테스트가 끝나고 운영서버로 배포 할 수 있는 브랜치
develop : 다음 버전을 출시전 테스트를 위한 브랜치 
feature : 기능을 개발하는 브랜치
release : 이번 출시 버전을 준비하는 브랜치
hotfix  : 운영중인 버전에서 발생한 버그를 수정 하는 브랜치
```
