from openai import OpenAI
import base64
import mimetypes
import os



client=OpenAI(api_key=key)

def generator_gym(gym):
    prompt=f"""
    Opracuj plan treningu w {gym.place} dla osoby która ćwiczy już {gym.experience} lat, i che obecnie inwestować w 
    {gym.objective}, w wieku {gym.age}, oraz o wadze {gym.libra} kg, daj mu co tyle ćwiczeń na jedną partie 
    {gym.n_exercise} dodaj ile powtórzeń. Do każdego ćwiczenia dodaj adres url do youtuba upewnij się że film jest nadal
     dostępny. Rospisz na konkretne dni co trenować
    """
    response=client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000
    )
    return response.choices[0].message.content.strip()


def generator_diet(diet):
    prompt=f"""Wygeneruj plan diety na {diet.diet_time} dni, mają się w nim znajdować te składniki {diet.food},
    a te składniki wyklucz {diet.food_not_like}. Jestem uczulony na 
    {(diet.allergies if diet.allergies else "brak alergii")}. Moim celem jest
    {diet.intention}. Jeśli jakieś danie wymaga przygotowania podaj  2 adres strony z przepisem 
    
    """
    response=client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000
    )
    return response.choices[0].message.content.strip()


def generator_photo(photo):


    image_path = photo.image.path
    if not os.path.exists(image_path):
        return "Nie znaleziono pliku zdjęcia."


    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type:
        mime_type = "image/jpeg"

    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")


    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "Oceń postawę osoby na zdjęciu treningowym. "
                        "Podaj w punktach:\n"
                        "1️⃣ Opis postawy (czy jest stabilna / bezpieczna),\n"
                        "2️⃣ 3–5 błędów technicznych, jeśli widać,\n"
                        "3️⃣ Konkretne wskazówki, jak poprawić formę,\n"
                        "4️⃣ Ogólną ocenę w skali 1–5.\n"
                        "Użyj prostego języka, unikaj terminów medycznych."
                    ),
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{mime_type};base64,{image_data}"
                    },
                },
            ],
        }
    ]


    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=800,
            temperature=0.4,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Wystąpił błąd podczas analizy zdjęcia: {e}"