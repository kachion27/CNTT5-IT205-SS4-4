lucky_number = 89
true_turn = False

for turn in range(1, 6):
    number_choice = int(input(f"Lượt đoán {turn} - Nhập số của bạn: "))
    
    if number_choice == lucky_number:
        print("=> Chúc mừng! Bạn đã đoán chính xác mã số may mắn!")
        true_turn = True
    elif number_choice < lucky_number:
        print("=> Gợi ý: Số của bạn nhỏ hơn mã số may mắn!")
    else:
        print("=> Gợi ý: Số của bạn lớn hơn mã số may mắn!")

print("--- TRÒ CHƠI KẾT THÚC ---")

if not true_turn:
    print(f"Bạn đã hết lượt và chúc may mắn lần sau. (Mã số đúng là: {lucky_number})")