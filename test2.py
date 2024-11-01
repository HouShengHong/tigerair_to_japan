from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import resource


a = webdriver.Chrome()

# del a

mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

g = globals()

print(mem_usage,len(g),g)















