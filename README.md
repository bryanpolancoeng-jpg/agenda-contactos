# Agenda de contactos

Agenda de contactos en consola hecha en Python. Permite listar, agregar y buscar contactos.
Ejercicio de la asignatura Herramientas Avanzadas para el Desarrollo de Aplicaciones (102HAD1), UTLA.

## Biblioteca de terceros agregada: rapidfuzz

**Para qué se agregó:** la búsqueda original solo encontraba un contacto si el texto estaba
escrito exactamente igual (`"Jhon"` no encontraba a `"John Smith"`). Con `rapidfuzz` la búsqueda
tolera errores de escritura y ordena los resultados del más al menos parecido.

**Cómo está integrada:** solo el archivo `busqueda.py` (el adaptador) importa `rapidfuzz`.
El programa principal (`main.py`) usa la función `buscar_contactos()` y no conoce la biblioteca.
Para cambiar a otra (por ejemplo `thefuzz`) solo se modifica `busqueda.py`.

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows (en Mac/Linux: source .venv/bin/activate)
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

## Estructura

- `main.py`: menú y funciones de la agenda.
- `busqueda.py`: adaptador que envuelve a rapidfuzz.
- `requirements.txt`: dependencias con su versión.

## Análisis

1. ¿Qué resolvía el código anterior y qué se gana con la biblioteca?
El código anterior buscaba contactos con texto in nombre: solo encontraba un resultado si el texto estaba escrito igual que en la agenda (ignorando mayúsculas). Tenía 7 líneas de código. La función buscar_contactos del adaptador tiene 13 líneas (15 si se cuenta todo el archivo busqueda.py con el import y la constante; en ambos casos sin docstrings ni líneas vacías), así que no se gana en cantidad de líneas: el adaptador es más largo. Lo que se gana es capacidad: ahora “Jhon” encuentra a “John Smith”, los resultados salen ordenados del más al menos parecido, y se puede ajustar qué tan estricta es la búsqueda con un umbral. Escribir eso a mano implicaría implementar y mantener un algoritmo de distancia de edición, algo que la biblioteca ya trae probado. En mantenimiento también se gana: main.py quedó más corto y la lógica de búsqueda está en un solo archivo. Al probar, el umbral inicial de 70 no encontraba a John Smith con “Jhon” (sacaba 67.5), y tuve que bajarlo a 60.

2. ¿Qué criterio pesó más y cuándo convendría la alternativa?
Pesó más el mantenimiento: rapidfuzz tuvo su último commit el 12 de octubre de 2026 y su última versión el 30 de agosto de 2026, mientras que thefuzz tiene su último commit en marzo de 2025 y su última versión en enero de 2024. Además, thefuzz depende de rapidfuzz, así que usar rapidfuzz directamente evita una capa intermedia. La alternativa convendría en un proyecto que ya use la interfaz de FuzzyWuzzy y no quiera reescribir su código.

3. ¿Qué riesgo introduce la dependencia y cómo lo reducen el adaptador y el registro de versión?
Depender de una biblioteca externa significa que una actualización podría cambiar su comportamiento o romper compatibilidad, que el proyecto podría dejar de mantenerse, o que exija una versión de Python que no tengo (rapidfuzz 3.14.6 requiere Python 3.11 o superior). El registro de la versión en requirements.txt (con pip freeze, que fija la versión exacta) hace que quien instale el proyecto obtenga la misma versión con la que funcionó, así una actualización no cambia el comportamiento sin que yo lo decida. El adaptador busqueda.py reduce el riesgo de reemplazo: si rapidfuzz dejara de funcionar o de mantenerse, solo cambiaría ese archivo y no main.py.

