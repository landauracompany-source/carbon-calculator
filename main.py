from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>산림 탄소 계산기</h2>
    <form action="/calculate" method="get">
        면적(ha): <input name="area"><br><br>
        단위재적(m3/ha): <input name="volume"><br><br>
        생장률(%): <input name="growth"><br><br>
        <button type="submit">계산</button>
    </form>
    """

@app.get("/calculate")
def calculate(area: float, volume: float, growth: float):
    carbon = area * volume * (growth/100) * 0.5
    return {"예상 탄소 흡수량(tCO2)": carbon}
