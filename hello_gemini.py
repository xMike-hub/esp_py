from google import genai
from google.genai import types 
import os

# La nostra chiave non deve essere mai scritta grzie punto 2

chiave = os.environ["GEMINI_API_KEY"]
# Configuro un client Genai e lo configuro con la chiave
client = genai.Client(api_key=chiave)

config = types.GenerateContentConfig(
    temperature=0.2, 
    max_output_tokens=1024,
    )
# Genera risposta
response = client.models.generate_content(
    model= "geminai-flash-latest", # Chiedo a google di usare il modello veloce
    contents= "Ciao! Chi sei?", # faccio una domanda al modello
)

# STAMPA OUTPUT
print(response.text)