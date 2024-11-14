import cv2
from pyzbar import pyzbar

# Fungsi untuk mendeteksi instruksi dari barcode
def detect_barcode_direction(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        
        if barcode_data == "left":
            print("Instruksi: Belok Kiri")
            return "left"
        elif barcode_data == "right":
            print("Instruksi: Belok Kanan")
            return "right"
        elif barcode_data == "forward":
            print("Instruksi: Maju")
            return "forward"
        else:
            print("Instruksi tidak dikenali:", barcode_data)
            return None
    return None


cap = cv2.VideoCapture(0)  # Sesuaikan dengan indeks kamera di Raspberry Pi
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Deteksi barcode pada frame
        direction = detect_barcode_direction(frame)

        # Implementasi gerakan berdasarkan instruksi
        if direction == "left":
            # Implementasi pergerakan ke kiri
            print("Robot bergerak ke kiri.")
        elif direction == "right":
            # Implementasi pergerakan ke kanan
            print("Robot bergerak ke kanan.")
        elif direction == "forward":
            # Implementasi pergerakan maju
            print("Robot bergerak maju.")
        
        # Tampilkan video dengan penanda barcode
        cv2.imshow("Barcode Detection", frame)

        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
