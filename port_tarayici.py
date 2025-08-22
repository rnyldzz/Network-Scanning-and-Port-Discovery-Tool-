import socket
import sys

def port_tarayici(hedef):
    """
    Belirtilen hedef IP veya alan adındaki açık portları tarar.
    """
    try:
        hedef_ip = socket.gethostbyname(hedef)
    except socket.gaierror:
        print(f"Hata: Alan adı çözümlenemedi: {hedef}")
        return

    print(f"--- Port taraması başlıyor: {hedef} ({hedef_ip}) ---")
    
    for port in range(1, 8081):
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(1)
        
        sonuc = soket.connect_ex((hedef_ip, port))
        
        if sonuc == 0:
            print(f"[*] Port {port} açık.")
        
        soket.close()
        
    print("--- Tarama tamamlandı. ---")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Kullanım: python port_tarayici.py <hedef_ip_veya_alan_adi>")
    else:
        hedef = sys.argv[1]
        port_tarayici(hedef)
