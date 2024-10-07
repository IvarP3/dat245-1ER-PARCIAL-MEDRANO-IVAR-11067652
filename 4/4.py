from sklearn.preprocessing import LabelEncoder
preprocesamiento = LabelEncoder()
nombres_clases = data['class'].unique()
etiquetado_simple = preprocesamiento.fit_transform(nombres_clases)
print(etiquetado_simple)




from sklearn.preprocessing import OneHotEncoder
preprocesamiento = OneHotEncoder()
nombres_clases2 = [[nombres_clases[0],3],
                [nombres_clases[1],1],
                [nombres_clases[2],2]]
etiquetado_binario = preprocesamiento.fit(nombres_clases2)
print(etiquetado_binario)
print(etiquetado_binario.categories_)
resultado = preprocesamiento.transform(nombres_clases2).toarray()
print(resultado)





from sklearn.preprocessing import KBinsDiscretizer

# Seleccionar las columnas numéricas
X = ['u', 'g', 'r', 'i', 'z', 'redshift', 'alpha', 'delta']

# discretización con 5 intervalos (bins)
preprocesamiento = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')

discretizacion = preprocesamiento.fit_transform(data[X])
print(discretizacion)





from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import MinMaxScaler
preprocesamiento = Normalizer()
normalizacion = preprocesamiento.fit_transform(data[X])
print(normalizacion)
preprocesamiento = MinMaxScaler()
normalizacion = preprocesamiento.fit_transform(data[X])
print(normalizacion)