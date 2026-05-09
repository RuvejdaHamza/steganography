# Steganografia - Image Steganography Project

## Qëllimi i projektit
Ky projekt demonstron **steganografinë**, artin e fshehjes së informacionit brenda një imazhi pa u vënë re nga syri i njeriut.

Objektivi kryesor është të fshehim një mesazh tekst brenda një imazhi bitmap (BMP) duke ndryshuar bitin e fundit (LSB - Least Significant Bit) të ngjyrave të pikselave.

---

## Si funksionon?

### Parimi bazë
- Çdo piksel në imazh ka tre vlera: **R (Kuqe), G (Gjelbër), B (Blu)**
- Secila vlerë është nga 0 deri në 255 (8-bit)
- **LSB (Least Significant Bit)** është biti më pak i rëndësishëm
- Ndryshimi i tij nga 0 në 1 ndryshon ngjyrën vetëm për ±1
- Ky ndryshim është i padukshëm për syrin e njeriut

---

### Struktura e të dhënave të fshehura
- **14 bitat e parë:** ruajnë gjatësinë e mesazhit (deri në 16,383 karaktere)
- **7 bitat e ardhshëm:** çdo karakter konvertohet në 7-bit ASCII

---

## Siguria
Përdoret një **çelës (key)** për të përzier renditjen e pikselave.

- Pa çelësin e saktë, mesazhi nuk mund të nxirret
- Edhe nëse dihet teknika, renditja e gabuar e pixelave e prish rezultatin

---

## Çfarë kam bërë?

Kam implementuar dy skripta në Python:

| Skripta      | Funksioni |
|--------------|----------|
| `embed.py`   | Fsheh mesazhin sekret brenda imazhit |
| `extract.py` | Nxjerr mesazhin e fshehur nga imazhi |

---

## Teknologjitë e përdorura
- Python 3
- Pillow (PIL) – për manipulimin e imazheve
- Random – për përzierjen e pikselave

---

## Kërkesat
Para ekzekutimit të projektit duhet të keni:

- Python 3
- Bibliotekën Pillow

---

## Instalimi
Instaloni bibliotekën e nevojshme:

```bash
pip install pillow
