from PyQt6 import QtWidgets, uic

class POSApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)  

        self.product_dropdown = self.findChild(QtWidgets.QComboBox, "productDropdown")
        self.quantity_input = self.findChild(QtWidgets.QSpinBox, "quantityInput")
        self.discount_dropdown = self.findChild(QtWidgets.QComboBox, "discountDropdown")
        self.add_to_cart_button = self.findChild(QtWidgets.QPushButton, "addToCartButton")
        self.clear_button = self.findChild(QtWidgets.QPushButton, "clearButton")
        self.cart_display = self.findChild(QtWidgets.QTextEdit, "cartDisplay")
        self.total_price_label = self.findChild(QtWidgets.QLabel, "totalPriceLabel")

        self.products = {
            "Bimoli (Rp 20.000)": 20000,
            "Beras 5 Kg (Rp 75.000)": 75000,
            "Kecap ABC (Rp 7000)": 7000,
            "Saos Saset (Rp 2500)": 2500,
        }

        self.product_dropdown.addItems(self.products.keys())
        self.discount_dropdown.addItems(["0%", "5%", "10%", "15%"])

        self.add_to_cart_button.clicked.connect(self.add_to_cart)
        self.clear_button.clicked.connect(self.clear_form)

        self.cart = []

    def add_to_cart(self):
        product = self.product_dropdown.currentText()
        quantity = self.quantity_input.value()
        discount = int(self.discount_dropdown.currentText().strip('%'))
        price = self.products[product] * quantity
        discounted_price = price - (price * discount / 100)
        
        self.cart.append((product, quantity, discounted_price))
        self.update_cart_display()
    
    def update_cart_display(self):
        self.cart_display.clear()
        total = 0
        for product, quantity, price in self.cart:
            self.cart_display.append(f"{product} x{quantity}: Rp {price:,.0f}")
            total += price
        self.total_price_label.setText(f"Total: Rp {total:,.0f}")
    
    def clear_form(self):
        self.product_dropdown.setCurrentIndex(0)
        self.quantity_input.setValue(1)
        self.discount_dropdown.setCurrentIndex(0)
        self.cart.clear()  
        self.update_cart_display()  


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = POSApp()
    window.show()
    app.exec()
