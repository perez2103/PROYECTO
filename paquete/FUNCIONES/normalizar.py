def tildes(t):
    cambiar = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in cambiar:
        t = t.replace(a, b).replace(a.upper(), b.upper())
    return t