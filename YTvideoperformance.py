from selenium import webdriver
from time import sleep as sp
import sqlite3
print("welcome to my app:")

while True:
    db = sqlite3.connect('Ytvideo.db')
    cr = db.cursor()

    cr.execute("Create Table  if not exists video(channelname text,vidtitle text,views integer,upload text,likes text,dislikes text)")


    path = "C:\Program Files (x86)\chromedriver.exe"
    print("please enter a valid youtube video link or -1 to exit the app :")
    d = input("=========>")
    if d == '-1':
        break
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browse = webdriver.Chrome(executable_path=path, options=options)
    browse.get(d)
    sp(5)
    browse.maximize_window()
    sp(5)
    title = browse.find_element_by_xpath("""//*[@id="container"]/h1/yt-formatted-string""")
    tl = title.text
    sp(5)
    k = browse.find_element_by_xpath("""//*[@id="count"]/ytd-video-view-count-renderer/span[1]""")
    d = k.text
    l,e = d.split(' ')
    f = list(l)
    while ',' in f:
        f.remove(',')
    views = ''
    for i in f:
        views+=i
    views = int(views)
    g = views
    upload_time = browse.find_element_by_xpath("""//*[@id="info-strings"]/yt-formatted-string[1]""")
    b = upload_time.text
    sp(5)
    channel_name = browse.find_element_by_xpath("""//*[@id="text"]/a""")
    x = channel_name.get_attribute("innerText")
    sp(5)
    dislikes = browse.find_element_by_xpath("""//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[2]/a""")
    h = dislikes.get_attribute("innerText")
    likes = browse.find_element_by_xpath("""//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[1]/a""")
    u = likes.get_attribute("innerText")
    cr.execute(f"insert into video(channelname,vidtitle,views,upload,likes,dislikes) values('{x}','{tl}',{g},'{b}','{u}','{h}')")

    db.commit()
    db.close()
    print("succefully added to the database")

    browse.quit()


print("thanks for using the app")
