import time
import sys

# Fungsi baru untuk mendapatkan input pengguna dengan validasi
def get_user_config():
    """Meminta pengguna untuk konfigurasi karakter, kecepatan, dan mode."""
    # Fitur 1: Variasi Karakter
    char = input("Masukkan karakter untuk pola (contoh: *, #, @, -): ") or '-'
    
    # Fitur 1: Variasi Kecepatan
    while True:
        try:
            speed_input = input("Masukkan kecepatan perulangan (delay dalam detik, contoh: 0.05): ")
            if not speed_input:
                delay = 0.1 # Nilai default
            else:
                delay = float(speed_input)
                if delay < 0:
                    raise ValueError
            break
        except ValueError:
            print("Input kecepatan tidak valid. Masukkan angka positif.")

    # Fitur 2: Mode Pola Baru
    mode = input("Pilih Mode Pola (A: Kuadrat, B: Fibonacci): ").upper()
    if mode not in ('A', 'B'):
        mode = 'A' # Default mode
    
    return char, delay, mode

# Fungsi bantuan untuk menghasilkan angka Fibonacci (untuk Mode B)
def fibonacci_generator(n):
    """Menghasilkan deret Fibonacci hingga suku ke-n."""
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b
        
# Fungsi utama untuk menjalankan perulangan dengan konfigurasi baru
def run_animation(char, delay, mode):
    print(f"\nMode Aktif: {mode} | Karakter: {char} | Kecepatan: {delay}s")
    print("Tekan Ctrl+C untuk keluar.")
    
    try:
        while True:
            if mode == 'A':
                # MODE A: Pola Kuadrat (Pola asli dari kode awal)
                for i in range(1, 9):
                    print(char * (i * i))
                    time.sleep(delay)

                for i in range(7, 1, -1):
                    print(char * (i * i))
                    time.sleep(delay)
            
            elif mode == 'B':
                # MODE B: Pola Fibonacci (Fitur 2 Baru)
                fib_values = list(fibonacci_generator(8)) # Ambil 8 suku pertama
                
                # Meningkat
                for length in fib_values:
                    print(char * length)
                    time.sleep(delay)

                # Menurun (Membalik deret, dimulai dari yang terbesar)
                for length in reversed(fib_values[:-1]):
                    print(char * length)
                    time.sleep(delay)

    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna.")
        sys.exit()

# Program Utama
if __name__ == "__main__":
    # Dapatkan konfigurasi dari pengguna (Fitur 1 & 2)
    karakter_pola, kecepatan_delay, mode_pola = get_user_config()
    
    # Jalankan animasi
    run_animation(karakter_pola, kecepatan_delay, mode_pola)