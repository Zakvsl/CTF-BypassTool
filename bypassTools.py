import requests
print(r"""
 ____              ____  ___    
| __ ) _   _ _   _/  _ \/ __ \SSSSS
|  _ \| | | | | | | | )/ (_) \SSSSS
| | ) | |_| | |_| | __/| |  | |SSSSS
|____/ \__, |\__, | |  | |  | |SSSSS
       |___/ |___/| Your Head!               
""")

def find_flag_with_user_input(url):
    """Minta input User-Agent dan Referer dari pengguna, kemudian cari flag."""
    # Meminta User-Agent dari pengguna
    user_agent = input("Masukkan User-Agent yang akan digunakan: ").strip()
    
    # Membuat header awal hanya dengan User-Agent
    headers = {
        "User-Agent": user_agent
    }
    
    try:
        # Mengirimkan permintaan awal hanya dengan User-Agent
        response = requests.get(url, headers=headers, timeout=5)
        print(f"Testing dengan User-Agent: {user_agent}")
        print(f"Status code: {response.status_code}")
        print("Pesan dari server:")
        print(response.text)
        
        # Memeriksa apakah flag ditemukan tanpa Referer
        if "flag" in response.text.lower():
            print("Flag ditemukan tanpa Referer!")
            return
        
        # Jika flag tidak ditemukan, meminta Referer dari pengguna
        custom_referer = input("Masukkan Referer yang akan digunakan: ").strip()
        
        # Menambahkan Referer ke header
        headers["Referer"] = custom_referer
        
        # Mengirimkan permintaan kedua dengan Referer
        response = requests.get(url, headers=headers, timeout=5)
        print(f"Testing dengan User-Agent: {user_agent} dan Referer: {custom_referer}")
        print(f"Status code: {response.status_code}")
        print("Pesan dari server:")
        print(response.text)
        
        # Memeriksa apakah flag ditemukan
        if "flag" in response.text.lower():
            print("Flag ditemukan!")
        else:
            print("Flag tidak ditemukan dengan Referer ini.")
    
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

def bypass_ctf():
    """Fungsi utama untuk menjalankan bypass CTF."""
    # Meminta input URL dari user
    url = input("Masukkan URL target: ").strip()
    
    # Menjalankan fungsi untuk mencari flag berdasarkan input pengguna
    find_flag_with_user_input(url)

if _name_ == "_main_":
    bypass_ctf()