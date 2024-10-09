# ==================================
# Utilisation des bibliothèques numpy et matplotlib
# ==================================
import numpy as np
import matplotlib.pyplot as plt
# ==================================
# Problème I.1 : Formule mathématique
# ==================================
def formule_mathematique():
    x = (2 * (512 * np.cos((np.pi / 3) + 13**2))) / 127

    print(f"Formule mathématique : {x}")
# ==================================
# Problème I.2 : Echantillonnage d'une fonction
# ==================================
def echantillonnage_fonction():
    t = np.linspace(1, 10, 20)
    y = np.tan(np.sqrt((np.sin(10*t)**4) + np.cos(5 * t)**2))

    print(f"Echantillonnage d'une fonction :")
    for i in range(0, len(y), 2):
        print(f"{y[i]}, {y[i+1]}")
    # Tracer des courbes : matplotlib
    plt.figure(1)
    plt.title("Echantillonnage d'une fonction")
    plt.plot(t, y)
    plt.show()
# ==================================
# Problème I.3 : Regression linéaire
# ==================================
def regression_lineaire():
    # Paramètres de la droite
    a = 2
    b = -3
    # Création d'un array de 50 valeurs entre 0 et 10
    X = np.linspace(0, 10, 50) 
    # Equation de la droite 
    Y = a * X + b
    # Trace de la droite
    plt.figure(2)
    plt.plot(X, Y, color='red')
    # Ajout du bruit Gaussien centré de variance 2
    Y1 = Y + (np.random.randn(np.size(Y)) * np.sqrt(2))
    # Tracer avec plot
    plt.plot(X, Y1, 'b*')
    plt.title("Bruit Gaussien centré de variance 2")
    plt.legend(["Droite", "Bruit Gaussien"])
    plt.show()
# ==================================
# Problème I.3 : Calcul des coefficients de la droite de régression
# ==================================
def calcul_coefficient():
    # Paramètres de la droite
    a = 2
    b = -3
    # Création d'un array de 50 valeurs entre 0 et 10
    X = np.linspace(0, 10, 50) 
    # Equation de la droite 
    Y = a * X + b
    # Ajout du bruit Gaussien centré de variance 2
    Y1 = Y + (np.random.randn(np.size(Y)) * np.sqrt(2))
    # Construire la matrice A
    A = np.vstack([X, np.ones(len(X))]).T
    B = Y1
    # Calculer les coefficients a et b
    coefficients = np.linalg.inv(A.T @ A) @ A.T @ B
    A_estime, B_estime = coefficients
    # Tracer la droite estimée
    Y_estime = A_estime * X + B_estime
    # Trace de la droite estimée
    plt.figure(3)
    plt.plot(X, Y, label="Droite")
    plt.plot(X, Y1, label="Bruit Gaussien")
    plt.plot(X, Y_estime, label="Droite estimée")
    plt.title("Droite estimée")
    plt.legend(["Droite", "Bruit Gaussien", "Droite estimée"])
    plt.show()
# ==================================
# Problème I.3 : Calcul la variance de l'erreur d'approximation
# ==================================
def calcul_variance_erreur():
    # Paramètre de la droite
    a = 2
    b = -3
    # Création d'un array de 50 valeurs entre 0 et 10
    X = np.linspace(0, 10, 50) 
    # Equation de la droite 
    Y = a * X + b
    # Ajout du bruit Gaussien centré de variance 2
    Y1 = Y + (np.random.randn(np.size(Y)) * np.sqrt(2))
    # Construire la matrice A
    A = np.vstack([X, np.ones(len(X))]).T
    B = Y1
    # Calculer les coefficients a et b
    coefficients = np.linalg.inv(A.T @ A) @ A.T @ B
    A_estime, B_estime = coefficients
    # Tracer la droite estimée
    Y_estime = A_estime * X + B_estime
    # Calculer la variance de l'erreur d'approximation
    erreur = Y1 - Y_estime
    variance_erreur = np.var(erreur)
    variance_erreur_1 = (erreur.T @ erreur) / len(X)
    print(f"Variance de l'erreur d'approximation : {variance_erreur}")
    print(f"Variance de l'erreur d'approximation version 2: {variance_erreur_1}")
# ==================================
# Problème I.4 : Représentation une fonction à 2 paramètres
# ==================================
def representation_fonction():
    x = np.arange(-4, 4, 0.2)
    y = x
    X, Y = np.meshgrid(x, y)
    z = np.sinc(X) * np.sinc(Y)
    fig1 = plt.figure(1)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, z, cmap='viridis')
    fig2 = plt.figure(2)
    bx = plt.axes(projection='3d')
    bx.plot_wireframe(X, Y, z, color='black')
    plt.show()
# ==================================
# Problème I.4 : Représentation Gaussienne
# ==================================
def representation_gaussian():
    x = np.arange(-4, 4, 0.2)
    y = x
    X, Y = np.meshgrid(x, y)
    z = np.exp(-X**2 - Y**2)
    fig1 = plt.figure(1)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, z, cmap='viridis')
    fig2 = plt.figure(2)
    bx = plt.axes(projection='3d')
    bx.plot_wireframe(X, Y, z, color='black')
    plt.show()
# ==================================
# Problème I.5 : Découverte des fonctions mathématiques
# ==================================
def decouverte_fonctions_mathematiques():
    # while loop placeholder, complete or remove if not needed
    while True:
        print(f"1. Fonction mathématique : np.asin()")
        print(f"2. Fonction mathématique : np.acos()")
        print(f"3. Fonction mathématique : np.atan()")
        print(f"4. Fonction mathématique : np.abs()")
        print(f"5. Fonction mathématique : np.round()")
        print(f"6. Fonction mathématique : np.floor()")
        print(f"7. Fonction mathématique : np.ceil()")
        print(f"8. Quitter")

        choix = int(input("Choisir une fonction mathématique : "))
        if choix == 1:
            x = np.linspace(-1, 1, 100)
            y = np.asin(x)
            plt.plot(x, y)
            plt.title("Fonction mathématique : np.asin()")
            plt.show()
        elif choix == 2:
            x = np.linspace(-1, 1, 100)
            y = np.acos(x)
            plt.plot(x, y)
            plt.title("Fonction mathématique : np.acos()")
            plt.show()
        elif choix == 3:
            x = np.linspace(-1, 1, 100)
            y = np.atan(x)
            plt.plot(x, y)
            plt.title("Fonction mathématique : np.atan()")
            plt.show()
        elif choix == 4:
            x = np.linspace(-1, 1, 100)
            y = np.abs(x)
            plt.plot(x, y)
            plt.title("Fonction mathématique : np.abs()")
            plt.show()
        elif choix == 5:
            x = np.linspace(-1, 1, 100)
            y = np.round(x)
            plt.plot(x, y)
            plt.title("Fonction mathématique : np.round()")
            plt.show()
        elif choix == 6:
            x = np.linspace(-1, 1, 100)
            y = np.floor(x)
            plt.plot(x, y)
            plt.title("Fonction mathématique : np.floor()")
            plt.show()
        elif choix == 7:
            x = np.linspace(-1, 1, 100)
            y = np.ceil(x)
            plt.plot(x, y)
            plt.title("Fonction mathématique : np.ceil()")
            plt.show()
        elif choix == 8:
            print("Au revoir!")
            break
        else:
            print("Choix invalide!")
# ==================================
# Problème I.6 : Plus petite valeur
# ==================================
def petite_valeur_fonction():
    precision = 1.0
    count = 0
    for _ in range(1000):
        if 1.0 + precision == 1.0:
            break
        precision /= 10
        count += 1
    print(f"Le processeur peut gérer jusqu'à {count} décimales pour les nombres réels.")

if __name__ == "__main__":
    # formule_mathematique()
    # echantillonnage_fonction()
    # regression_lineaire()
    # calcul_coefficient()
    # calcul_variance_erreur()
    # representation_fonction()
    # representation_gaussian()
    # decouverte_fonctions_mathematiques()
    petite_valeur_fonction()
