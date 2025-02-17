# import relevant libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# define url
url = "https://mb-vnext-identity.sharedo.tech/login?"

# set Chrome options to run in incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

# instantiate webdriver and open a chrome browser with options
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=chrome_options)

# maximize browser window
driver.maximize_window()

# load the webpage
driver.get(url)

# # find the first name field
# first_name = driver.find_element(By.XPATH, 'FILL IN')
# # fill out the first name field
# first_name.send_keys("FILL IN")


# # find the last name field
# last_name = driver.find_element(By.XPATH, 'FILL IN')
# # find the last name field
# last_name.send_keys("FILL IN")

# # find the email field
# email = driver.find_element(By.XPATH, 'FILL IN')
# # fill in the email field
# email.send_keys("FILL IN")

# # find the telephone field
# telephone = driver.find_element(By.XPATH, 'FILL IN')
# # fill in the telephone field
# telephone.send_keys("FILL IN")

# # find the password field
# password = driver.find_element(By.XPATH, 'FILL IN')
# # fill in the password field
# password.send_keys("FILL IN")

# # find the password confirm field
# password_confirm = driver.find_element(By.XPATH, 'FILL IN')
# # fill in the password confirm field
# password_confirm.send_keys("FILL IN")

# # find the desired response to the newsletter subscribe field
# newsletter_subscribe = driver.find_element(By.XPATH, 'FILL IN')
# # click on it
# newsletter_subscribe.click()

# # find the checkbox for agreeing to the terms
# agree = driver.find_element(By.XPATH, 'FILL IN')
# # click on the agree checkbox
# agree.click()

# find the AD Login button
AD_button = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div/div[2]/div[3]/div/ul/li[2]/a/span[2]')
# /html/body/div[2]/div/div/div[2]/div[3]/div/ul/li[2]/a/span[2]

# click on the AD Login button
AD_button.click()


# find the email field
# email = driver.find_element(
#     By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]')
email = driver.find_element(By.NAME, 'loginfmt')
# fill in the email field
email.send_keys(".com.au")
# # find the password field
# password = driver.find_element(By.XPATH, '//*[@id="i0118"]')
# # fill in the password field
# password.send_keys("")

# # find the Sign in button
# signin_button = driver.find_element(
#     By.XPATH, '//*[@id="idSIButton9"]')

# # click on the Sign in button
# signin_button.click()

# scroll down by 200 units to view the lower part of the page
# driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

# pause the program for 5 seconds to view the results
sleep(5)

# close the driver
driver.quit()
