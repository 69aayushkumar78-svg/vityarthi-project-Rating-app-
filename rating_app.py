import json
import os

DATA_FILE = "app_data.json"

# --- DATA MANAGEMENT ---
def load_data():
    if not os.path.exists(DATA_FILE):
        print("\n=============================================")
        print(" FIRST-TIME SETUP: SETUP ADMIN CREDENTIALS  ")
        print("=============================================")
        admin_id = input("Create Admin ID: ").strip()
        while not admin_id:
            admin_id = input("Admin ID cannot be empty. Create Admin ID: ").strip()
            
        admin_pass = input("Create Admin Password: ").strip()
        while not admin_pass:
            admin_pass = input("Password cannot be empty. Create Admin Password: ").strip()

        default_data = {
            "admin": {"id": admin_id, "password": admin_pass},
            "products": []
        }
        save_data(default_data)
        print("Admin setup complete!\n")
        return default_data

    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- RATING HELPER ---
def get_rating(prompt):
    while True:
        try:
            score = float(input(f"  {prompt} (1 to 5 stars): "))
            if 1 <= score <= 5:
                return score
            print("  Please enter a number between 1 and 5.")
        except ValueError:
            print("  Invalid input! Please enter a number.")

# --- USER WORKFLOW ---
def user_flow(data):
    print("\n--- USER LOGIN ---")
    name = input("Enter your Name: ").strip()
    email = input("Enter your Email: ").strip()

    if not name or not email:
        print("Name and email cannot be empty!")
        return

    while True:
        products = data.get("products", [])
        if not products:
            print("\nNo products available to rate yet. Check back later!")
            break

        print(f"\nWelcome, {name}!")
        print("Available Products:")
        for idx, prod in enumerate(products, 1):
            print(f"  {idx}. {prod['name']}")
        print("  0. Back to Main Menu")

        try:
            choice = int(input("\nSelect a product number to rate: "))
            if choice == 0:
                break
            if 1 <= choice <= len(products):
                target_product = products[choice - 1]
                print(f"\nRating for: {target_product['name']}")

                rating_data = {
                    "user_name": name,
                    "user_email": email,
                    "worth_of_money": get_rating("Worth of Money"),
                    "quality": get_rating("Product Quality"),
                    "support": get_rating("Customer Support")
                }

                target_product["ratings"].append(rating_data)
                save_data(data)
                print(f"Thank you, {name}! Your rating has been submitted successfully.")
            else:
                print("Invalid product selection.")
        except ValueError:
            print("Please enter a valid number.")

# --- ADMIN WORKFLOW ---
def admin_flow(data):
    print("\n--- ADMIN LOGIN ---")
    admin_id = input("Admin ID: ").strip()
    admin_pass = input("Admin Password: ").strip()

    if admin_id != data["admin"]["id"] or admin_pass != data["admin"]["password"]:
        print("Invalid Admin ID or Password!")
        return

    while True:
        print("\n--- ADMIN DASHBOARD ---")
        print("1. Add New Product")
        print("2. View All Products & Ratings")
        print("3. Change Admin Credentials")
        print("4. Logout")
        
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            p_name = input("Enter new product name: ").strip()
            if p_name:
                data["products"].append({
                    "name": p_name,
                    "ratings": []
                })
                save_data(data)
                print(f"Product '{p_name}' added successfully!")
            else:
                print("Product name cannot be empty.")

        elif choice == "2":
            products = data.get("products", [])
            if not products:
                print("\nNo products registered yet.")
                continue

            print("\n================ ALL PRODUCTS ================")
            for prod in products:
                ratings = prod["ratings"]
                count = len(ratings)
                print(f"\nProduct Name: {prod['name']}")
                print(f"Total Reviews: {count}")

                if count > 0:
                    avg_money = sum(r["worth_of_money"] for r in ratings) / count
                    avg_quality = sum(r["quality"] for r in ratings) / count
                    avg_support = sum(r["support"] for r in ratings) / count
                    
                    print(f"  - Avg Worth of Money: {avg_money:.2f} / 5")
                    print(f"  - Avg Quality:        {avg_quality:.2f} / 5")
                    print(f"  - Avg Support:        {avg_support:.2f} / 5")
                    print("  - Individual Submissions:")
                    for r in ratings:
                        print(f"      * {r['user_name']} ({r['user_email']}) -> "
                              f"Money: {r['worth_of_money']}, Quality: {r['quality']}, Support: {r['support']}")
                else:
                    print("  No ratings submitted yet.")
            print("==============================================")

        elif choice == "3":
            new_id = input("Enter new Admin ID: ").strip()
            new_pass = input("Enter new Admin Password: ").strip()
            if new_id and new_pass:
                data["admin"]["id"] = new_id
                data["admin"]["password"] = new_pass
                save_data(data)
                print("Admin credentials updated successfully!")
            else:
                print("ID and Password cannot be empty.")

        elif choice == "4":
            print("Logged out from Admin.")
            break
        else:
            print("Invalid option. Try again.")

# --- MAIN MENU ---
def main():
    data = load_data()
    
    while True:
        print("\n===============================")
        print("    PRODUCT RATING SYSTEM      ")
        print("===============================")
        print("1. User Login (Rate Products)")
        print("2. Admin Login")
        print("3. Exit Program")

        choice = input("Select Portal (1-3): ").strip()

        if choice == "1":
            user_flow(data)
        elif choice == "2":
            admin_flow(data)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()