import requests  # can request/pullout data from a website
from bs4 import BeautifulSoup  # helps parse individual data
import inspect
import smtplib
import time
import getpass

# URL = 'https://www.amazon.com/Powerbeats-Pro-Totally-Wireless-Earphones/dp/B07R5QD598/
# ref=sr_1_4?dchild=1&keywords=airpods+pro&qid=1585944327&sr=8-4 '

URL = 'https://www.futwiz.com/en/fifa20/career-mode/players'

headers1 = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/80.0.3987.149 Safari/537.36'
}  # gives info about the browser


def check_price(email1, email2, passwd):

    page = requests.get(URL, headers=headers1)  # storing the data in variable

    soup = BeautifulSoup(page.content, 'html.parser')  # storing the parsed data in variable
    # soup = BeautifulSoup(page.content, "lxml")

    ratingrow = soup.find_all(class_="highestbarcolour")  # finding all rows with ratings(class = "hi..color") and poten

    ratinglist = []

    for row in ratingrow:
        for j in row:
            j1 = int(j)
            ratinglist.append(j1)

    print(ratinglist)

    count = 0
    for rating in ratinglist:
        if rating > 90:
            count += 1

    if count > 20:
        send_email(email1, email2, passwd)



def send_email(email1, email2, passwd):
    server = smtplib.SMTP('smtp.gmail.com', 587)  # protocal
    server.ehlo()  # command sent by an email server to identify itself connecting to another email
    server.starttls()  # encrypts connection
    server.ehlo()

    # server.login('subidbasaula@gmail.com', 'vvtc uwju mcoz omyf')

    # print(email1, passwd)
    server.login(email1, passwd)

    subject = 'More than 10 90 rated players!'
    body = 'Check the futwiz site: : https://www.futwiz.com/en/fifa20/career-mode/players, {}'.format(passwd)

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        email1,
        email2,
        msg
    )

    print("Email has been sent!")

    server.quit()


em1 = input("\nEnter your email: ")
em2 = input("Email of recipient: ")
passw = getpass.getpass('Enter your password: ')

while True:
    check_price(em1, em2, passw)
    time.sleep(2*60)