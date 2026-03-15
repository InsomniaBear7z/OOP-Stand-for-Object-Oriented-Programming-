Chapter 1
import time

total_seconds = time.time()

seconds_in_a_day = 24 * 60 * 60
seconds_in_an_hour = 60 * 60
seconds_in_a_minute = 60


days = total_seconds // seconds_in_a_day

remainder = total_seconds % seconds_in_a_day

hours = remainder // seconds_in_an_hour

remainder = remainder % seconds_in_an_hour

minutes = remainder // seconds_in_a_minute

seconds = remainder % seconds_in_a_minute

print(f"Tổng số giây từ the Epoch: {total_seconds}")
print(f"Số ngày đã trôi qua: {int(days)} ngày")
print(f"Thời gian hiện tại (theo giờ GMT): {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")
