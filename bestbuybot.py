from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#open Chrome driver
driver = webdriver.Chrome(executable_path='C:/Users/andyp/AppData/Local/Temp/Temp1_chromedriver_win32.zip/chromedriver.exe')

url = 'https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&browsedCategory=abcat0507002&id=pcat17071&iht=n&ks=960&list=y&qp=soldout_facet%3DAvailability~Exclude%20Out%20of%20Stock%20Items&sc=Global&st=categoryid%24abcat0507002&type=page&usc=All%20Categories'

#retieve the url link and go to the website
driver.get(url)

driver.maximize_window()

button = driver.find_element(By.XPATH, "/html/body/div[4]/main/div[10]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[5]/ol/li[1]/div/div/div/div/div/div[2]/div[2]/div[3]/div/div/div/div/div/div/button")
button.click()

time.sleep(5)
cart = driver.find_element(By.XPATH, "/html/body/div[9]/div/div[1]/div/div/div/div/div[1]/div[3]/a")
cart.click()

time.sleep(5)
checkout = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div[1]/button")
checkout.click()

time.sleep(5)
guest = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/main/div[2]/div[4]/div/div[2]/button")
guest.click()

time.sleep(5)
#enter credentials
first_name = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[1]/label/div/input").send_keys("Andy")
last_name = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[2]/label/div/input").send_keys("Pen")
address = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[3]/div[2]/div/div/input").send_keys("705 Auburn St")
city = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[5]/div/div[1]/label/div/input").send_keys("Whitman`"
                                                                                                                                                                                                                               "")
state = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[5]/div/div[2]/label/div/div/select").send_keys("MA")
zip_code = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[6]/div/div[1]/label/div/input").send_keys("02382")
email = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[2]/label/div/input").send_keys("donrezi@sah-ilk-han.com")
phone = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[3]/label/div/input").send_keys("(781) 447-3190")
proceed = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button/span").click()
time.sleep(5)
#address_confirm = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[1]/div/div[1]/div/div/div/div/button[1]/span").click()
#time.sleep(5)
credit_card = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div[1]/div/section/div[1]/div/input")
credit_card.click()
credit_card.send_keys("4485454580909054")
month = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div[1]/div/section/div[2]/div[1]/div/div[1]/label/div/div/select").send_keys("04")
year = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div[1]/div/section/div[2]/div[1]/div/div[2]/label/div/div/select").send_keys("2022")
cvv = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[1]/div[1]/div/section/div[2]/div[2]/div/div[2]/div/input").send_keys("714")

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount==lenOfPage:
        match=True
#order = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[2]/div[2]/button").click()
