# Diccionario de Datos

## Trastornos Neurocognitivos y Demencia en América Latina e Iberoamérica (2000-2025)

### prevalencia_demencia.csv
| Campo | Tipo | Descripción |
|-------|------|-------------|
| pais | string | País |
| año | integer | Año |
| prevalencia_pct | float | % de prevalencia en mayores de 60 |
| casos_estimados | integer | Número de casos estimados |

### factores_riesgo.csv
| Campo | Tipo | Descripción |
|-------|------|-------------|
| factor | string | Factor de riesgo |
| tipo | string | Modificable/No modificable |
| odds_ratio | float | Razón de odds |
| evidencia | string | Nivel de evidencia |

### acceso_diagnostico.csv
| Campo | Tipo | Descripción |
|-------|------|-------------|
| pais | string | País |
| neurologos_per_100k | float | Neurólogos por 100.000 hab |
| tiempo_diagnostico_meses | float | Tiempo medio hasta diagnóstico |
| cobertura_seguro_pct | float | % con cobertura de seguro |

### tendencias_temporales.csv
| Campo | Tipo | Descripción |
|-------|------|-------------|
| año | integer | Año (2000-2025) |
| casos_nuevos | integer | Casos nuevos por año |
| mortalidad_pct | float | Tasa de mortalidad asociada |