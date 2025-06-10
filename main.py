import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

bairros = [
    "Nova Campinas",
    "Cambuí",
    "Barão Geraldo",
    "Taquaral",
    "Vila Industrial",
    "Jardim Proença",
    "Parque das Universidades",
    "Sousas",
    "Jardim Florence",
    "Campo Grande",
    "Bonfim",
    "Parque Taquaral",
]

dates = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")

def get_horario_pico(bairro):
    if "Industrial" in bairro: return np.random.choice(["13h-16h", "14h-17h"])
    elif "Parque" in bairro: return np.random.choice(["19h-22h", "20h-23h"])
    else: return np.random.choice(["17h-20h", "18h-21h", "19h-22h"])



def simular_clima(data):
    mes = data.month
    if mes in [12,1,2]:  # Verão
        temp = np.random.normal(28, 3)
        chuva = np.random.exponential(5) if np.random.rand() < 0.3 else 0
    elif mes in [6,7,8]:  # Inverno
        temp = np.random.normal(20, 2)
        chuva = np.random.exponential(2) if np.random.rand() < 0.1 else 0
    else:
        temp = np.random.normal(24, 2)
        chuva = np.random.exponential(3) if np.random.rand() < 0.2 else 0
    return temp, min(95, np.random.normal(75, 10)), chuva


dados = []
for data in dates:
    bairro = np.random.choice(bairros, p=[0.15,0.12,0.1,0.1,0.08,0.08,0.07,0.07,0.06,0.05,0.05,0.07])
    temp, umid, chuva = simular_clima(data)
    consumo_base = np.random.normal(400, 100)
    if data.month in [12,1,2]: consumo_base *= 1.25
    elif data.month in [6,7,8]: consumo_base *= 0.85
    if chuva > 20: consumo_base *= 0.9
    if data.weekday() >= 5: consumo_base *= 1.18
    dados.append([
        data.strftime("%d/%m/%Y"),
        int(np.clip(consumo_base, 250, 650)),
        bairro,
        get_horario_pico(bairro),
        round(temp,1),
        f"{int(umid)}%",
        round(chuva,1)
    ])

df = pd.DataFrame(dados, columns=["dia", "consumo", "bairro", "horario_pico", "temperatura", "umidade", "precipitacao"])
df.to_csv("consumo_campinas_2025_completo.csv", index=False, encoding="utf-8")

plt.figure(figsize=(12, 6))
sns.barplot(x='bairro', y='consumo', data=df, estimator=np.mean)
plt.title('Consumo Médio de Água por Bairro (2025)')
plt.xlabel('Bairro')
plt.ylabel('Consumo Médio (Litros)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()