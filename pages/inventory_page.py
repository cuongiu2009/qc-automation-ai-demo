from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_product_to_cart_by_name(self, product_name: str):
        # Định dạng tên sản phẩm theo chuẩn data-test attribute (ví dụ: "Sauce Labs Backpack" -> "add-to-cart-sauce-labs-backpack")
        formatted_name = product_name.lower().replace(" ", "-")
        locator_str = f'[data-test="add-to-cart-{formatted_name}"]'
        self.page.locator(locator_str).click()

    def get_cart_badge_count(self) -> str:
        if self.cart_badge.is_visible():
            return self.cart_badge.inner_text()
        return "0"

    def get_title_text(self) -> str:
        return self.title.inner_text()
