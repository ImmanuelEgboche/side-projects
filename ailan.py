from requests import sessions
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from requests_html import HTMLSession, AsyncHTMLSession
import time 
import configparser
# import config 
#NEED TO CREATE A CONFIG FILE WHICH STORES CARD DETAILS, PASSWORDS ETC


"""
SITE WE'RE CHOOSING 

"""
base_url = 'https://www.nike.com/launch'

#Identifies where the products are located using HTML elements.
def get_link():
    chosen_page = base_url + "t/air-jordan-1-low-travis-scott-fragment"
    session = HTMLSession()
    connector = session.get(chosen_page)
    #find html id - websites hide their hmtl elements
    products = connector.html.find("#shop-scroller",first=True).find("li")
    return products, session

#Given a target name match with the item on the website
def check_website(target_name):
    target_name_list = [i.lower() for i in target_name.split(' ')]
    potenial_urls = []
    products, session = get_link()
    for item in products:
        target_url = base_url + item.find("a", first=True).attrs['href']
        connector = session.get(target_url)
        product_name = connector.html.find('h5[class=headline-1 pb3-sm]',first=True).text.lower()
        found = True
        for q in target_name_list:
            if q not in product_name :
                found = False
                break
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        if found: 
            print(f"found a match{product_name}")
            #Is it avaiable for purchase?
            if is_avaiable(r):
                print("buy")
                potenial_urls.append(target_url)
            else:
                print("not there")
        else:
            print(f"no matches for {product_name} try again :P")
    return potenial_urls

#As the trainers arent out yet a element of prediction in needed
def is_avaiable(test):
    buybtn = test.html.find('input[value="add to cart"]',first=True)
    return (buybtn is not None)

#Purchase the trainers
def cop(url):
    driver = webdriver.FirefoxProfile()
    #url
    driver.get(url)
    btn = driver.find_with_id('add-remove-buttons').find_elements_by_tag('input')
    if len(btn) == 0:
        print("not avaiable")
        return
    btn[0].click()
    time.sleep(1)
    #checkout 
    checkout_url = "https://www.nike.com/checkout"
    # driver.find_element_by_id('order_billing_name').send_keys(config.NAME)
    # driver.find_element_by_id('order_email').send_keys(config.EMAIL)
    # driver.find_element_by_id('order_tel').send_keys(config.PHONE)
    # driver.find_element_by_id('bo').send_keys(config.ADDRESS)
    # driver.find_element_by_id('order_billing_zip').send_keys(config.ZIPCODE)
    # driver.find_element_by_id('order_billing_city').send_keys(config.CITY)
    # driver.find_element_by_id('rnsnckrn').send_keys(config.CREDIT_CARD)
    # driver.find_element_by_id('orcer').send_keys(config.CC_CVV)
    # driver.find_element_by_id('order_terms').click()
    # driver.find_element_by_id('store_address').click(
    ins_tags = driver.find_elements_by_tag_name('ins')
    for el in ins_tags:
        el.click()
    #Reformat config files and code
    select = Select(driver.find_element_by_id('order_billing_state'))
    select.select_by_value(config.STATE)
    select = Select(driver.find_element_by_id('credit_card_month'))
    select.select_by_value(config.CC_MONTH)
    select = Select(driver.find_element_by_id('credit_card_year'))
    select.select_by_value(config.CC_YEAR)

    time.sleep(2)

    # pay
    pay_btn = driver.find_element_by_id('pay').find_elements_by_tag_name('input')
    pay_btn[0].click()
    
def main(target_product):
    urls = check_website(target_product)
    print(f'found {len(urls)} matches')
    if len(urls) == 0:
        print('still no matches')
        return
    print('working url:{urls[0]}')
    url = urls[0]
    cop(url)
    print('done')
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ailan')
    parser.add_argument('--name', required=True,help="Specify product name to find and purchase")
    args = parser.parse_args()
    main(target_product=args.name)
