import matplotlib.pyplot as plt
import seaborn as sns
# Graficar dispersión de redshift vs magnitud en banda u
plt.figure(figsize=(8, 6))
plt.scatter(dataset_filtrado['redshift'], dataset_filtrado['u'], alpha=0.6, color='blue')
plt.title('Redshift vs Magnitud en banda u')
plt.xlabel('Redshift')
plt.ylabel('Magnitud en banda u')
plt.grid(True)
plt.show()

# Graficar dispersión de redshift vs ascensión recta
plt.figure(figsize=(8, 6))
plt.scatter(dataset_filtrado['redshift'], dataset_filtrado['alpha'], alpha=0.6, color='green')
plt.title('Redshift vs Alpha')
plt.xlabel('Redshift')
plt.ylabel('Alpha')
plt.grid(True)
plt.show()

# Mapa de calor de la relación entre magnitudes u, redshift, y alpha
plt.figure(figsize=(8, 6))
sns.heatmap(dataset_filtrado[['redshift', 'u', 'alpha']].corr(), annot=True, cmap='coolwarm')
plt.title('Mapa de calor de correlación entre redshift, magnitud u y Alpha')
plt.show()
