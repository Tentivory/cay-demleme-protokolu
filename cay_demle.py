#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çay Demleme Protokolü - Resmi ve Absürt Simülatör
Çay demlenmeden kod yazılmaz. Bu program bunu kanıtlar.
"""

import time
import random
import sys

def yavas_yaz(metin, hiz=0.03):
    """Çay gibi yavaş yavaş yaz"""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def cay_demle():
    print("=" * 50)
    yavas_yaz("☕ ÇAY DEMLEME PROTOKOLÜ BAŞLATILIYOR ☕")
    print("=" * 50)
    time.sleep(1)
    
    asamalar = [
        ("Su kaynatılıyor...", "Su kaynamazsa çay olmaz, hayat olmaz."),
        ("Çaylık ısıtılıyor...", "Soğuk çaylık = trajedi."),
        ("İlk demleme (açma) yapılıyor...", "Açma çay, protokolün kalbidir."),
        ("İkinci demleme...", "Şimdi ciddi işler başlıyor."),
        ("Çay dinleniyor...", "Sabır, çay gibi demlenir."),
        ("Bardak dolduruluyor...", "İnce belli bardak şart. Kalın belli yasak."),
    ]
    
    for asama, yorum in asamalar:
        yavas_yaz(f"\n▶ {asama}")
        time.sleep(random.uniform(1.5, 3.0))
        yavas_yaz(f"   → {yorum}")
        time.sleep(1)
    
    yavas_yaz("\n✅ ÇAY DEMLENDİ!")
    yavas_yaz("Artık kod yazabilirsiniz. Ama önce bir yudum alın.")
    
    # Gizli siyasi not (base64 benzeri ama basit)
    gizli = "bürokrasi çay demlerken de var"
    # print(gizli)  # Açılmasın, saklı kalsın
    
    while True:
        cevap = input("\nÇay içtin mi? (evet/hayır): ").strip().lower()
        if cevap == "evet":
            yavas_yaz("Mükemmel. Protokol tamamlandı. Kod yazmaya başlayabilirsiniz.")
            yavas_yaz("Ama unutma: Her 45 dakikada bir yeni çay.")
            break
        elif cevap == "hayır":
            yavas_yaz("Hata! Çay içilmeden protokol tamamlanamaz. Tekrar demleniyor...")
            time.sleep(2)
            yavas_yaz("(Sonsuz döngüye hoş geldiniz)")
        else:
            yavas_yaz("Anlaşılmadı. Çay içildi mi içilmedi mi?")

if __name__ == "__main__":
    try:
        cay_demle()
    except KeyboardInterrupt:
        yavas_yaz("\n\nProtokol kesildi. Çay soğudu. Yazık.")
        sys.exit(0)
