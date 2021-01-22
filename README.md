# 프로젝트 정리 Repository

### 프로젝트 및 공모전 자료

- 코드
- 분석 개요 및 요약
- 최종 결과 정리
- 기타 정리 자료



### 프로젝트 항목

1. 텍스트마이닝으로 기준금리분석
   - 금융통화위원회 의사록 텍스트마이닝을 통한 기준금리 분석
   - 참고논문 : Deciphering Monetary Policy Board - Minutes through Text Mining Approach: The Case of Korea

   - 파이썬 eKoNLPy 사용
   - Scrapy 사용하여 데이터 수집, 나이브 베이즈 모델로 n-gram 어조 분석
   - 내 역할 : 논문 번역  및 요약, 금리 데이터 크롤링 및 라벨링, n-gram 추출, 코퍼스 라벨링, 감성분석, 문서의 tone과 기준금리간의 상관관계 분석, 시각화
2. SNS프로파일링

   - 인스타그램의 텍스트와 커뮤니티를 이용하여 User의 성별, 연령대 예측
   - Scrapy 사용하여 데이터 수집, SVM과 KoBert모델로 텍스트 분석, CNM알고리즘으로 커뮤니티 분석
   - 참고논문 : Twitter user profiling based on text and community mining for market analysis (Kazushi Ikeda, Gen Hattori, Chihiro Ono, Hideki Asoh, Teruo Higashino, 2013)
   - 내 역할 : 논문 번역 및 요약, 인스타그램 데이터 크롤링, SVM으로 성별 예측
3. 라벨링_앱개발

   - 텍스트 라벨링을 위한 애플리케이션 제작
   - SNS프로파일링 프로젝트에 수집했던 데이터를 학습데이터로 이용, User의 성별, 연령대, 거주지, 관심사를 라벨링
   - MariaDB 이용하여 데이터베이스 구축, React로 애플리케이션 제작
   - 내 역할 : 데이터베이스 구축(SQL)
4. 종목 분석보고서 자동생성 AI
   - 종목명, 기간 검색으로 해당 기간 이슈와 뉴스 및 예측 그래프 제공하는 분석보고서 웹서비스
   - LDA 토픽 모델링
   - KoBert 모델로 텍스트 학습 후 XGBoost로 시계열 예측
   - 내 역할 : 데이터 수집, 토픽 모델링 최적화
