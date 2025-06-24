import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from database.db_manager import create_tables
from views.product_view import ProductWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ShopERP - Main Menu")
        self.setGeometry(100, 100, 500, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Botão para abrir a tela de produtos
        btn_products = QPushButton("Manage Products")
        btn_products.clicked.connect(self.open_product_window)
        layout.addWidget(btn_products)

    def open_product_window(self):
        """Opens the product management window."""
        self.product_window = ProductWindow()  # Create a new product window instance
        self.product_window.show()  # Shows the window


if __name__ == "__main__":
    create_tables()  # Grants the table exists before starting the app
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
