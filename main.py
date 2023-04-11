def calculate_price(num_dozen):
    """Calculate the price based on the number of dozen eggs purchased."""
    
    if num_dozen < 0:
        raise ValueError("โปรดป้อนจำนวนโหลที่มากกว่า 0")
    if not isinstance(num_dozen, int):
        raise ValueError("โปรดป้อนจำนวนโหลที่เป็นตัวเลข")
    
    price_per_dozen = 4
    if num_dozen < 5:
        price = num_dozen * price_per_dozen
    else:
        price_per_dozen_discounted = 3
        price = num_dozen * price_per_dozen_discounted
    return round(price, 2)

if __name__ == "__main__":
    while True:
        num_dozen_input = input("ป้อนจำนวนไข่ที่ User ต้องการ (จำนวนไข่/ต่อฟอง): ")
        try:
            num_dozen = int(num_dozen_input)
            if num_dozen <= 0:
                print("โปรดป้อนจำนวนโหลที่มากกว่า 0")
                continue
            else:
                break
        except ValueError:
            print("โปรดป้อนจำนวนโหลที่เป็นตัวเลข")
            continue
        

    # Call the calculate_price function and print the result
    price = calculate_price(num_dozen)
    print("ราคาที่ต้องจ่าย: $", price, "บาท")