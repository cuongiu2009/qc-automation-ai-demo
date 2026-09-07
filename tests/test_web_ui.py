from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_successful_login_and_add_to_cart(headed_page):
    """
    Test Case 1: Đăng nhập thành công và thêm sản phẩm vào giỏ hàng.
    """
    login_page = LoginPage(headed_page)
    inventory_page = InventoryPage(headed_page)

    # 1. Thực hiện đăng nhập với thông tin tài khoản hợp lệ
    login_page.login("standard_user", "secret_sauce")

    # Xác thực đăng nhập thành công bằng cách kiểm tra URL và Tiêu đề trang Product
    assert "inventory.html" in headed_page.url, "Đăng nhập không thành công, URL không khớp!"
    assert inventory_page.get_title_text() == "Products", "Tiêu đề trang sản phẩm không khớp!"

    # 2. Thêm một sản phẩm cụ thể (ví dụ: Sauce Labs Backpack) vào giỏ hàng
    inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")

    # Xác thực biểu tượng giỏ hàng hiển thị số lượng là 1
    assert inventory_page.get_cart_badge_count() == "1", "Số lượng sản phẩm trong giỏ hàng không chính xác!"


def test_failed_login_locked_out_user(headed_page):
    """
    Test Case 2: Đăng nhập thất bại với tài khoản bị khóa (locked_out_user).
    """
    login_page = LoginPage(headed_page)

    # 1. Thực hiện đăng nhập với tài khoản bị khóa
    login_page.login("locked_out_user", "secret_sauce")

    # Xác thực thông báo lỗi hiển thị đúng nội dung của hệ thống
    error_message = login_page.get_error_message()
    expected_error = "Epic sadface: Sorry, this user has been locked out."
    
    assert expected_error in error_message, f"Thông báo lỗi thực tế không khớp: '{error_message}'"
