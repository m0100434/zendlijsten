# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:56:59 2021

@author: ArxXi
"""


from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import pickle
from datetime import date


def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)


def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)

def remove_entry(index):
    ourtime.pop(index-entries_deleted)
    # print("time which is going to be deleted = "+ ourtime[index])
    # ourtime[index] = "-"

"""
Een v
VTM v
Vier v
Canvas v
Vitaya = vtm 4 v
Q2  v
Vijf v
CAZ = vtm 3 v
Zes v
Ketnet v
La Une v
RTL-TVI v
AB3 ?
La Deux v
Club RTL v
Plug RTL ?
La Trois v
Nickelodeon FR ?
"""

def channel_identifier(anchor_link):
    tmp = anchor_link.split("/")
    if(tmp[4] == "een"):
        return "een"
    if (tmp[4] == "canvas"):
        return "canvas"
    if (tmp[4] == "vtm"):
        return "vtm"
    if (tmp[4] == "vier"):
        return "vier"
    if (tmp[4] == "vijf"):
        return "vijf"
    if (tmp[4] == "zes"):
        return "zes"
    if (tmp[4] == "rtl-tvi-hd"):
        return "RTI TVI HD"
    if (tmp[4] == "la-une"):
        return "LA UNE"
    if (tmp[4] == "la-deux"):
        return "LA DEUX"
    if (tmp[4] == "ketnet"):
        return "KETNET"
    if (tmp[4] == "vtm2"):
        return "vtm2"
    if (tmp[4] == "vtm3"):
        return "vtm3"
    if (tmp[4] == "club-rtl"):
        return "club-rtl"
    if (tmp[4] == "vtm4"):
        return "vtm4"
    if (tmp[4] == "caz-2"):
        return "caz-2"
    if (tmp[4] == "la-trois"):
        return "la-trois"


    return "null"


# options = FirefoxOptions()
# options.add_arguments("--headless")
# driver = webdriver.Firefox(options=options)

#0 click een, canvas,vtm, vier
#1 click vjtf
#2 click zes
#9 click la une , la deux, ketnet, la trois
#14 click

date_of_movie = ""
links_traveresed = 0

default_link = "https://www.demorgen.be/tv-gids/dag/24-04-2021"


if(len(default_link.split("/")) ==6):
    date_of_movie =default_link.split("/")[5]
    print("got true")
else:
    date_of_movie = date.today()
    date_of_movie = date_of_movie.strftime('%d/%m/%y')

driver = webdriver.Firefox()
driver.maximize_window()
driver.get(default_link)




# driver.implicitly_wait(15)
delay = 10 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'sp_message_iframe_404503')))
    print("Iframe element ready")
except TimeoutException:
    print("Iframe not loaded issue")


a = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(1)

print("switching to iframe done")

green_button = driver.find_element_by_xpath('//button[text()="Akkoord"]')
green_button.click()

time.sleep(10)

print("It will be on schedule website")
driver.switch_to.default_content()

#declarration
iteration = 0
ourtime = []
channel_names = []
ad_index = 82
associated_channel_name = []
production_date = []
show_title = []
current_episode = []
total_episode = []
season_number = []
myepisode_number = ""
description = []
genre = []
series_movie = []
actors = []
episode_text = " "
entries_deleted = 0
number_of_clicks = [0,1,2,6,9,14]



links = []
while (iteration != (len(number_of_clicks))):
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/div/div/div[1]/div[2]/button[2]')))
        next_button = driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div/div/div[1]/div[2]/button[2]")
        for i in range(0, number_of_clicks[iteration]):
            print("next button should be clicked")
            next_button.click()
            driver.implicitly_wait(2)
        print("Next Button located")
    except TimeoutException:
        print("Next Button Not Located")



    a = driver.find_elements_by_class_name("tvgm-channel__logo-placeholder")



    #Getting channel names on current page
    for i in range(0,len(a)):
        ourlink = a[i].get_property("href")
        distributed = ourlink.split("/")
        channel = distributed[4]
        channel_names.append(channel)


    #time of shows

    b = driver.find_elements_by_class_name("tvgm-broadcast-teaser__time")
    for i in range(0,len(b)):
        ourtime.append(b[i].text)


    c = driver.find_elements_by_class_name("tvgm-broadcast-teaser__link")



    for i in range(0,len(c)):
        if((c[i].get_property("href")) not in links):
            links.append(c[i].get_property("href"))



    #getting link


    for i in range(links_traveresed,len(links)):
        tmp = links[i]
        episode_text = " "
        if(channel_identifier(tmp) != "null"):
            associated_channel_name.append(channel_identifier(tmp))
            driver.get(tmp)
            #Page visited

            try:
                production_date.append(driver.find_element_by_class_name("tvgm-broadcast-detail__productionyear").text)
            except NoSuchElementException:
                print("Production Date not found")
                production_date.append("-")

            try:
                show_title.append(driver.find_element_by_class_name("tvgm-broadcast-detail__title").text)
            except NoSuchElementException:
                print("Show title not found")
                show_title.append("-")


            try:
                description.append(driver.find_element_by_class_name("tvgm-broadcast-detail__description").text)
            except NoSuchElementException:
                print("Description not found")
                description.append("-")

            try:
                actors.append(driver.find_element_by_class_name("tvgm-broadcast-detail__castandcrew").text)
            except NoSuchElementException:
                print("Actors not found")
                actors.append("-")


            try:
                temp = driver.find_element_by_class_name("tvgm-broadcast-detail__info-playable").text
                temp = temp.split(",")

                if(len(temp) == 2):
                    series_movie.append(temp[0])
                    genre.append(temp[1])
                    print("This got executed (Genre)")
                if (len(temp) == 1):
                    series_movie.append(temp[0])
                    genre.append("-")

            except NoSuchElementException:
                print("Series/Movie not found")
                series_movie.append("-")
                genre.append("-")


            try:
                driver.find_element_by_class_name("tvgm-broadcast-detail__episode-numbers")
                myepisode_number = driver.find_element_by_class_name("tvgm-broadcast-detail__episode-numbers").text

                tmp = myepisode_number.split(" ")

                season_number.append(tmp[1])
                #changing done
                if(len(tmp)>2):
                    combined_episode_number = tmp[3].split("/")
                    if(len(combined_episode_number) ==2):
                        current_episode.append(combined_episode_number[0])
                        total_episode.append(combined_episode_number[1])
                        print("This got executed (Episodes)")

                    if (len(combined_episode_number) == 1):
                        current_episode.append(combined_episode_number[0])
                        total_episode.append("-")
                else:
                    #if both not available
                    total_episode.append("-")
                    current_episode.append("-")
                print("Epsisode starting and ending exist ")



            except NoSuchElementException:
                print("Starting ending Episode not exist")
                season_number.append("-")
                current_episode.append("-")
                total_episode.append("-")
            #tester
            #break

        else:
            #not interested in this channel
            remove_entry(i)
            entries_deleted = entries_deleted +1
            print("****** ENTRY SKIPPED ********")

    links_traveresed = len(links)
    #tester
    # if(i == ad_index):
    #     break

    driver.get(default_link)
    iteration = iteration+1



driver.close()



# print("Starting time = " + ourtime[ad_index])
# print("Actors = " + actors[ad_index])
# print("Associated Channel Name = " + associated_channel_name[ad_index])
# print("Production Date = " + production_date[ad_index])
# print("Show title = " + show_title[ad_index])
# print("Current Episode = " + current_episode[ad_index])
# print("Total Episode = " + total_episode[ad_index])
# print("Genre  = " + genre[ad_index])
# print("Series_Movie = " + series_movie[ad_index])
# print("Season Number = " + season_number[ad_index])

# for i in range(0,len(ourtime)):
#     if(ourtime[i] == "-"):
#         del(ourtime[i])

print(ourtime)
print(actors)
print(associated_channel_name)
print(production_date)
print(show_title)
print(current_episode)
print(total_episode)
print(genre)
print(series_movie)
print(season_number)


print(len(ourtime))
print(len(actors))
print(len(associated_channel_name))
print(len(production_date))
print(len(show_title))
print(len(current_episode))
print(len(total_episode))
print(len(genre))
print(len(series_movie))
print(len(season_number))




import csv

with open('channel_data_210424.csv', mode='w',newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in range(0,len(ourtime)):
        if(i==0):
            employee_writer.writerow(["Date of Movie","Starting Time","Actors","Channel Name","Production Date","Title of Show","Current Episode","Total Episodes","Genre","Series/Movie","Season Number"])

        employee_writer.writerow([date_of_movie,ourtime[i],actors[i],associated_channel_name[i],production_date[i],show_title[i],current_episode[i],total_episode[i],genre[i],series_movie[i],season_number[i]])
