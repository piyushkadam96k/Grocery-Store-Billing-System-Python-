groceries = {          
    "bananas": 87,   
    "bread": 219,    
    "milk": 113,     
    "eggs": 351,     
    "cheese": 396,  
    "chicken": 528,   
    "rice": 193,     
    "pasta": 157,     
    "tomatoes": 202,
    "apple": 100
}

def billing():
    print("\n===== Welcome to XYZ store =====\n")
    print("\t==== Stock is here ====")
    
    items = list(groceries.keys())
    cart = {}   # to store what user buys
    
    for i, key in enumerate(items, start=1):
        print(f"\t {i}. {key} : {groceries[key]}")
        
    while True:
        user = int(input(f"\nWhich item do you want to buy (enter number): "))
        if 1 <= user <= len(items):
            chosen_item = items[user - 1]  
            price = groceries[chosen_item]
            qty = int(input(f"Enter quantity of {chosen_item}: "))
            
            # add to cart
            if chosen_item in cart:
                cart[chosen_item] += qty
            else:
                cart[chosen_item] = qty
                
            print(f"\n✔ Added {qty} {chosen_item}(s) - {price*qty} total")
        else:
            print("\n❌ Invalid choice, please try again.")
        
        choice = input("\nDo you want to quit? (press 'q' to quit, Enter to continue): ")
        if choice.lower() == 'q':
            print("\n===== Final Bill =====")
            total = 0
            for item, qty in cart.items():
                price = groceries[item]
                cost = price * qty
                total += cost
                print(f"{item} x {qty} = {cost}")
            print("----------------------")
            print(f"Grand Total = {total}")
            print("Thank you for shopping with us! 🛒")
            break

billing()
