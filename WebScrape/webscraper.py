"""
Dependencies:
    pip install Pillow
    pip install selenium
    pip install requests
    pip install webdriver-manager
    
manually downloading a chrome webdriver is not required. webdriver-manager will take care of it

Scrapes slightly less than 100 images/minute

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import os

wd = webdriver.Chrome()
wd.implicitly_wait(2)

def get_images_from_google(url, wd, max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            load_more = wd.find_element(By.CLASS_NAME, "LZ4I")
            load_more.click()
            print("Loading more images")
        except:
            return
        
    wd.get(url)
    
    image_urls = set()
    skips = 0
    img_counter = 0;
    failure_counter = 0;
    
    while len(image_urls) + skips < max_images:
        if failure_counter > 30:
            print("Critical failure. Scraped", len(image_urls), "images")
            break
        
        if img_counter >= 22:
            scroll_down(wd)
            img_counter = 0
        else:
            img_counter += 1
        
        thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")
        if len(thumbnails) == 0:
            failure_counter += 1
            print("Failure counter:", failure_counter)
        for img in thumbnails[len(image_urls) + skips:max_images]:
            try:
                img.click()
            except Exception as e:
                print("Scrape fail -", e)
                max_images += 1
                skips += 1
                failure_counter += 1
                print("Failure counter:", failure_counter)
                continue
            
            try:
                images = wd.find_elements(By.CSS_SELECTOR, "img[class='sFlh5c pT0Scc iPVvYb']")
            except Exception as e:
                print("Url find fail -", e)
                continue
            for image in images:
                if image.get_attribute("src") in image_urls:
                    max_images += 1
                    skips += 1
                    print("Duplicate image")
                    break
                
                if image.get_attribute("src") and "http" in image.get_attribute("src"):
                    image_urls.add(image.get_attribute("src"))
                    print("Found image ", len(image_urls))
                    failure_counter = 0;
                    
    return image_urls
    

def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name
        
        with open(file_path, "wb") as f:
            image.save(f, "JPEG")
            
        print("Saved", file_name)
        return True
    except Exception as e:
        print("Failed -", e)
        return False

search_url = "https://www.google.com/search?q=city+skyline+wallpaper&tbm=isch&ved=2ahUKEwjbjaqO2qOCAxVpLd4AHfRmABEQ2-cCegQIABAA&oq=city+skyline+wallpaper&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBAgAEB4yBggAEAUQHjIGCAAQBRAeOgcIABCKBRBDOgYIABAHEB46BAgjECdQtCBYsi9g2jFoAHAAeACAAVuIAZsFkgECMTOYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=nb1CZZvLFuna-LYP9M2BiAE&bih=695&biw=1519&hl=en"
urls = get_images_from_google(search_url, wd, 10)
print("Attempting to save", len(urls), "images")
num_failed = 0

try:
    os.mkdir("imgs")
except:
    print("Directory imgs/ already created")
for i, url in enumerate(urls):
    if not download_image("imgs/", url, str(i) + ".png"):
        num_failed += 1
        
print("Failed to save", num_failed, "images")
#wd.quit()