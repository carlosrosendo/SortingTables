from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/tables")

# click header to sort
driver.find_element(By.XPATH, "//table[@id='table1']/thead/tr/th/span[text()='Last Name']").click()

# created a list of elements inside the table, iterated over them using for loop
lastName = []
table1 = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr/td[1]")
for element in table1:
    #print(element.text)
    lName = element.text
    lastName.append(lName)
    lastName.append(element.text)

print(lastName)
# created a copy of what was the empty list and gave it a new name
lastName_actual = lastName.copy()

# sort the list we coped
lastName_actual.sort()
print(lastName_actual)

# Validate data gets sorted
assert lastName_actual == lastName

