from crawler.news_crawler import crawl_news
from emailer.email_sender import send_email
from datetime import datetime, timedelta
import pandas as pd

if __name__ == "__main__":
    print("Starting the newsletter...")

    # 섹션별 키워드 리스트
    keywords_by_section = {
    #    "반도체": ["반도체", "HBM", "파운드리", "Foundry", "SLI", "TSMC", "GPU", "엔비디아"],
        "반도체": ["반도체"],
    #    "배터리": ["배터리", "2차 전지", "전기차", "테슬라"],
    #    "AI/로봇": ["AI", "인공지능", "로봇", "robot", "OPENAI", "오픈AI"]
    }
    
    # # 네이버 뉴스에서 사용할 매체 코드 리스트 (중앙일보: 1025, 동아일보: 1020 등)
    # channels = ["1025", "1020"]  # 예시로 중앙일보와 동아일보 매체 선택

    # 어제 날짜와 오늘 날짜를 계산하여 URL에 반영
    today = datetime.now().strftime('%Y.%m.%d')
    yesterday = (datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)).strftime('%Y.%m.%d')
    
    # 각 섹션별 뉴스 리스트를 저장할 딕셔너리
    news_by_section = {}

    # 각 섹션 및 키워드에 대해 크롤링 실행
    for section, keywords in keywords_by_section.items():
        all_news_for_section = []
        for keyword in keywords:
            print(f"Crawling news for keyword: {keyword}")
            news_list = crawl_news(keyword, yesterday, today)  # 키워드, 매체, 날짜 전달
            all_news_for_section.extend(news_list)  # 크롤링된 뉴스를 추가
        news_by_section[section] = all_news_for_section  # 섹션별 뉴스 저장
    
    print("##################")
    # print(news_by_section)
    news_list = news_by_section['반도체']
    df = pd.DataFrame(news_list)
    print(df)
    #실행 결과 {'반도체': [{'title': '10월 1∼10일 수출, 전년比 33% 증가… 반도체 수출 ‘맑음’', 'link': 'https://biz.chosun.com/policy/policy_sub/2024/10/11/6S2ZYZ6TPFGTTJ6PIKGCQNBB2A/?utm_source=naver&utm_medium=original&utm_campaign=biz', 'summary': '  조업일수 하루 더 많은 영향 반도체 수출 45.5% 증가 무역수지는 22억불 적자 10월 1~10일 수출이 전년 동기 대비 33.2% 증가 했다. 이달 초도 국군의날... 주요 품목별로 보면 반도체 수출이 전년 동기 대비 45.5% 늘었다. 승용차와 선박 수출도 전년 동기 대비 28.9%, 265.0% 증가했다. 반면 석유제품과... ', 'date': '조선비즈언론사 선정', 'media_name': '조선비즈언론사 선정'}, {'title': 'AMD AI 반도체 공개...엔비디아에 도전장', 'link': 'http://www.fnnews.com/news/202410111017371162', 'summary': '  AMD가 새로운 인공지능(AI)용 칩을 공개하면서 엔비디아에 도전장을 냈다. 10일(현지시간) 경제전문방송 CNBC는 AMD가 미국 샌프란시스코에서 열린 행사에서 인스팅트 MI325X를 공개하면서 엔비디아가 내년부터 본격적으로 대량 생산해 인도할 그래픽처리장치(GPU)인 블랙웰을 겨냥하고 있다고... ', 'date': '파이낸셜뉴스', 'media_name': '파이낸셜뉴스'}, {'title': "삼성전자,  반도체 부문 '비핵심' LED 사업 접는다", 'link': 'http://www.newsprime.co.kr/news/article.html?no=657949', 'summary': '   삼성전자(005930)가 반도체 사업을 담당하는 디바이스솔루션(DS) 부문 산하에 있는 비핵심 분야인 발광다이오드(LED) 사업에서  철수한다. 11일 업계에... 삼성전자는 LED 사업을 접는 대신 최근 수요가 늘고 있는 전력 반도체와 마이크로 LED 사업에 집중할 방침이다. 이에 따라 기존 LED 사업팀 인력 중... ', 'date': '프라임경제', 'media_name': '프라임경제'}, {'title': '[단독]  삼성전자, ‘4조원대 반도체 기술 유출’ 전직 임원 아파트·예금...', 'link': 'https://biz.chosun.com/topics/law_firm/2024/10/11/UADNEOL6OFGE7EOB7XU4BG675U/?utm_source=naver&utm_medium=original&utm_campaign=biz', 'summary': '  삼성전자가 반도 체 기술을 중국에 유출한 혐의로 기소된 임원 출신 최진석(66)씨를 상대로 110억원대 손해배상을 받기 위해 최씨의 서울 강남 아파트와... 한편, 삼성전자·하이닉스반도체 임원을 지낸 최씨는 삼성전자 수석연구원 출신 오모씨(60) 등과 함께 삼성전자가 독 자 개발한 D램 공정 기술을 중국에... ', 'date': '조선비즈언론사 선정', 'media_name': '조선비즈언론사 선정'}, {'title': '"반도체 45%·선박 265% 급증"…이달 10일 새 수출 33%↑', 'link': 'http://news.mt.co.kr/mtview.php?no=2024101108472618756', 'summary': "  특히 전체 수출의 5분의 1을 차지하는 반도체가 45%, 선박이 265% 증가하면서 호조세를 이끌었다. 관세청이 11일 발표한 '10월 1일~10일 수출입 현황... 이달 10일간의 수출 품목을 보면 반도체가 전년동기 대비 45.5% 급증하면서 호조세를 이끌었다. 반도체가 전체 수출에서 차지하는 비중은 20%로... ", 'date': '머니투데이', 'media_name': '머니투데이'}, {'title': "머크, 한국서 차세대 반도체 개발 '신규 R&D 센터' 개소", 'link': 'https://zdnet.co.kr/view/?no=20241010080827', 'summary': '  개소는 반도체 산업의 혁신을 주도하기 위한 머크의 여정에서 중요한 역할을 할 것"이라며 "이 연구소를 통해 반도체 기술 의 미래를 리드하고 빠르게 진화하는 디지털 산업의 수요 충족을 대응하여, 고객사의 혁신을 가속화하는데 기여할 것으로 확신한다"고 강조했다. 김우규 한국 머크 대표이사는... ', 'date': '지디넷코리아언론사 선정', 'media_name': '지디넷코리아언론사  선정'}, {'title': 'KTL, 반도체 소재·부품 산업 자립화에 앞장', 'link': 'http://www.enewstoday.co.kr/news/articleView.html?idxno=2185694', 'summary': "  한국산업기술시험원(이하 KTL)은 경상북도 및 구미시와 함께 '반도체 소재·부품 시험평가센터 구축' 사업을 실시하고 반도체 산업 자립화를 위한 소재·부품 공급망 확보에 나선다고 11일 밝혔다. 최근 반도체 산업에 대한 패권경쟁이 가속화되면서 미국, 중국, 일본 등 주요 국가들이 자국 중심의 공급망 구축을... ", 'date': '이뉴스투데이', 'media_name': '이뉴스투데이'}, {'title': '외국인 매도 3년만에 최고···“대부분 반도체주”', 'link': 'https://www.mk.co.kr/article/11137286', 'summary': '  당시에는 국내에 코로나19 확산세가 지속되고 반도체업 전망이 어두워지며 외국인들이 장기간에 걸쳐 매도세를 지속했다. 박재영 금감원 증권거래감독팀장은 최근 외국인 매도세에 대해 “매도된 주식 대부분은 반도체주다.  인공지능(AI)의 수익성에 대한 의문이 제기되며 관련 종목들이 함께... ', 'date': '매일경제', 'media_name': '매일경제'}, {'title': '독일 머크사, 안성에 반도체 SoD 연구소 개소', 'link': 'https://www.etnews.com/20241010000424', 'summary': '  머크는 반도체·디스플레이 소재와 반도체 제조용 기기를 생산하는 글로벌이다. 연구소는 머크가 900만 유로(약 120억원)를 투자해 2년3개월 공사를 거쳐 안성공장 내 총면적 약 390㎥로 조성했다. 이곳에서는 반도체 배선 관련 전처리 공정의 제품인 SoD의 연구 개발 및 응용 테스트를 진행할 예정이다.... ', 'date': '전자신문', 'media_name': '전자신문'}, {'title': '서울반도체, 3분기 매출 3023억…전년 동기 대비 7%↑', 'link': 'http://news.mt.co.kr/mtview.php?no=2024101116184052596', 'summary': '  서울반도체가 올해 3분기 연결기준 잠정 매출이 3023억원으로 집계됐다고 11일 공시했다. 지난해 같은 기간(2820억원)대비 7% 증가했다. 또 시장 전망치인 2953억원을 웃돌았다. 서울반도체는 다음달 3분기 확정실적을 발표하고 세부 내용을 공개한다. ', 'date': '머니투데이', 'media_name': '머니투데이'}]}
    # 이메일 전송
    send_email(news_by_section)
    
    print("Newsletter sent and process completed!")


