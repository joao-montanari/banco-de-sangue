import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.barplot(x='bairro', y='consumo', data=df, estimator=np.mean)
plt.title('Consumo Médio de Água por Bairro (2025)')
plt.xlabel('Bairro')
plt.ylabel('Consumo Médio (Litros)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()