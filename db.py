import sqlite3


# Bazaga ulanish funksiyasi
def get_db_connection():
    conn = sqlite3.connect('products.db')  # Fayl nomi - mahsulotlar.db
    conn.row_factory = sqlite3.Row  # Natijalarni kamroq formatda olish
    return conn

# Mahsulot qo'shish funksiyasi
def add_product(name: str, price: float):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    conn.commit()  # O'zgarishlarni saqlaymiz
    conn.close()
    print(f"Mahsulot '{name}' muvaffaqiyatli qo'shildi!")

# Mahsulot o'chirish funksiyasi
def delete_product(product_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM products WHERE id = ?"
    cursor.execute(query, (product_id,))
    conn.commit()  # O'zgarishlarni saqlaymiz
    conn.close()
    print(f"Mahsulot ID {product_id} muvaffaqiyatli o'chirildi!")

# Barcha mahsulotlarni olish funksiyasi
import sqlite3

def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM products")
    products = cursor.fetchall()
    conn.close()
    return products


def clear_cache():
    # Keshni tozalash logikasi
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Masalan, mahsulotlar jadvalidagi barcha ma'lumotlarni o'chirish
    cursor.execute("DELETE FROM products")
    
    conn.commit()
    conn.close()
