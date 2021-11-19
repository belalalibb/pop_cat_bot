from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options = webdriver.ChromeOptions()
options.headless = False
#options.add_argument(r"--user-data-dir=C:\Program Files (x86)\Google\Chrome\Application\Google\Chrome\User Data\Profile {#}/")
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-minimize")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#=======================================
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--window-size=1920,1080")
#options.add_argument("--start-maximized")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
