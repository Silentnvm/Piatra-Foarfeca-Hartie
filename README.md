# Piatra, Foarfecă, Hârtie

Acesta este un proiect simplu în Python care implementează clasicul joc "Piatră, Foarfecă, Hârtie". Proiectul conține două versiuni ale jocului: una care rulează în consolă și o versiune web interactivă.

## Cuprins

- [Descriere](#descriere)
- [Tehnologii Utilizate](#tehnologii-utilizate)
- [Instalare](#instalare)
- [Utilizare](#utilizare)
  - [Versiunea în Consolă](#versiunea-în-consolă)
  - [Versiunea Web](#versiunea-web)
- [Cum se Joacă](#cum-se-joacă)

## Descriere

Proiectul oferă două moduri de a juca "Piatră, Foarfecă, Hârtie" împotriva calculatorului:

1.  **Versiunea în Consolă (`piatra_foarfeca_hartie.py`):** O aplicație text-based care rulează direct în terminal. Jucătorul introduce alegerea sa (piatră, foarfecă sau hârtie) de la tastatură, iar rezultatul este afișat imediat.
2.  **Versiunea Web (`p_f_h_web.py`):** O aplicație web simplă și intuitivă construită cu ajutorul bibliotecii Streamlit. Jucătorul poate selecta opțiunea dorită folosind butoane, iar scorul este actualizat în timp real.

## Tehnologii Utilizate

- **Python 3:** Limbajul de programare de bază.
- **Streamlit:** Framework-ul folosit pentru a crea interfața web interactivă.

## Instalare

Pentru a rula acest proiect, trebuie să aveți Python 3 instalat pe sistemul dumneavoastră.

1.  Clonați acest repository pe mașina locală:
    ```bash
    git clone https://github.com/nume-utilizator/Piatra_foarfeca_hartie.git
    cd Piatra_foarfeca_hartie
    ```

2.  Pentru versiunea web, este necesar să instalați biblioteca `streamlit`. Puteți face acest lucru folosind pip:
    ```bash
    pip install streamlit
    ```
    Nu sunt necesare alte biblioteci pentru versiunea în consolă, deoarece folosește doar module standard din Python.

## Utilizare

### Versiunea în Consolă

Pentru a juca versiunea în consolă, navigați în directorul proiectului și rulați scriptul `piatra_foarfeca_hartie.py`:

```bash
python piatra_foarfeca_hartie.py
```

Urmați instrucțiunile afișate în consolă pentru a face o alegere și pentru a continua sau opri jocul.

### Versiunea Web

Pentru a lansa versiunea web, asigurați-vă că ați instalat `streamlit`, apoi rulați următoarea comandă în terminal:

```bash
streamlit run p_f_h_web.py
```

Această comandă va porni un server local și va deschide aplicația într-o filă nouă a browserului web.

## Cum se Joacă

Regulile jocului sunt simple:

- **Piatra** zdrobește **Foarfeca**.
- **Foarfeca** taie **Hârtia**.
- **Hârtia** învelește **Piatra**.

Jocul se desfășoară împotriva calculatorului, care face o alegere aleatorie la fiecare rundă.
