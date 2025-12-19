"""
Configuration file with URL and base settings
"""


class Config:
    # API URL
    PETSTORE_BASE_URL = "https://petstore.swagger.io/v2"

    # UI URL
    SAUCEDEMO_BASE_URL = "https://www.saucedem.com"

    # Timeouts
    DEFAULT_TIMEOUT = 30000
    API_TIMEOUT = 10

    # Playwright settings
    HEADLESS = False
    BROWSER = "chromium"
    VIEWPORT = {"width": 1920, "height": 1080}

    # Test data
    SAUCEDEMO_USERS = {
        "standard": "standard_user",
        "locked": "locked_out_user",
        "problem": "problem_user",
        "performance": "performance_glitch_user",
    }
    SAUCEDEMO_PASSWORD = "secret_sauce"
