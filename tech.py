from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def fiyat_karsilastir():
    # Tarayıcı ayarları
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Görünmez modda çalıştırmak için
    
    # Tarayıcıyı başlat
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        # Siteye git
        driver.get("https://www.amazon.com.tr/s?i=electronics&srs=44219324031&bbn=44219324031&rh=n%3A44219324031%2Cn%3A12466496031&s=date-desc-rank&ds=v1%3A6mBzYV7K1ylXxCO%2FcBwYKnfG6dokjZBYmAuPbXxEp78&pf_rd_i=44219324031&pf_rd_m=A1UNQM1SR2CHM&pf_rd_p=bcc88ca7-b7df-4b17-899c-41df4a987cde&pf_rd_r=JJYVFN9R7A3FACTHCJE1&pf_rd_s=merchandised-search-14&qid=1731944811&ref=sr_st_date-desc-rank")
        time.sleep(2)  # Sayfanın yüklenmesi için bekle
        
        # Ürün listesini bul
        urunler = driver.find_elements(By.CSS_SELECTOR, "#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(6)")
        
        for urun in urunler:
            try:
                # Ürün bilgilerini çek
                urun_adi = urun.find_element(By.CSS_SELECTOR, "URUN_ADI_SECICI").text
                sifir_fiyat = float(urun.find_element(By.CSS_SELECTOR, "SIFIR_FIYAT_SECICI").text.replace("TL", "").replace(".", "").replace(",", "."))
                ikinci_el_fiyat = float(urun.find_element(By.CSS_SELECTOR, "IKINCI_EL_FIYAT_SECICI").text.replace("TL", "").replace(".", "").replace(",", "."))
                
                # Fiyat karşılaştırması
                if ikinci_el_fiyat <= sifir_fiyat * 0.95:  # %5 daha uygun olanları bul
                    print(f"Ürün: {urun_adi}")
                    print(f"Sıfır Fiyat: {sifir_fiyat} TL")
                    print(f"İkinci El Fiyat: {ikinci_el_fiyat} TL")
                    print(f"Fark: %{((sifir_fiyat - ikinci_el_fiyat) / sifir_fiyat * 100):.2f}")
                    print("-" * 50)
                
            except Exception as e:
                print(f"Ürün bilgileri çekilirken hata: {e}")
                continue
                
    finally:
        driver.quit()

if __name__ == "__main__":
    fiyat_karsilastir()