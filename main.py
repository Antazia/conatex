from fastapi import FastAPI

app = FastAPI()

@app.get("/microscope-info")
def get_microscope_info():
    return {
        "message": "Si vous cherchez un microscope, voici quelques conseils...",
        "details": "Les microscopes optiques sont les plus courants. Si vous voulez un modèle numérique, pensez aux options avec caméra intégrée."
    }
