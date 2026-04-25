from fastapi import FastAPI

app = FastAPI(

    title="VitalPet",
    description="VitalPet es un sistema inteligente de gestión veterinaria diseñado para acompañar la salud de tu mascota mucho más allá de la sala de espera. A través de una plataforma web y móvil, VitalPet centraliza el historial clínico completo de cada mascota: diagnósticos, tratamientos y evolución médica, todo al alcance del veterinario y del dueño en cualquier momento.",
    version="1.0.0",

)


@app.get("/")
async def root():
    """Endpoint raiz que retorna un saludo"""
    return {"message": "Tu mascota merece la mejor atencion"}
    