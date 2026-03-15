total_seconds = 42 * 60 + 42
print(f"1. Tổng số giây trong 42 phút 42 giây là: {total_seconds} giây")

miles = 10 / 1.61
print(f"2. Số dặm trong 10 km là: {miles:.2f} dặm")

seconds_per_mile = total_seconds / miles
pace_minutes = int(seconds_per_mile // 60)
pace_seconds = seconds_per_mile % 60
print(f"3a. Tốc độ trung bình (pace) là: {pace_minutes} phút {pace_seconds:.2f} giây / dặm")

total_hours = total_seconds / 3600
speed_mph = miles / total_hours
print(f"3b. Vận tốc trung bình là: {speed_mph:.2f} dặm/giờ")