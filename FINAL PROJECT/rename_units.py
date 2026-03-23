"""One-time database cleanup script.

I used this when I wanted to rename old categories like "Unit 1" -> "Chap 1".
Not part of the normal app flow, just a helper.
"""

import sqlite3

# Configuration
DB_NAME = 'quiz.db'

def rename_categories():
    # Connect to the database
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    print("Renaming 'Unit' to 'Chap' in categories...")
    
    # 1. Update the categories
    # This replaces "Unit" with "Chap" anywhere in the category name
    # e.g., "Unit 1" becomes "Chap 1"
    c.execute("UPDATE questions SET category = REPLACE(category, 'Unit', 'Chap') WHERE category LIKE 'Unit %'")
    
    rows_affected = c.rowcount
    conn.commit()
    
    print(f"Success! Updated {rows_affected} questions.")
    
    # 2. Verify the changes
    print("\nNew Category List:")
    c.execute("SELECT DISTINCT category FROM questions ORDER BY category")
    categories = c.fetchall()
    for row in categories:
        print(f"- {row[0]}")
        
    conn.close()

if __name__ == '__main__':
    rename_categories()
