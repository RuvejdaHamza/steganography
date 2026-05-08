# Steganografia 

## Qëllimi i projektit

Ky projekt demonstron **steganografinë** - artin e fshehjes së informacionit brenda një imazhi pa u vënë re nga syri i njeriut.

**Objektivi kryesor:** Të fshehim një mesazh tekst brenda një imazhi bitmap (BMP) duke ndryshuar bitin e fundit (LSB - Least Significant Bit) të ngjyrave të pikselave.

## Si funksionon?

### Parimi bazë
- Çdo piksel në imazh ka tre vlera: **R (Kuqe)**, **G (Gjelbër)** dhe **B (Blu)**
- Secila vlerë është nga **0 deri në 255** (8 bit në binar)
- Biti i fundit (LSB) është më pak i rëndësishëm - ndryshimi i tij nga 0 në 1 ndryshon ngjyrën vetëm për ±1
- Ky ndryshim është i **padukshëm** për syrin e njeriut

### Struktura e të dhënave të fshehura
- **14 bitat e parë:** Ruajnë gjatësinë e mesazhit (mund të fshehë deri në 16,383 karaktere)
- **7 bitat e ardhshëm:** Çdo karakter konvertohet në 7 bit (ASCII standard)

### Siguria
Përdoret një **çelës (key)** për të përzier renditjen e pikselave. 
Pa çelësin e saktë, mesazhi nuk mund të nxirret edhe nëse dikush e di teknikën.

## Çfarë kam bërë?

Kam implementuar **dy skripta Python**:

| Skripta | Funksioni |
|---------|-----------|
| `embed.py` | Fsheh mesazhin sekret brenda imazhit |
| `extract.py` | Nxjerr mesazhin e fshehur nga imazhi |

### Teknologjitë e përdorura
- **Python 3** - Gjuha programuese
- **Pillow (PIL)** - Biblioteka për manipulimin e imazheve
- **Random** - Për randomizimin e renditjes së pikselave
