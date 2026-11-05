# shopping cart 클래스 생성
# 상품 목록 저장 기능
# 메서드 
# - 장바구니 담기
# - 장바구니 빼기
# - 상품 목록 조회

class ShoppingCart:
    def __init__(self):
        self.bucket = []
    def add_item(self, item):
        self.bucket.append(item)
    def remove_item(self, item):
        self.bucket.remove(item)
    def show_items(self):
        return self.bucket


# 상품 클래스
# 속성 
# - 제품명
# - 가격

class Item:
    def __init__(self, name, price ):
        self.name = name
        self.price = price

# 쇼핑 카트 생성
cart = ShoppingCart()

# 상품 3개 생성
item_a = Item("초코파이", 12000)
item_b = Item("귤", 9000)
item_c = Item("사과", 6000)

# 상품 1개 장바구니 담기
cart.add_item(item_a)
# 상품 1개 장바구니 담기
cart.add_item(item_b)
# 상품 1개 장바구니 담기
cart.add_item(item_c)
# 상품 1개 장바구니에서 빼기
cart.add_item(item_b)
# 장바구니에 담긴 상품 목록 조회
for item in cart.show_items():
    print(item.name, item.price)
