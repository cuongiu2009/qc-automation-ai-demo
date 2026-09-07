import pytest

@pytest.mark.ai_demo
def test_simulated_ui_failure_for_ai_analysis(headed_page):
    """
    Test case cố tình gây lỗi Timeout để trigger AI analysis.
    Sử dụng fixture 'headed_page' để dùng cấu hình trình duyệt chuẩn của dự án.
    """
    # Cố tình tìm locator không tồn tại
    headed_page.locator("#invalid-login-btn-id").click(timeout=3000)
