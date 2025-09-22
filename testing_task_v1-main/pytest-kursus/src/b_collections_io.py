# B-OSA: kogud ja failid.
# Ülesanne: kirjuta teste, et leida vigased funktsioonid!

def unique_sorted(nums):
    """Tagasta kasvavas järjekorras unikaalsed arvud."""
    return sorted(set(nums))

def count_words(text):
    """Tagasta sõnade (split vastavalt whitespace) sageduste sõnastik."""
    words = text.lower().split()
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result

def merge_dicts(d1, d2):
    """Tagasta uus sõnastik, kus d2 väärtused varjutavad d1 omad."""
    result = d1.copy()
    result.update(d2)
    return result

def find_max_pair(nums):
    """Tagasta (max, näitude_arv); tühja korral ValueError."""
    if not nums:
        raise ValueError("Tühja loendi maksimum ei ole defineeritud")
    max_val = max(nums)
    count = nums.count(max_val)
    return (max_val, count)

def flatten(nested):
    """Lamedda [[...],[...]] -> [...] (ainult üks tase)."""
    result = []
    for sublist in nested:
        result.extend(sublist)
    return result

def read_file(path):
    """Loe failitekst ja tagasta stringina."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, text):
    """Kirjuta tekst faili ja tagasta kirjutatud märkide arv."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    return len(text)

def safe_get(d, key, default=None):
    """Võta d[key] või tagasta default, kui pole olemas."""
    return d.get(key, default)

def top_n(nums, n):
    """Tagasta suurimad n arvu kahanevas järjekorras; vigase n korral ValueError."""
    if n <= 0:
        raise ValueError("n peab olema positiivne")
    if n > len(nums):
        raise ValueError("n ei tohi olla suurem kui loendi pikkus")
    return sorted(nums, reverse=True)[:n]

def chunk_list(lst, size):
    """Tükelda list võrdseteks tükkideks (viimane võib olla lühem); size>0."""
    if size <= 0:
        raise ValueError("Suurus peab olema positiivne")
    result = []
    for i in range(0, len(lst), size):
        result.append(lst[i:i + size])
    return result
