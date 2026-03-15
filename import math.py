Chapter 2
import math

radius = 5
volume = (4/3) * math.pi * radius**3

print("--- Kết quả Bài 1 ---")
print(f"Thể tích hình cầu bán kính {radius} là: {volume:.2f}")
print()


cover_price = 24.95
discount_rate = 0.40
num_copies = 60

discounted_price = cover_price * (1 - discount_rate)

shipping_cost = 3.00 + (num_copies - 1) * 0.75

total_wholesale_cost = (discounted_price * num_copies) + shipping_cost

print("--- Kết quả Bài 2 ---")
print(f"Tổng chi phí cho {num_copies} cuốn sách là: ${total_wholesale_cost:.2f}")
print()


start_hour = 6
start_minute = 52

easy_pace_sec = (8 * 60) + 15
tempo_pace_sec = (7 * 60) + 12

total_run_sec = (easy_pace_sec * 2) + (tempo_pace_sec * 3)

run_minutes = total_run_sec // 60
run_seconds = total_run_sec % 60

arrival_minute_total = start_minute + run_minutes
arrival_hour = start_hour + (arrival_minute_total // 60)
arrival_minute = arrival_minute_total % 60

print("--- Kết quả Bài 3 ---")
print(f"Bạn sẽ về đến nhà lúc: {arrival_hour}:{arrival_minute:02d}:{run_seconds:02d} AM")
