import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def headed_page():
    # Tự động phát hiện môi trường CI để chạy headless
    is_ci = os.environ.get("CI") == "true"
    
    # Khởi tạo Playwright sync API
    with sync_playwright() as p:
        # Nếu ở CI chạy headless, ngược lại chạy headed (cục bộ)
        launch_args = ["--start-maximized"] if not is_ci else []
        browser = p.chromium.launch(headless=is_ci, args=launch_args)
        
        context_args = {"no_viewport": True} if not is_ci else {}
        context = browser.new_context(**context_args)
        page = context.new_page()
        
        # Mở trang web cần test
        page.goto("https://www.saucedemo.com")
        
        yield page
        
        # Đóng sau khi hoàn thành test case
        page.close()
        context.close()
        browser.close()
