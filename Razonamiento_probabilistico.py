# Modelado de Incertidumbre
# Supongamos que estamos tratando de diagnosticar una enfermedad rara.

# Elemento 2: Redes Bayesianas
# Supongamos que tenemos información previa y condicional sobre la enfermedad y sus síntomas.
# Probabilidad de tener la enfermedad P(D)
p_disease = 0.01

# Probabilidad de presentar síntomas dados la enfermedad P(S|D)
p_symptoms_given_disease = 0.95

# Probabilidad de presentar síntomas sin la enfermedad P(S|¬D)
p_symptoms_without_disease = 0.1

# Elemento 3: Inferencia Probabilística
# Supongamos que un paciente presenta síntomas. Queremos calcular la probabilidad de que tenga la enfermedad.

# Usamos la regla de Bayes
p_disease_given_symptoms = (p_symptoms_given_disease * p_disease) / ((p_symptoms_given_disease * p_disease) + (p_symptoms_without_disease * (1 - p_disease)))

# Elemento 1: Modelado de Incertidumbre
print(f"Elemento 1: Modelado de Incertidumbre\n")
print(f"Probabilidad de tener la enfermedad P(D) = {p_disease:.2f}")

# Elemento 2: Redes Bayesianas
print(f"\nElemento 2: Redes Bayesianas\n")
print(f"Probabilidad de presentar síntomas dados la enfermedad P(S|D) = {p_symptoms_given_disease:.2f}")
print(f"Probabilidad de presentar síntomas sin la enfermedad P(S|¬D) = {p_symptoms_without_disease:.2f}")

# Elemento 3: Inferencia Probabilística
print(f"\nElemento 3: Inferencia Probabilística\n")
print(f"Probabilidad de tener la enfermedad dado que presenta síntomas P(D|S) = {p_disease_given_symptoms:.2f}")
