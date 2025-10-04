from openai import OpenAI
from fitness.models import Gym
client=OpenAI(api_key='Sekretyny_Klucz')

def generator(gym):
    prompt=f"""
    Opracuj plan treningu w {gym.place} dla osoby która ćwiczy już {gym.experience}, i che obecnie inwestować w 
    {gym.objective}, w wieku {gym.age}, oraz o wadze {gym.libra} kg, daj mu co tyle ćwiczeń {gym.n_exercise} do każdego 
    ćwiczenia dodaj adres url do youtuba
    """
    response=client.chat.completions.create(
        model='gpt-4-min',
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000
    )
    return response['choices'][0]['message']['content'].strip()