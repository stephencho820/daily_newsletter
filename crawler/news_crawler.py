import requests
from bs4 import BeautifulSoup
import time

def crawl_news(query, yesterday, today):
    news_list = []
    page = 1  # Start from page 1

    while True:
        # 일 단위로 필터링된 URL을 생성, 페이지 번호 추가
        url = f"https://search.naver.com/search.naver?where=news&query={query}&sm=tab_pge&sort=0&photo=0&field=1&pd=3&ds={yesterday}&de={today}&docid=&related=0&mynews=1&office_type=1&office_section_code=1011&nso=so:r,p:from{yesterday.replace('.', '')}to{today.replace('.', '')}&is_sug_officeid=0&office_category=3&service_area=0&start={page}"
        #print(url)
        print(f"Fetching page {page}...")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 뉴스 제목, 링크, 요약, 날짜, 매체명 추출
        items = soup.select(".news_wrap")
        
        if not items:
            # 더 이상 결과가 없으면 반복 종료
            print("No more news articles found.")
            break

        for item in items:
            title = item.select_one(".news_tit").text
            link = item.select_one(".news_tit")["href"]
            summary = item.select_one(".news_dsc").text
            date = item.select_one(".info_group .info").text  # 뉴스 날짜 추출
            media_name = item.select_one(".info_group .press").text.strip()  # 매체명 추출
            
            news_list.append({
                "title": title,
                "link": link,
                "summary": summary,
                "date": date,
                "media_name": media_name
            })
        
        # 잠시 대기 후 다음 페이지로 넘어감
        time.sleep(0.5)  # 서버 과부하 방지를 위해 지연시간 추가
        page += 10  # 네이버 뉴스는 페이지 당 10개의 결과를 표시하므로, 페이지 번호를 10씩 증가

    return news_list

# Example usage
# query = "반도체"
# yesterday = "2024.10.11"
# today = "2024.10.12"

# news_data = crawl_news(query, yesterday, today)

# # Display the number of news articles crawled
# print(f"Total news articles fetched: {len(news_data)}")
