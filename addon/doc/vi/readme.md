# SMB
NVDA add-on cho phần mềm Sao Mai Braille  
Phiên bản 25.10  
Bản quyền 2022 - 2025 bởi Nhóm Công Nghệ Sao Mai

Sao Mai Braille (SMB) là phần mềm soạn thảo văn bản định dạng và chuyển dịch chữ nổi miễn phí, phát triển bởi
[Sao Mai Vì Người Mù](https://www.saomaicenter.org/vi).
Hiện tại, có một số vấn đề về tiếp cận mà không thể khắc phục trực tiếp trong chương trình. Vì vậy, add-on nhỏ này sẽ giúp trình đọc màn hình NVDA tiếp cận tốt hơn với giao diện của SMB.
Có thể xem thêm thông tin về chương trình SMB tại [https://www.saomaicenter.org/vi/smsoft/smb](https://www.saomaicenter.org/vi/smsoft/smb)

# Các Phím tắt bị loại bỏ
Kể từ phiên bản SMB 25.5, các phím tắt sau sẽ bị loại bỏ:

- Alt+F9: mở hộp thoại Insert equation
- Alt+F10: mở hộp thoại Insert Picture
- Alt+F11: mở hộp thoại Insert Music Score

Thay vào đó, chúng tôi sẽ sử dụng:

- Ctrl+Shift+Q: mở hộp thoại Insert equation
- Ctrl+Shift+G: mở hộp thoại Insert Picture
- Ctrl+Shift+M: mở hộp thoại Insert Music Score

Điều này có thể giúp người dùng dễ ghi nhớ hơn.
Tuy nhiên, nhiều người dùng có thể đã quen với các phím tắt cũ.
Vì vậy, add-on này đã tích hợp các phím lệnh cũ để bạn có thể sử dụng song song cả hai kiểu phím tắt.

Tuy nhiên, chúng tôi vẫn khuyến khích bạn dùng các phím tắt mới vì những lợi ích mà chúng mang lại.

Từ phiên bản 25.7 của add-on này, chúng tôi thêm phím tắt của SMB vào phân loại tên SMB để người dùng có thể tùy chỉnh chúng thông qua hộp thoại Quản Lý Thao Tác của NVDA khi đứng tại cửa sổ Sao Mai Braille.

# Dịch add-on
Hiện tại, add-on này bao gồm các chuỗi thông báo trợ giúp nhập cho các phím tắt cũ của SMB, cũng như tập tin README này.
Bạn có thể dịch chúng thông qua [kho mã SMB trên GitHub](https://github.com/manhcuong0312/SMB),
hoặc liên hệ với chúng tôi qua thông tin trong phần trợ giúp và phản hồi nếu bạn không quen sử dụng nền tảng đó.

# trợ giúp và phản hồi

Sao Mai Vì Người Mù là một tổ chức phi lợi nhuận quy mô nhỏ, có trụ sở tại HCM, Việt Nam.
Chúng tôi chủ yếu dựa vào các khoản tài trợ dự án để thực hiện các hoạt động hỗ trợ miễn phí cho người khiếm thị.
Chúng tôi cần sự giúp đỡ của quý vị để có thể duy trì và mở rộng các hoạt động hỗ trợ này.
Vui lòng liên hệ với chúng tôi theo thông tin sau:

Sao Mai Vì Người Mù

- Địa chỉ: 52/22 Huỳnh Thiện Lộc, Hòa Thạnh, Tân Phú, TP.HCM, Việt Nam.
- Email: [support@saomaicenter.org](mailto:support@saomaicenter.org)
- Liên hệ để dịch add-on này: [tech@saomaicenter.org](mailto:tech@saomaicenter.org)
- Website: [https://saomaicenter.org/vi](https://saomaicenter.org/vi)

Đăng ký tham gia/theo dõi các kênh của chúng tôi:

- Đăng ký nhận thông báo từ chúng tôi bằng cách gửi email trống tới: [tin+subscribe@saomaicenter.org](mailto:tin+subscribe@saomaicenter.org)
- Diễn đàn trao đổi qua email: [https://groups.io/g/smcb](https://groups.io/g/smcb)
- X: [x.com/SaoMaiCenter](https://x.com/saomaicenter)
- Facebook: [fb.com/SaoMaiForTheBlind](https://www.facebook.com/saomaifortheblind)
- Youtube: [https://www.youtube.com/@smcenter](https://www.youtube.com/@smcenter)

# Nhật Kí thay đổi

## 2025.10
- Tương thích với NVDA 2025.3.
- Thêm tập tin Readme cho ngôn ngữ Thổ Nhĩ Kỳ (Đóng góp bởi Umut KORKMAZ).
- Cập nhật bản địa hóa.

## 2025.7.2
- Cập nhật trợ giúp nhập cho phím tắt của SMB.
- Cập nhật bản dịch tiếng Việt. Các thuật ngữ Insert Equation, Insert Picture và Insert Music Score được dịch khớp với giao diện tiếng Việt của SMB.

## 2025.7
- Thêm phím tắt của SMB vào phân loại tên SMB để người dùng có thể tùy chỉnh chúng thông qua hộp thoại Quản Lý Thao Tác của NVDA khi đứng tại cửa sổ Sao Mai Braille.
- Tương thích với NVDA 2025.2.

## 2025.5.22
- Cảnh báo đến người dùng nếu dùng các phím tắt cũ khi chưa tạo tài liệu .smd hoặc .smb

## 2025.5

* Cập nhật mẫu tiện ích bổ sung theo phiên bản tháng 3/2025
* Làm cho trợ giúp đầu vào của ba phím tắt bị loại bỏ có thể dịch được
* Cập nhật tập tin readme

## 2025.4.2

* Thêm tính năng cho phép sử dụng song song phím tắt mới và cũ của SMB
* Cập nhật tập tin readme

## 2025.4

* Tương thích với NVDA 2025.1
* Thay đổi địa chỉ kho mã của tiện ích bổ sung
* Cập nhật tập tin readme

## 2023.12

* Tương thích với NVDA 2024.1
* Cập nhật tập tin readme

## 2023.10

* Tương thích với NVDA 2023.3
* Chuyển kho mã Github sang tài khoản của manhcuong0312

## 2023.9

* Tương thích với NVDA 2023.2

## 2023.4

* Sửa lỗi với ngôn ngữ Thổ Nhĩ Kỳ, và hiện tại tiện ích bổ sung yêu cầu NVDA 2022.1.0 trở lên

## 2023.3

* Sửa tên và tóm tắt
* Cập nhật bản dịch

## 2023.2

* Tương thích với NVDA 2023.1

## 2023.1

* Tương thích với NVDA 2022.4
* Thêm bản dịch tiếng Thổ Nhĩ Kỳ bởi Umut KORKMAZ

## 2022.8

* Tương thích với NVDA 2022.3