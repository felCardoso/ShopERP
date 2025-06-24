import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView,
)

# from PyQt6.QtCore import Qt

from controllers.product_controller import ProductController
from views.ui.product_view_ui import Ui_MainWindow
from models.product import Product


class ProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Instances the class of the generated UI
        self.ui.setupUi(self)  # Config the UI in the window

        self.setWindowTitle("Gerenciar Produtos")

        self.product_controller = ProductController()

        self.ui.pushButtonSave.clicked.connect(self.save_product)
        # self.ui.pushButtonList.clicked.connect(self.load_products)

        self.setup_product_table()
        self.load_products()

    def setup_product_table(self):
        """Configura as colunas da QTableWidget."""
        self.ui.tableWidgetProducts.setColumnCount(5)  # Column Count
        self.ui.tableWidgetProducts.setHorizontalHeaderLabels(
            ["ID", "Name", "Description", "Price", "Stock"]
        )
        # Adjust the columns to fill the avaliable space
        self.ui.tableWidgetProducts.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeMode.ResizeToContents
        )  # ID
        self.ui.tableWidgetProducts.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeMode.Stretch
        )  # Name
        self.ui.tableWidgetProducts.horizontalHeader().setSectionResizeMode(
            2, QHeaderView.ResizeMode.Stretch
        )  # Description
        self.ui.tableWidgetProducts.horizontalHeader().setSectionResizeMode(
            3, QHeaderView.ResizeMode.ResizeToContents
        )  # Price
        self.ui.tableWidgetProducts.horizontalHeader().setSectionResizeMode(
            4, QHeaderView.ResizeMode.ResizeToContents
        )  # Stock
        self.ui.tableWidgetProducts.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )  # Selects the whole line
        self.ui.tableWidgetProducts.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )  # Doesn't allow to edit the table directly

    def save_product(self):
        """Save or updates a product in the database."""

        name = self.ui.lineEditName.text().strip()
        description = self.ui.lineEditDescription.text().strip()
        price_text = self.ui.lineEditPrice.text().strip()
        stock_text = self.ui.lineEditStock.text().strip()

        if not name:
            QMessageBox.warning(self, "Invalid Input", "Product name cannot be blank!")
            return

        try:
            price = float(price_text.replace(",", "."))  # Also accepts comma as float
            stock = int(stock_text)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Price and stock must be valid!")
            return

        product = Product(name=name, description=description, price=price, stock=stock)
        try:
            saved_product = self.product_controller.add_product(product)
            QMessageBox.information(
                self,
                "Success",
                f"Product '{saved_product.name}' saved with ID: {saved_product.id}",
            )
            self.clear_fields()
            self.load_products()  # Reloads the list to show the new product
        except ValueError as ve:  # Specific controller validation error
            QMessageBox.warning(self, "Validation Error", str(ve))
        except Exception as e:
            QMessageBox.critical(
                self, "Saving Error", f"Could not save the product: {e}"
            )

    def load_products(self):
        """Loads all the products in the database and shows them in the screen."""
        self.ui.tableWidgetProducts.setRowCount(0)  # Clears the table
        try:
            products = self.product_controller.get_all_products()
            for row_idx, product in enumerate(products):
                self.ui.tableWidgetProducts.insertRow(row_idx)
                self.ui.tableWidgetProducts.setItem(
                    row_idx, 0, QTableWidgetItem(str(product.id))
                )
                self.ui.tableWidgetProducts.setItem(
                    row_idx, 1, QTableWidgetItem(product.name)
                )
                self.ui.tableWidgetProducts.setItem(
                    row_idx, 2, QTableWidgetItem(product.description)
                )
                self.ui.tableWidgetProducts.setItem(
                    row_idx, 3, QTableWidgetItem(f"{product.price:.2f}")
                )
                self.ui.tableWidgetProducts.setItem(
                    row_idx, 4, QTableWidgetItem(str(product.stock))
                )
        except Exception as e:
            QMessageBox.critical(
                self, "Loading Error", f"Could not load the products table: {e}"
            )

    def clear_fields(self):
        """Clears the form input fields."""
        self.ui.lineEditName.clear()
        self.ui.lineEditDescription.clear()
        self.ui.lineEditPrice.clear()
        self.ui.lineEditStock.clear()


# Screen Test
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductWindow()
    window.show()
    sys.exit(app.exec())
