from fastapi import FastAPI
import Optimo
app = FastAPI()
#http://127.0.0.1:8000

@app.get("/home/{numVar}/{numDes}/{tipoOpt}/{coeficientesFO}/{coeficientesDes}/{valoresIndependientes}")
def index(numVar:int, numDes:int,tipoOpt:str,coeficientesFO:str,coeficientesDes:str,valoresIndependientes:str):
    #return {"numVar": numVar, "numDes": numDes, "tipoOpt": tipoOpt, "coeficientesFO":coeficientesFO,"coeficientesDes": coeficientesDes, "valoresIndependientes": valoresIndependientes }
    return Optimo.simplex(numVar,numDes,tipoOpt, coeficientesFO, coeficientesDes,valoresIndependientes)

