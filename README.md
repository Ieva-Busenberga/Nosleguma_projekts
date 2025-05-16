# iPhone Cenu Salīdzināšanas Sistēma

Šī programmatūra ir izstrādāta, lai automatizētu iPhone viedtālruņu cenu salīdzināšanas procesu starp diviem Latvijas interneta veikaliem: Euronics (euronics.lv) un RD Electronics (rdveikals.lv). Sistēma sastāv no atsevišķiem Python skriptiem, kas nolasa aktuālās iPhone modeļu cenas no katras mājaslapas un saglabā tās atsevišķos Excel failos, kā arī galvenās programmas, kas šos datus apstrādā, veic cenu salīdzināšanu un ģenerē kopsavilkumu.

## Projekta Uzdevums

Galvenais projekta uzdevums ir izveidot lietotājam draudzīgu un automatizētu veidu, kā salīdzināt dažādu iPhone modeļu cenas divos lielākajos Latvijas elektronikas veikalos. Projekta mērķis ir atvieglot lēmumu pieņemšanu par izdevīgāko pirkumu, sniedzot pārskatu par cenu atšķirībām un kopējo veikalu izdevīgumu. Šī sistēma ir izstrādāta, lai palīdzētu sekot līdzi iPhone cenu svārstībām un ātri noteikt labāko piedāvājumu.

## Izmantotās Python Bibliotēkas

Projekta izstrādes gaitā tiek izmantotas šādas Python bibliotēkas:

* **`requests`:** Šī bibliotēka tiek izmantota, lai nosūtītu HTTP pieprasījumus uz mājaslapām (euronics.lv un rdveikals.lv) un iegūtu to HTML saturu. Tā ir nepieciešama, lai piekļūtu mājaslapu datiem.
* **`bs4` (Beautiful Soup 4):** Šī bibliotēka tiek izmantota iegūtā HTML satura parsēšanai. Tā palīdz ērti orientēties HTML struktūrā un atlasīt nepieciešamos datus, piemēram, iPhone modeļu nosaukumus un cenas, izmantojot HTML tagus un klases.
* **`xlsxwriter`:** Šī bibliotēka tiek izmantota Excel failu (`.xlsx`) izveidei un datu ierakstīšanai tajos. Tā nodrošina iespēju saglabāt nolasītos datus strukturētā veidā, kas ir viegli lasāms un apstrādājams.
* **`subprocess`:** Šī bibliotēka tiek izmantota, lai palaistu atsevišķus Python skriptus (euronics.py un rdveikals.py) no galvenās programmas. Tas ļauj automatizēt datu nolasīšanas procesu pirms cenu salīdzināšanas.
* **`openpyxl`:** Šī bibliotēka tiek izmantota, lai atvērtu un lasītu datus no iepriekš saglabātajiem Excel failiem (euronics.xlsx un rdveikals.xlsx) galvenajā programmā. Tā ir nepieciešama, lai piekļūtu nolasītajiem datiem un veiktu cenu salīdzināšanu.
* **`re` (regulārās izteiksmes):** Šī bibliotēka tiek izmantota teksta apstrādei, lai no iPhone modeļu nosaukumiem iegūtu specifisku informāciju, piemēram, modeļa variantu (mini, Pro, Pro Max, Plus) un atmiņas apjomu (GB). Regulārās izteiksmes nodrošina elastīgu veidu, kā atrast un izvilkt nepieciešamo informāciju no dažādi formatētiem teksta datiem.

## Definētās Datu Struktūras

Projektā tiek izmantotas šādas definētas datu struktūras:

* **Saraksti (Lists):** Datu nolasīšanas skriptos iegūtie iPhone modeļu nosaukumi un cenas sākotnēji tiek glabāti sarakstos, kur katrs elements ir saraksts, kas satur modeļa nosaukumu un cenu. Piemēram: `['iPhone 15 Pro Max, 256 GB', '1450.00']`. Šie saraksti pēc tam tiek ierakstīti Excel failos.
* **Vārdnīcas (Dictionaries):** Galvenajā programmā, lai efektīvi salīdzinātu cenas, dati no abiem Excel failiem tiek pārveidoti vārdnīcās. Vārdnīcas atslēga ir elements, kas satur iPhone modeļa nosaukumu (ieskaitot variantu) un atmiņas apjomu (GB). Vērtība ir saraksts ar cenām (lai potenciāli apstrādātu vairākas cenas vienam modelim, lai gan šajā projektā parasti būs viena cena). Piemēram: `{'iPhone 15 Pro Max': {256: [1450.00], 512: [1600.00]}, 'iPhone 15 Pro': {128: [1200.00]}}`. Šī struktūra atvieglo modeļu salīdzināšanu pēc nosaukuma un atmiņas apjoma.

## Programmatūras Izmantošanas Metodes

1.  **Datu nolasīšanas skriptu palaišana:** Vispirms ir jāizpilda galvenā programma. Tā automātiski palaiž divus atsevišķus Python skriptus: `euronics.py` un `rdveikals.py`. Šie skripti nolasa iPhone modeļu cenas no attiecīgajām mājaslapām un saglabā tās divos atsevišķos Excel failos (`euronics.xlsx` un `rdveikals.xlsx`).
2.  **Datu nolasīšana un sakārtošana:** Galvenā programma pēc datu nolasīšanas skriptu veiksmīgas izpildes nolasa datus no `euronics.xlsx` un `rdveikals.xlsx` failiem, izmantojot `openpyxl` bibliotēku. Dati tiek apstrādāti, iegūstot modeļa nosaukumu (ar variāciju, ja tāda ir) un atmiņas apjomu (GB), izmantojot regulārās izteiksmes. Dati tiek saglabāti vārdnīcas elementos, kuru atslēga ir (modelis, atmiņas apjoms) un vērtība ir cena.
3.  **Cenu salīdzināšana:** Galvenā programma salīdzina katra iPhone modeļa cenu starp abiem veikaliem, ņemot vērā gan modeli, gan atmiņas apjomu.
4.  **Rezultātu saglabāšana:** Salīdzināšanas rezultāti tiek saglabāti jaunā Excel failā (`salidzinajums.xlsx`). Šajā failā ir norādīts modelis, atmiņas apjoms, cena Euronics, cena RD Electronics un veikals, kurā cena ir zemāka.
5.  **Kopsavilkuma izveide:** Programma aprēķina un parāda statistiku par to, cik reizes katrs veikals piedāvāja zemāku cenu, un parāda šo informāciju gan konsolē, gan saglabā `salidzinajums.xlsx` failā.

## Demonstrācijas Video (saite)

(https://ej.uz/Projekta_video_datustrukturas)

Šajā video būs redzama programmatūras darbība, sākot no skriptu palaišanas un datu nolasīšanas līdz pat cenu salīdzināšanas rezultātu un veikalu izdevīguma analīzes parādīšanai.

## GitHub Izmantošana

Viss projekta izstrādes process, ieskaitot programmas kodu un šo README failu, tiek glabāts un pārvaldīts GitHub repozitorijā. Katra koda izmaiņa tiek fiksēta, nodrošinot iespēju sekot līdzi projekta attīstībai un sadarboties ar citiem izstrādātājiem (ja tādi ir).
