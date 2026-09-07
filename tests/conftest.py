import os
import pytest
from playwright.sync_api import sync_playwright
from utils.ai_analyzer import analyze_failure_log

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

# Tự động kích hoạt AI Analysis khi test thất bại
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        if os.environ.get("GEMINI_API_KEY"):
            print("\n\n" + "="*20 + " AI FAILURE ANALYSIS " + "="*20)
            analysis = analyze_failure_log(report.longreprtext)
            print(analysis)
            print("="*60 + "\n")

