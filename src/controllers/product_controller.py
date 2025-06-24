from database.db_manager import connect_db
from models.product import Product
import sqlite3


class ProductController:
    def __init__(self):
        pass  # Por enquanto, não precisamos de nada aqui

    def add_product(self, product: Product):
        """Add a new product to the database."""
        conn = connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO products (name, description, price, stock) VALUES (?, ?, ?, ?)",
                (product.name, product.description, product.price, product.stock),
            )
            product.id = cursor.lastrowid  # Pega o ID que foi gerado automaticamente
            conn.commit()
            return product
        except sqlite3.IntegrityError:
            # Caso o nome do produto já exista (UNIQUE constraint)
            raise ValueError(f"Produto com o nome '{product.name}' já existe.")
        except Exception as e:
            conn.rollback()
            raise Exception(f"Erro ao adicionar produto: {e}")
        finally:
            conn.close()

    def get_all_products(self):
        """Return a list with all products in the database."""
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, description, price, stock FROM products")
        products_data = cursor.fetchall()
        conn.close()
        return [
            Product(
                id=row[0], name=row[1], description=row[2], price=row[3], stock=row[4]
            )
            for row in products_data
        ]

    def get_product_by_id(self, product_id: int):
        """Return a product by its ID."""
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, name, description, price, stock FROM products WHERE id=?",
            (product_id,),
        )
        product_data = cursor.fetchone()
        conn.close()
        if product_data:
            return Product(
                id=product_data[0],
                name=product_data[1],
                description=product_data[2],
                price=product_data[3],
                stock=product_data[4],
            )
        return None

    def update_product(self, product: Product):
        """Update all data from an existing product."""
        if product.id is None:
            raise ValueError("Product ID is needed to update.")

        conn = connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE products SET name=?, description=?, price=?, stock=? WHERE id=?",
                (
                    product.name,
                    product.description,
                    product.price,
                    product.stock,
                    product.id,
                ),
            )
            conn.commit()
            return cursor.rowcount > 0  # Return True if any line was updated
        except sqlite3.IntegrityError:
            raise ValueError(f"Product named '{product.name}' already exists.")
        except Exception as e:
            conn.rollback()
            raise Exception(f"Product update error: {e}")
        finally:
            conn.close()

    def delete_product(self, product_id: int):
        """Delete a product by its ID."""
        conn = connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
            conn.commit()
            return cursor.rowcount > 0  # Return True if any line was deleted
        except Exception as e:
            conn.rollback()
            raise Exception(f"Error deleting product: {e}")
        finally:
            conn.close()
