"""
Configuration file for test settings
"""

import os

class Config:
    # Base URL of the application under test
    BASE_URL = os.getenv("BASE_URL", "https://bpholter.stage.bio-beat.cloud")
    
    # Browser settings
    BROWSER = "chromium"  # Options: chromium, firefox, webkit
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"  # Set to True for headless mode
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))  # Slow down operations by specified milliseconds
    
    # Timeouts (in milliseconds)
    DEFAULT_TIMEOUT = 30000
    NAVIGATION_TIMEOUT = 30000
    
    # Screenshot settings
    SCREENSHOT_ON_FAILURE = True
    SCREENSHOT_PATH = "screenshots"
    
    # Test data
    VALID_USERNAME = os.getenv("VALID_USERNAME", "validuser@example.com")
    VALID_PASSWORD = os.getenv("VALID_PASSWORD", "ValidPass123!")
    
    # Video recording
    RECORD_VIDEO = False
    VIDEO_PATH = "videos"
