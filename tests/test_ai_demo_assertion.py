import pytest

@pytest.mark.ai_demo
def test_simulated_assertion_failure_for_ai_analysis(headed_page):
    """
    Test case cố tình gây lỗi AssertionError (sai title) để trigger AI analysis.
    """
    # Lấy title trang và assert sai để kích hoạt lỗi
    title = headed_page.title()
    assert title == "Wrong Page Title", f"Expected 'Wrong Page Title', but got '{title}'"
