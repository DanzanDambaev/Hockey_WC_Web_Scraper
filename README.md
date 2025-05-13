# Hockey_WC_Web_Scraper
**Hockey_WC_Web_Scraper** ir Pasaules hokeja čempionāta tīmekļa skrāpis, kurš izmanto IIHF adrese "https://www.iihf.com/en/events/2025/wm/schedule",
lai saņemt datus par spēlēm.

Papildi tiek izstrādāta informācijas glabāšanas struktūra **class Spele** ērtākai piekļuvei, ka arī menu spēļu izvadīšanai terminālī.

## Izmantošana

Lai izmantot programmu, ir nepieciešams instalēt **requests** un **BeutifulSoup**

Izmantojiet komandu *pip* lai instalēt **requests** un **BeutifulSoup**.

```
pip install requests
pip install beautifulsoup4
```

Koda procesā terminālī tiks parādīta menu, kurā iespējams izvēlēties norādītu opciju lai izvadīt atbilstošu informāciju.

Ir iespējams manuāli mainīt gadus kodā **2025** vietā, lai saņemt rezultātus no citiem gadiem.

```
adrese = "https://www.iihf.com/en/events/2025/wm/schedule"
```
