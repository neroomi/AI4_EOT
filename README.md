# 2.1 시작

- 조장: 박현수
- 조원: 이중헌, 정수경, 김연경, 박윤수
- 2.1 진행사항 : 기본적인 테이블, 화면 구성,  프로젝트 준비 
- 2.5 진행사항 : 모델 생성


## 2.6 수정 사항 
1. 각각 기능별 애플리케이션 분리   
날씨 weathers   
회원 users   
추천 recommends   
메모 bulletin   
각 애플리케이션에 있는 user 관련 내용 삭제   

2. 애플리케이션 URL 경로 수정 config/urls

3. template 경로 root 경로로 이동   
html 파일 저장 위치 templates/애플리케이션이름/파일명   
사용 시 애플리케이션이름/파일명.html

## 2.8 
1. 브랜치 >> feature/weathers/pys
2. 기존에 작업한 내용 업로드
	>1. Todayweather 기능 구현
	>	>geopy패키지를 이용해서 위도,경도를 구해 openweather api로 날씨데이터 수집
	>	
	>	2. 템플릿에 api데이터 출력
	>
	>4. 예보데이터 차트 만들준비
	>
3. 
