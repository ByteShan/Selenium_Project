import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def click_element(element):
    element.click()
    time.sleep(2)

def click_calendar(date):
    date.click()

def select_dropdown_option(driver, by, value, option):
    dropdown = Select(driver.find_element(by, value))
    dropdown.select_by_visible_text(option)
    time.sleep(2)

def take_screenshot(driver, filename):
    driver.save_screenshot(filename)

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the URL and maximize the window
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()

    # Navigate to iPhone product
    click_element(driver.find_element(By.XPATH, "//a[normalize-space()='Phones & PDAs']"))
    click_element(driver.find_element(By.XPATH, "//a[normalize-space()='iPhone']"))

    # View product images
    click_element(driver.find_element(By.XPATH, "//ul[@class='thumbnails']/li[1]"))
    next_pic_button = driver.find_element(By.XPATH, "//button[@title='Next (Right arrow key)']")
    
    for _ in range(5):
        click_element(next_pic_button)

    # Take a screenshot
    take_screenshot(driver, f"screenshot#{random.randint(0, 101)}.png")

    # Close the picture slide
    click_element(driver.find_element(By.XPATH, "//button[normalize-space()='×']"))

    # Update product quantity and add to cart
    quantity = driver.find_element(By.ID, "input-quantity")
    quantity.clear()
    quantity.send_keys("2")

    click_element(driver.find_element(By.XPATH, "//button[@id='button-cart']"))

    # Navigate to HP product
    laptop = driver.find_element(By.XPATH, "//a[normalize-space()='Laptops & Notebooks']")
    ActionChains(driver).move_to_element(laptop).perform()

    click_element(driver.find_element(By.XPATH, "//a[normalize-space()='Show AllLaptops & Notebooks']"))
    click_element(driver.find_element(By.XPATH, "//a[normalize-space()='HP LP3065']"))

    # Scroll to make the 'Add to Cart' button clickable
    review = driver.find_element(By.XPATH, "//a[normalize-space()='Write a review']")
    review.location_once_scrolled_into_view
    time.sleep(1)

    # Choose a date from the calendar
    click_calendar(driver.find_element(By.XPATH, "//i[@class='fa fa-calendar']"))
    right_click = driver.find_element(By.XPATH, "//div[@class='datepicker-days']//th[@class='next'][contains(text(),'›')]")

    while not driver.find_element(By.XPATH, "//th[@class='picker-switch']").text == "December 2023":
        click_calendar(right_click)

    click_element(driver.find_element(By.XPATH, "//td[normalize-space()='31']"))
    click_element(driver.find_element(By.XPATH, "//button[@id='button-cart']"))

    # Proceed to checkout
    click_element(driver.find_element(By.ID, "cart-total"))
    click_element(driver.find_element(By.XPATH, "//strong[normalize-space()='Checkout']"))

    # Remove an item from the cart
    click_element(driver.find_element(By.XPATH, "//tbody/tr[1]/td[4]/div[1]/span[1]/button[2]/i[1]"))

    # Continue to checkout
    checkout_button = driver.find_element(By.XPATH, "//a[@class='btn btn-primary']")
    checkout_button.location_once_scrolled_into_view
    click_element(checkout_button)

    # Guest account
    click_element(driver.find_element(By.XPATH, "//input[@value='guest']"))
    click_element(driver.find_element(By.ID, "button-account"))

    # Scroll to get a full view
    scroll = driver.find_element(By.XPATH, "//a[normalize-space()='Step 2: Billing Details']")
    scroll.location_once_scrolled_into_view
    time.sleep(1)

    # Fill out personal details
    driver.find_element(By.ID, "input-payment-firstname").send_keys("Shan")
    driver.find_element(By.ID, "input-payment-lastname").send_keys("VSK")
    driver.find_element(By.ID, "input-payment-email").send_keys("Shan@Selenium.com")
    driver.find_element(By.ID, "input-payment-telephone").send_keys("9842130820")
    driver.find_element(By.ID, "input-payment-address-1").send_keys("99, Avvaiyar Street")
    driver.find_element(By.ID, "input-payment-city").send_keys("Chennai")
    driver.find_element(By.ID, "input-payment-postcode").send_keys("600 001")

    # Select country and region
    select_dropdown_option(driver, By.ID, "input-payment-country", "India")
    select_dropdown_option(driver, By.ID, "input-payment-zone", "Tamil Nadu")

    # Continue to proceed to step 3
    click_element(driver.find_element(By.XPATH, "//input[@id='button-guest']"))

    # Continue through steps 4 and 5
    click_element(driver.find_element(By.XPATH, "//input[@id='button-shipping-method']"))
    click_element(driver.find_element(By.XPATH, "//input[@name='agree']"))
    click_element(driver.find_element(By.XPATH, "//input[@id='button-payment-method']"))

    # Get the final price and print it in the console
    total_price = driver.find_element(By.XPATH, "//table[@class='table table-bordered table-hover']/tfoot/tr[3]/td[2]")
    print(f"The total cart value is: {total_price.text}")

    # Confirm the order
    click_element(driver.find_element(By.ID, "button-confirm"))

    # Print confirmation text
    success_msg = driver.find_element(By.XPATH, "//h1[normalize-space()='Your order has been placed!']")
    print(success_msg.text)

    # Print the final message
    print("The project has been successfully completed! :-)")

finally:
    # Close the browser
    driver.quit()