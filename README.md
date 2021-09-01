<br>

## **✨ 향해99 최종 프로젝트 Delight**
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
 ✏ [인스타그램 DB 구축]

- 음식이 가지고 있는 정보는 <br>
  인스타그램 크롤링을 통해 얻은 **인스타그램DB**와 음식이 가지는 고유의 특징인, **재료DB**로 이루어져 있습니다.
  
  <br>
- 인스타그램 DB 구축을 위해 <br>
  **Selenuim 라이브러리를 활용**하여 1개 음식당 200개의 인스타그램 게시글을 크롤링하였습니다.

<br>
<br>
✏ [모델링]

- 추천 모델은 비지도학습(Unsupervised learning) 중 하나인<br>
  **협업필터링**(Collaborative Filtering, CF) 모델을 사용하였습니다.
  
  <br>
- 사용자 기반 협업필터링(User Based CF, UBCF)이 아닌<br>
  **컨텐츠 기반 협업필터링**(Contents Based CF, CBCF)을 사용하였습니다.
  
  <br>
- 음식이 가지고 있는 정보를 벡터로 표현하고, 각 음식들간의 코사인 유사도를 구해<br>
  **가장 유사도가 높은 음식을 3종을 추천**하고 있습니다.
