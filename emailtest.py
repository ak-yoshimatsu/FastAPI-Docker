from smtplib import SMTP
from email.mime.multipart import MIMEMultipart

# メール本文作成
from email.mime.text import MIMEText
from email.utils import formatdate


def createMIMEText(send_from: str, send_to: str, message: str, subject: str) -> MIMEText:
    """MiMETextを作成

    Args:
        send_from (str): 送信元メールアドレス
        send_to (str): 宛先メールアドレス
        message (str): 本文
        subject (str): 件名

    Returns:
        MIMEText: MIMEText
    """
    msg = MIMEText(message, 'html')

    msg['Subject'] = subject
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate()

    return msg


from_email = 'source@example.com'
to_email = 'destination@example.com'
subject = 'テスト件名'
message = 'テスト本文'

mime = createMIMEText(from_email, to_email, message, subject)
print('mime', mime)


def send_email(msg):
    # host = 'http://localhost'
    host = 'mailhog'
    port = 8025

    # サーバを指定する
    server = SMTP(host, port)

    # メールを送信する
    server.send_message(msg)

    # 閉じる
    server.quit()


send_email(mime)
