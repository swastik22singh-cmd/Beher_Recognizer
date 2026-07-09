import re

# Independent vowels
HRASVA = {'अ', 'इ', 'उ', 'ऋ'}
DEERGHA = {'आ', 'ई', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ'}

# Hindi matras
HRASVA_MATRAS = {'ि', 'ु', 'ृ'}
DEERGHA_MATRAS = {'ा', 'ी', 'ू', 'े', 'ै', 'ो', 'ौ'}


def generate_pattern(text):
    """
    Converts Hindi text into a matra pattern.
    Hrasva (short) = 1
    Deergha (long) = 2
    """

    # Remove punctuation
    text = re.sub(r"[^\u0900-\u097F\s]", "", text)

    pattern = []

    for ch in text:

        # Independent vowels
        if ch in HRASVA:
            pattern.append("1")

        elif ch in DEERGHA:
            pattern.append("2")

        # Matras
        elif ch in HRASVA_MATRAS:
            pattern.append("1")

        elif ch in DEERGHA_MATRAS:
            pattern.append("2")

    return "".join(pattern)


if __name__ == "__main__":
    text = input("Enter Hindi Shayari: ")

    print("Pattern:", generate_pattern(text))
