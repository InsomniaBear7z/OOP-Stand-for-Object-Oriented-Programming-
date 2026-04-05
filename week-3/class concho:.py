class concho:
    def __init__(self, ten, mau_sac, giong, cam_xuc="Bình thường"):

        self.ten = ten
        self.mau_sac = mau_sac
        self.giong = giong
        self.cam_xuc = cam_xuc

    def sua(self):
        print(f"[{self.ten}] đang sủa: Gâu gâu gâu!")

    def vay_duoi(self):
        self.cam_xuc = "Rất vui vẻ"
        print(f"[{self.ten}] đang vẫy đuôi vì {self.cam_xuc}.")

    def an(self, thuc_an):
        print(f"[{self.ten}] đang ăn {thuc_an} nhồm nhoàm.")
        
    def chay(self):
        print(f"[{self.ten}] đang chạy tung tăng ngoài sân.")


class oto:
    def __init__(self, hang, kich_thuoc, mau, gia):
        self.hang = hang
        self.kich_thuoc = kich_thuoc
        self.mau = mau
        self.gia = gia
        self.toc_do = 0  


    def tang_toc(self, muc_tang):
        self.toc_do += muc_tang
        print(f"[Xe {self.hang}] Tăng tốc lên {self.toc_do} km/h.")

    def giam_toc(self, muc_giam):
        self.toc_do -= muc_giam
        if self.toc_do < 0:
            self.toc_do = 0
        print(f"[Xe {self.hang}] Giảm tốc xuống còn {self.toc_do} km/h.")

    def dam(self):
        self.toc_do = 0
        print(f"[Xe {self.hang}] đã xảy ra va chạm và khựng lại hoàn toàn.")


class taikhoan:
    def __init__(self, ten_tk, so_tk, ngan_hang, so_du_ban_dau=0):
        self.ten_tk = ten_tk
        self.so_tk = so_tk
        self.ngan_hang = ngan_hang
        self.so_du = so_du_ban_dau

    def gui(self, so_tien):
        if so_tien > 0:
            self.so_du += so_tien
            print(f"[Gửi tiền] Thành công! Đã nạp {so_tien:,.0f}đ vào tài khoản {self.so_tk}.")
        else:
            print("[Lỗi] Số tiền gửi phải lớn hơn 0.")

    def rut(self, so_tien):
        if 0 < so_tien <= self.so_du:
            self.so_du -= so_tien
            print(f"[Rút tiền] Thành công! Đã rút {so_tien:,.0f}đ khỏi tài khoản {self.so_tk}.")
        else:
            print("[Lỗi] Số dư không đủ hoặc số tiền rút không hợp lệ.")

    def kiem_tra_so_du(self):
        print(f"[Tra cứu] Chủ thẻ: {self.ten_tk} | NH: {self.ngan_hang} | Số dư hiện tại: {self.so_du:,.0f}đ")
        
       
print("Test lớp con chó")
corgi = concho("kio", "Vàng", "Corgi")
corgi.sua()
corgi.an("xúc xích")
corgi.vay_duoi()

print("\n Test lớp oto")
mercedes = oto("Mercedes C300", "Sedan", "Đen", "2 Tỷ VND")
mercedes.tang_toc(50)
mercedes.tang_toc(30)
mercedes.giam_toc(40)
mercedes.dam()

print("\n Test lớp tài khoản")
tk_ca_nhan = taikhoan("Nguyen Van A", "123456789", "Vietcombank", 5000000)
tk_ca_nhan.kiem_tra_so_du()
tk_ca_nhan.gui(2000000)
tk_ca_nhan.rut(10000000) # Thử rút quá số dư
tk_ca_nhan.rut(1500000)
tk_ca_nhan.kiem_tra_so_du()