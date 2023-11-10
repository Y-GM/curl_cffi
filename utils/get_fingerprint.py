import sys
import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--ignore-certificate-errors")

# wait 2 seconds for the container to be started
print("connecting to selenium docker container")
while True:
    try:
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options,
        )
        break
    except Exception:
        time.sleep(1)

print("going to fingerprint target")
version = sys.argv[1]

driver.get("https://tls.peet.ws/api/all")

with open(f"fingerprints/ja3-{version}.json", "w") as f:
    content = driver.find_element("tag name", "pre").text
    f.write(content)

driver.get("https://tls.browserleaks.com/json")

with open(f"fingerprints/ja3n-{version}.json", "w") as f:
    content = driver.find_element("tag name", "pre").text
    f.write(content)

driver.close()
driver.quit()
