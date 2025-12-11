# =================================  TESTY  ===================================
# Testy do tego pliku obejmują jedynie weryfikację poprawności wyników dla
# prawidłowych danych wejściowych - obsługa niepoprawych danych wejściowych
# nie jest ani wymagana ani sprawdzana. W razie potrzeby lub chęci można ją 
# wykonać w dowolny sposób we własnym zakresie.
# =============================================================================
import numpy as np


def chebyshev_nodes(n: int = 10) -> np.ndarray | None:
    if n <= 0:
        return None
    k = np.arange(0, n)
    nodes = np.cos(k * np.pi / (n - 1))
    return nodes

    #nie rozumiem dlaczego jak byk pisze poniżej, że funkcja sortuje od najmniejszego do największego a testy sprawdzają wyniki od największego do najmniejszego
    """Funkcja generująca wektor węzłów Czebyszewa drugiego rodzaju (n,) 
    i sortująca wynik od najmniejszego do największego węzła.

    Args:
        n (int): Liczba węzłów Czebyszewa.
    
    Returns:
        (np.ndarray): Wektor węzłów Czebyszewa (n,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    pass


def bar_cheb_weights(n: int = 10) -> np.ndarray | None:
    if n <= 0:
        return None
    delta_j = np.ones(n)
    delta_j[0] = 0.5
    delta_j[-1] = 0.5
    weights = ((-1) ** np.arange(n)) * delta_j
    return weights
    """Funkcja tworząca wektor wag dla węzłów Czebyszewa wymiaru (n,).

    Args:
        n (int): Liczba wag węzłów Czebyszewa.
    
    Returns:
        (np.ndarray): Wektor wag dla węzłów Czebyszewa (n,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    pass


def barycentric_inte(
    xi: np.ndarray, yi: np.ndarray, wi: np.ndarray, x: np.ndarray
) -> np.ndarray | None:
    try:
        xi = np.asarray(xi)
        yi = np.asarray(yi)
        wi = np.asarray(wi)
        x = np.asarray(x)
    except Exception:
        return None

    
    if xi.shape != yi.shape or xi.shape != wi.shape:
        return None 
    Y = []
    
    for val in x:
        mask = np.isclose(val, xi, atol=1e-14)

        if np.any(mask):   
            Y.append(yi[mask][0])
        else:
           
            diff = val - xi
            l_vec = wi / diff 
            numerator = yi @ l_vec  
            denominator = np.sum(l_vec) 
            
            Y.append(numerator / denominator)

    return np.array(Y)
    

    """Funkcja przeprowadza interpolację metodą barycentryczną dla zadanych 
    węzłów xi i wartości funkcji interpolowanej yi używając wag wi. Zwraca 
    wyliczone wartości funkcji interpolującej dla argumentów x w postaci 
    wektora (n,).

    Args:
        xi (np.ndarray): Wektor węzłów interpolacji (m,).
        yi (np.ndarray): Wektor wartości funkcji interpolowanej w węzłach (m,).
        wi (np.ndarray): Wektor wag interpolacji (m,).
        x (np.ndarray): Wektor argumentów dla funkcji interpolującej (n,).
    
    Returns:
        (np.ndarray): Wektor wartości funkcji interpolującej (n,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    pass


def L_inf(
    xr: int | float | list | np.ndarray, x: int | float | list | np.ndarray
) -> float | None:
    
    return np.max(np.abs(np.array(xr) - np.array(x)))


    """Funkcja obliczająca normę L-nieskończoność. Powinna działać zarówno na 
    wartościach skalarnych, listach, jak i wektorach biblioteki numpy.

    Args:
        xr (int | float | list | np.ndarray): Wartość dokładna w postaci 
            skalara, listy lub wektora (n,).
        x (int | float | list | np.ndarray): Wartość przybliżona w postaci 
            skalara, listy lub wektora (n,).

    Returns:
        (float): Wartość normy L-nieskończoność.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    pass
