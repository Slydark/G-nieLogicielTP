# ==========================
# Séance II - Python, numpy, matplotlib
# ==========================
# ==================================
# Utilisation des bibliothèques numpy et matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import scipy.optimize as opt
# ==================================
# ==========================
# appelle de la fonction filtreExpotentielle
# from filtre import filtreExpotentielle
import filtre
# ==========================
# ==========================
# Problème II.1 : Passe-bas à réponse impulsionnelle exponentielle
# ==========================
# Vu que le programme qu'on va crée pour nous habituer à utiliser les fonctions 
# dans un autre fichier que la main.py puis l'appeler dans le main.py
# je saute cette partie pour la faire dans le fichier filtre.py
# ==========================
def passeBas():
    # Initialisation des paramètres
    alpha = 0.5
    delta_t = 0.01
    nombre_echantillons = 1000

    temps = np.arange(0, nombre_echantillons * delta_t, delta_t)
    signale = 1.9 * np.sin(5 * temps) + 1.5 * np.sin(11 * temps) + 1.7 * np.sin(2.3 * temps)
    signale += np.sqrt(0.3) * np.random.randn(np.size(temps))

    signale_filtre = filtre.filtreExpotentielle(nombre_echantillons, signale, alpha)

    plt.figure()
    plt.plot(signale, label="Signal d'entrée bruité")
    plt.plot(signale_filtre, label="Signal de sortie")
    plt.legend()
    plt.show()
# ==========================
# Problème II.3 : Recherche du minimum d'une fonction
# ==========================
def minFunction():
    x = np.linspace(-20, 20, 400)
    x_test = filtre.fonctionTest(x)
    result = opt.fmin(filtre.fonctionTest, -10)
    plt.figure()
    plt.plot(x_test, label="Signal résultant")
    plt.show()
    print(f"Resultat : {result}")
# ==========================
# Problème II.4 : Titres et légendes 1/2
# ==========================
def titresLegendes():
    t = np.arange(0, 10, 0.1)
    x = np.sin(np.pi * t)
    y = np.sinc(np.pi * t)
    z = np.cos(np.pi * t)

    plt.figure()
    plt.plot(t, x, label="sinus")
    plt.plot(t, y, label="sinc")
    plt.plot(t, z, label="cosinus")
    plt.title("3 signaux")
    plt.xlabel("Temps")
    plt.ylabel("Valeur du signal")
    plt.legend()
    plt.show()
# ==========================
# Problème II.4 : Titres et légendes 2/2
# ==========================
def titresLegendes2():
    t = np.arange(0, 10, 0.1)
    signals = [
        np.sin(np.pi * t),
        np.sinc(np.pi * t),
        np.cos(np.pi * t)
    ]
    labels = {
        0: "sinus",
        1: "sinc",
        2: "cosinus"
    }

    fig, axs = plt.subplots(3, 1, figsize=(8, 12))
    fig.suptitle("3 signaux")

    for i, signal in enumerate(signals):
        axs[i].plot(t, signal, label=labels[i])
        axs[i].set_xlabel("Temps")
        axs[i].set_ylabel("Valeur du signal")
        axs[i].legend()

    plt.tight_layout()
    plt.show()
# ==========================
# Problème II.5 : Animation d'un graphique
# ==========================
def animationGraphique():
    fig = plt.figure()
    x = np.arange(0, 5, 0.01)

    filtre.animation(x, fig)

    alpha_vals = np.hstack((np.linspace(1, 10, 30), np.linspace(10, 1, 30)))
    anim = ani.FuncAnimation(fig, filtre.animation, alpha_vals, interval=50)
    plt.show()
# ==========================
# Problème II.6 : Calculs de moments en 2D 1/2
# ==========================
def moments2D():
    a = 2
    b = -3
    x = np.random.randn(200)
    y = a * x + b + np.random.randn(np.size(x))

    plt.figure()
    plt.plot(x, y, '.')
    plt.axis('equal')
    plt.show()
# ==========================
# Problème II.6 : Calculs de moments en 2D 2/2
# ==========================
def anime2D():
    # Génération des points aléatoires
    a = 2
    b = -3
    x = np.random.randn(200)
    y = a * x + b + np.random.randn(np.size(x))

    # Création de la matrice A
    A = np.outer(x, y)

    # Calcul du barycentre
    x0 = np.mean(x)
    y0 = np.mean(y)

    # Affichage des résultats
    print("Matrice A :\n", A)
    print("Barycentre (x0, y0) : (", x0, ",", y0, ")")

    # Visualisation du nuage de points
    plt.figure(1)
    plt.plot(x, y, 'o')
    plt.axis('equal')
    plt.title('Nuage de points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

if __name__ == "__main__":
    # passeBas()
    # minFunction()
    # titresLegendes()
    # titresLegendes2()
    # animationGraphique()
    moments2D()