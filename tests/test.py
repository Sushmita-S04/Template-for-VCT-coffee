import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()
# or specify the host and port if necessary
# Make sure the ChromeDriver executable is in your system PATH

# Test Case 1: Verify Homepage


def test_homepage():
    driver.get("http://localhost:5000")  # Replace with your website URL

    # Assert the page title
    assert driver.title == "Welcome"

    # Assert the presence of the logo
    logo = driver.find_element(By.ID, "logo")
    assert logo.is_displayed()

    # Assert the presence of the sign-in button
    sign_in_button = driver.find_element(By.ID, "signInButton")
    assert sign_in_button.is_displayed()

    # Assert the presence of the cart icon
    cart_icon = driver.find_element(By.ID, "cartIcon")
    assert cart_icon.is_displayed()

    # Assert the presence of the category section
    category_section = driver.find_element(By.CLASS_NAME, "displayCategory")
    assert category_section.is_displayed()

    # Assert the number of items
    items = driver.find_elements(By.ID, "productName")
    assert len(items) > 0

# Test Case 2: Verify Registration Form


def test_registration_form():
    # Replace with your registration URL
    driver.get("http://localhost:5000/registerationForm")

    # Assert the page title
    assert driver.title == "Registration Form"

    # Find registration form elements
    email_input = driver.find_element(By.NAME, "email")
    password_input = driver.find_element(By.NAME, "password")
    confirm_password_input = driver.find_element(By.NAME, "cpassword")
    first_name_input = driver.find_element(By.NAME, "firstName")
    last_name_input = driver.find_element(By.NAME, "lastName")
    address1_input = driver.find_element(By.NAME, "address1")
    address2_input = driver.find_element(By.NAME, "address2")
    zipcode_input = driver.find_element(By.NAME, "zipcode")
    city_input = driver.find_element(By.NAME, "city")
    state_input = driver.find_element(By.NAME, "state")
    country_input = driver.find_element(By.NAME, "country")
    phone_input = driver.find_element(By.NAME, "phone")
    register_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")

    # Assert the presence of registration form elements
    assert email_input.is_displayed()
    assert password_input.is_displayed()
    assert confirm_password_input.is_displayed()
    assert first_name_input.is_displayed()
    assert last_name_input.is_displayed()
    assert address1_input.is_displayed()
    assert address2_input.is_displayed()
    assert zipcode_input.is_displayed()
    assert city_input.is_displayed()
    assert state_input.is_displayed()
    assert country_input.is_displayed()
    assert phone_input.is_displayed()
    assert register_button.is_displayed()

    # Fill in the registration form
    email_input.send_keys("test@example.com")
    password_input.send_keys("password")
    confirm_password_input.send_keys("password")
    first_name_input.send_keys("John")
    last_name_input.send_keys("Doe")
    address1_input.send_keys("123 Main St")
    address2_input.send_keys("Apt 4B")
    zipcode_input.send_keys("12345")
    city_input.send_keys("New York")
    state_input.send_keys("NY")
    country_input.send_keys("USA")
    phone_input.send_keys("555-1234")

    # Submit the registration form
    register_button.click()

    # Add assertions for successful registration or any error messages that may appear

# Test Case 3: Verify Product Description Page


def test_product_description_page():
    # Replace with your product description URL
    driver.get("http://localhost:5000/productDescription?productId=2")

    # Assert the page title
    assert driver.title == "Product Description"

    # Assert the presence of product information elements
    product_name = driver.find_element(By.ID, "productName")
    assert product_name.is_displayed()

    product_image = driver.find_element(By.ID, "productImage")
    assert product_image.is_displayed()

    description_table = driver.find_element(By.ID, "descriptionTable")
    assert description_table.is_displayed()

    add_to_cart_button = driver.find_element(
        By.CSS_SELECTOR, "#addToCart button")
    assert add_to_cart_button.is_displayed()

    # Add additional assertions as needed


# Perform the tests
try:
    test_homepage()
    print("Test Case 1: Homepage - PASSED")
except AssertionError as e:
    print("Test Case 1: Homepage - FAILED")
    print(str(e))

time.sleep(10)  # Delay for 10 seconds

try:
    test_registration_form()
    print("Test Case 2: Registration Form - PASSED")
except AssertionError as e:
    print("Test Case 2: Registration Form - FAILED")
    print(str(e))

time.sleep(10)  # Delay for 10 seconds

try:
    test_product_description_page()
    print("Test Case 3: Product Description Page - PASSED")
except AssertionError as e:
    print("Test Case 3: Product Description Page - FAILED")
    print(str(e))

time.sleep(10)  # Delay for 10 seconds

# Quit the WebDriver
driver.quit()
