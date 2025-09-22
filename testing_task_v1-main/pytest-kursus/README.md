# Pytest – mini-kursus (A–C)

See projekt on mõeldud, et harjutada testide kirjutamist `pytest` abil.

## Eeltingimused ja allalaadimine
1) Laadi projekt alla ja ava kaust `pytest-kursus`
2) (Soovitus) Loo virtuaalkeskkond
   - Windows: `python -m venv .venv` siis `venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
3) Paigalda pytest: `pip install pytest`
4) Kontrolli, et pytest töötab: `python -m pytest -q`

## Kuidas käivitada testid
1) Ava terminal projektikaustas `pytest-kursus`
2) Käivita kõik testid:
   pytest -q
3) Käivita ainult A-osa testid:
   pytest -q tests/test_a_basics.py
4) Käivita üksik testinimi (näiteks test_add_basic):
   pytest -q -k test_add_basic

## Ülesanne
1) Vaata `src/` failides olevaid funktsioone
2) Kirjuta teste `tests/` failides, et kontrollida funktsioonide õigsust
3) Mõned funktsioonid on tahtlikult vigased - sinu testid peaksid need leidma!
4) Kui testid kukuvad, siis oled leidnud vea. Kui testid lähevad läbi, siis funktsioon on õige.

## Ülesannete ülevaade
- A (a_basics.py): algtaseme puhtad funktsioonid (aritmeetika, sõned)
- B (b_collections_io.py): kogud ja failisüsteem (listid, sõnastikud, failid)  
- C (c_module.py): väike moodul klassi ja keerukamate servajuhtudega

