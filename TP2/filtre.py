# utilisation de la bibliothèque numpy
import numpy as np
import matplotlib.pyplot as plt
# ==========================
# création de notre fonction filtre_passe_bas
def filtreExpotentielle(nombre_echantillons, signal_entree, alpha = 0.1):
    yn = np.zeros(nombre_echantillons)
    yn[0] = alpha * signal_entree[0]

    for n in range(1, nombre_echantillons):
        yn[n] = alpha * signal_entree[n] + (1 - alpha) * yn[n - 1]
    return yn

# ==========================
# Fonction de test
def fonctionTest(x):
    fx = 0.8 - (np.exp(-(pow((x - 3), 2) - 5) / 100) - np.sin(np.pi * ((x / 30) + 1)))
    return fx

# ==========================
# Animation d'un graph
def animation(x, fig, alpha=0.1):
    fig.clear()
    y = np.exp(-x) * np.cos(alpha * x)
    graph, = plt.plot(x, y)
    plt.axis([0, 5, -1, 1])
    plt.draw()