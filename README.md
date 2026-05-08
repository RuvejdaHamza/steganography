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


## Kërkesat

### Para ekzekutimit të projektit duhet të keni të instaluar:

**Python 3**
**Bibliotekën Pillow**

## Instalimi

Instaloni bibliotekën e nevojshme me komandën:

pip install pillow

### Përgatitja e imazhit

Vendosni një imazh BMP me emrin **cover.bmp**  në të njëjtin folder me projektin.

Nëse nuk keni imazh, mund të krijoni një automatikisht me këtë komandë:

python -c "from PIL import Image; Image.new('RGB', (800, 600), color=(100,150,200)).save('cover.bmp')"
Përgatitja e mesazhit sekret

Ne file-in me emrin **secret.txt** shtoni mesazhin sekret brenda tij.

### Fshehja e mesazhit

Për të fshehur mesazhin brenda imazhit, ekzekutoni **python embed.py**
Pas ekzekutimit do të krijohet imazhi me mesazhin e fshehur.

### Nxjerrja e mesazhit

Për të nxjerrë mesazhin sekret nga imazhi, përdorni **python extract.py**
Mesazhi sekret do të shfaqet në terminal.
