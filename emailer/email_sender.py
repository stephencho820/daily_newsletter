import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_CONFIG

# HTML 템플릿 파일에서 내용을 읽어오는 함수
def load_template():
    with open("templates/email_template.html", "r", encoding="utf-8") as file:
        template = file.read()
    return template

def generate_section(news_list):
    # 뉴스 목록을 HTML 형식으로 생성
    section_html = ""
    for idx, news in enumerate(news_list, 1):
        section_html += f'<div class="news-item">{idx}. <a href="{news["link"]}">[{news["media_name"]}] {news["title"]}</a> ({news["date"]})<br>'
        section_html += f'   요약: {news["summary"]}</div><br>'
    return section_html

def send_email(news_by_section):
    # 이메일 설정 (config.py에서 불러옴)
    sender = EMAIL_CONFIG['sender']
    receivers = EMAIL_CONFIG['receivers']
    bcc = EMAIL_CONFIG['bcc']
    password = EMAIL_CONFIG['password']
    
    # 전체 수신자 리스트 생성 (수신자 + BCC)
    all_receivers = receivers + bcc

    # HTML 템플릿을 불러옴
    template = load_template()
    
    # 섹션별로 뉴스 HTML 생성
    반도체_news = generate_section(news_by_section.get("반도체", []))
    배터리_news = generate_section(news_by_section.get("배터리", []))
    AI_로봇_news = generate_section(news_by_section.get("AI/로봇", []))
    
    # 템플릿에서 변수를 실제 뉴스 내용으로 치환
    body = template.replace("{{ 반도체_news }}", 반도체_news)\
                   .replace("{{ 배터리_news }}", 배터리_news)\
                   .replace("{{ AI_로봇_news }}", AI_로봇_news)
    
    # 이메일 객체 생성 (다중 수신자를 위한 MIMEMultipart 사용)
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = ", ".join(receivers)  # 수신자를 이메일의 'To' 필드에 표시
    msg["Subject"] = "일일 주요 보도자료"
    
    # 이메일 본문 추가 (HTML 형식)
    msg.attach(MIMEText(body, "html"))
    
    # 이메일 전송
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, all_receivers, msg.as_string())  # all_receivers 리스트로 이메일 발송
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
