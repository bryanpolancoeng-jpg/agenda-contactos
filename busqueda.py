from rapidfuzz import fuzz, process

UMBRAL_MINIMO = 60   


def buscar_contactos(texto, contactos, limite=5):
    """Devuelve los contactos cuyo nombre se parece a `texto`, del más al menos parecido.

    Tolera errores de escritura: "Jhon" encuentra a "John Smith".
    """
    if not texto.strip():
        return []

    nombres = [c["nombre"] for c in contactos]
    coincidencias = process.extract(
        texto,
        nombres,
        scorer=fuzz.WRatio,
        processor=lambda s: s.lower(),
        limit=limite,
        score_cutoff=UMBRAL_MINIMO,
    )
    return [contactos[posicion] for _, _, posicion in coincidencias]