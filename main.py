from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Définition du format de la requête (basé sur ta fonction OpenAI)
class MicroscopeRequest(BaseModel):
    symbol: str

# Base de données fictive des microscopes
MICROSCOPE_DATA = {
    "MS100": "Le MS100 est un microscope optique adapté aux débutants.",
    "PRO200": "Le PRO200 est un microscope professionnel avec caméra intégrée.",
    "BIOX500": "Le BIOX500 est idéal pour les analyses biologiques avancées.",
    "DIGI800": "Le DIGI800 est un microscope numérique avec écran tactile.",
}

@app.post("/get_microscope_info")
def get_microscope_info(request: MicroscopeRequest):
    symbol = request.symbol.upper()  # Normaliser en majuscules

    if symbol in MICROSCOPE_DATA:
        return {
            "symbol": symbol,
            "description": MICROSCOPE_DATA[symbol]
        }
    else:
        raise HTTPException(status_code=404, detail="Microscope non trouvé")
