from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Set the path to the Microsoft Edge driver
edge_driver_path = 'C:/edgeDriver/msedgedriver.exe'

# Set the path to your user data directory 
user_data_dir = 'C:/Users/Admin/AppData/Local/Microsoft/Edge/User Data' 

# Create a new instance of the Edge driver with the specified user data directory 
options = webdriver.EdgeOptions() 
options.add_argument(f'user-data-dir={user_data_dir}') 
options.add_argument("--remote-allow-origins=*")
options.add_argument("--disable-gpu-sandbox")
options.add_argument("--no-sandbox")

# Create a new instance of the Edge driver
driver = webdriver.Edge(executable_path=edge_driver_path,options=options) 

# Minimize the window
driver.minimize_window()

# Navigate to the Bing search page
driver.get('https://www.bing.com')

# Sleeping for 2 seconds
time.sleep(2)

# List of possible search queries
search_queries = ['apple', 'banana', 'cat', 'dog', 'elephant', 'fish', 'grapefruit', 'horse', 
                  'guana', 'jaguar', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 
                  'quince', 'raspberry', 'strawberry', 'tangerine', 'umbrella', 'bird', 'vulture', 
                  'watermelon', 'x-ray', 'fish', 'yak', 'zebra','hello','naming',
                  'maharashtra','india','worldmap','bottle','mobile']

# Perform 35 searches
for i in range(35):
    # Find the search box element
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))

    # Clear the search box
    search_box.clear()

    # Enter a unique search query and submit the form
    search_query = search_queries[i]
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'b_content')))
    
    # Wait for some time before the next search
    time.sleep(2)

# Close the browser
driver.quit()