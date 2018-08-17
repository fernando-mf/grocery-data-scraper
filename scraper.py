from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.iga.net/en/online_grocery/")

input("Press any key to start script ...")

# Start scraper
# Take categories
categories = driver.find_elements_by_class_name("js-ga-category")
print("Categories : ")
for cat in categories:
    print("\t" + cat.text)

# Access single category
# TODO: Iterate through all the elements
# Take items
items = driver.find_elements_by_class_name("js-ga-productname")

# Work on item
# TODO: Iterate through products
productBrand = driver.find_element_by_class_name("product-detail__brand")
productName = driver.find_element_by_class_name("product-detail__name")
productWeight = driver.find_element_by_class_name("item-product__info--product-detail")
productPrice = driver.find_element_by_class_name("product-detail__price--sale")
productPricePerWeight = driver.find_element_by_class_name("product-detail__info")
productMediumImage = driver.find_element_by_id("body_0_main_1_ProductImage")
imageSrc = productMediumImage.get_attribute("src") # TODO: Get small and large image
backButton = driver.find_element_by_id("body_0_main_1_BackToSearch")
backButton.click()