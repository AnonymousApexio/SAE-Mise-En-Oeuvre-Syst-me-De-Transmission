import math

class Point:
    """Classe définissant un point"""
    
    def __init__(self, x=0.0, y=0.0):
        """
        Constructeur de la classe Point
        Args:
            x (float): Coordonnée x, 0 par défaut
            y (float): Coordonnée y, 0 par défaut
        """
        self.x = x
        self.y = y
    
    def distanceCoordonnee(self, x, y):
        """
        Calcule la distance entre ce point et des coordonnées données
        Args:
            x (float): Coordonnée x du point cible
            y (float): Coordonnée y du point cible
        Returns:
            float: Distance entre les points
        """
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)
    
    def distancePoint(self, camarade):
        """
        Calcule la distance entre ce point et un autre point
        Args:
            camarade (Point): Autre point
        Returns:
            float: Distance entre les points
        """
        return self.distanceCoordonnee(camarade.x, camarade.y)
    
    def __str__(self):
        """Représentation textuelle du point"""
        return f"Point({self.x}, {self.y})"


class Cercle:
    """Classe représentant un cercle géométrique"""
    
    def __init__(self, rayon, centre=None):
        """
        Constructeur de la classe Cercle
        Args:
            rayon (float): Rayon du cercle
            centre (Point, optional): Centre du cercle. Par défaut Point(0,0)
        """
        self.rayon = rayon
        self.centre = centre if centre is not None else Point()
    
    def diametre(self):
        """Calcule le diamètre du cercle"""
        return 2 * self.rayon
    
    def perimetre(self):
        """Calcule le périmètre du cercle"""
        return 2 * math.pi * self.rayon
    
    def surface(self):
        """Calcule la surface du cercle"""
        return math.pi * self.rayon**2
    
    def intersection(self, autreCercle):
        """
        Vérifie si ce cercle intersecte un autre cercle
        Args:
            autreCercle (Cercle): Autre cercle à tester
        Returns:
            bool: True si intersection, False sinon
        """
        distance_centres = self.centre.distancePoint(autreCercle.centre)
        return distance_centres <= (self.rayon + autreCercle.rayon)
    
    def appartient(self, point):
        """
        Vérifie si un point est à l'intérieur du cercle
        Args:
            point (Point): Point à tester
        Returns:
            bool: True si le point est dans le cercle
        """
        return self.centre.distancePoint(point) <= self.rayon
    
    def __str__(self):
        """Représentation textuelle du cercle"""
        return f"Cercle(centre={self.centre}, rayon={self.rayon})"


class Rectangle:
    """Classe représentant un rectangle"""
    
    def __init__(self, *args):
        """
        Constructeur de la classe Rectangle
        Trois modes:
        - Rectangle(): point (0,0), longueur=1, hauteur=1
        - Rectangle(point, longueur, hauteur)
        - Rectangle(point_bg, point_hd): calcul longueur et hauteur
        """
        if len(args) == 0:
            # Constructeur par défaut
            self.pointBasGauche = Point()
            self.longueur = 1.0
            self.hauteur = 1.0
        elif len(args) == 3:
            # Constructeur avec point, longueur, hauteur
            self.pointBasGauche = args[0]
            self.longueur = args[1]
            self.hauteur = args[2]
        elif len(args) == 2:
            # Constructeur avec deux points
            self.pointBasGauche = args[0]
            point_haut_droit = args[1]
            self.longueur = point_haut_droit.x - self.pointBasGauche.x
            self.hauteur = point_haut_droit.y - self.pointBasGauche.y
    
    def surface(self):
        """Calcule la surface du rectangle"""
        return self.longueur * self.hauteur
    
    def perimetre(self):
        """Calcule le périmètre du rectangle"""
        return 2 * (self.longueur + self.hauteur)
    
    def getBasGauche(self):
        """Retourne le point bas-gauche"""
        return self.pointBasGauche
    
    def getBasDroit(self):
        """Retourne le point bas-droit"""
        return Point(self.pointBasGauche.x + self.longueur, self.pointBasGauche.y)
    
    def getHautGauche(self):
        """Retourne le point haut-gauche"""
        return Point(self.pointBasGauche.x, self.pointBasGauche.y + self.hauteur)
    
    def getHautDroit(self):
        """Retourne le point haut-droit"""
        return Point(self.pointBasGauche.x + self.longueur, 
                    self.pointBasGauche.y + self.hauteur)
    
    def contient(self, p):
        """
        Vérifie si un point est à l'intérieur du rectangle
        Args:
            p (Point): Point à tester
        Returns:
            bool: True si le point est dans le rectangle
        """
        return (self.pointBasGauche.x <= p.x <= self.pointBasGauche.x + self.longueur and
                self.pointBasGauche.y <= p.y <= self.pointBasGauche.y + self.hauteur)
    
    def __str__(self):
        """Représentation textuelle du rectangle"""
        return f"Rectangle(bg={self.pointBasGauche}, l={self.longueur}, h={self.hauteur})"


class TriangleRectangle:
    """Classe représentant un triangle rectangle"""
    
    def __init__(self, cote1, cote2, angle_droit=None):
        """
        Constructeur de la classe TriangleRectangle
        
        Args:
            cote1 (float): Premier côté adjacent à l'angle droit
            cote2 (float): Deuxième côté adjacent à l'angle droit  
            angle_droit (Point, optional): Point de l'angle droit. Par défaut Point(0,0)
        """
        self.cote1 = cote1
        self.cote2 = cote2
        self.angle_droit = angle_droit if angle_droit is not None else Point()
    
    def hypotenuse(self):
        """
        Calcule la longueur de l'hypoténuse
        
        Returns:
            float: Longueur de l'hypoténuse
        """
        return math.sqrt(self.cote1**2 + self.cote2**2)
    
    def perimetre(self):
        """
        Calcule le périmètre du triangle
        
        Returns:
            float: Périmètre du triangle
        """
        return self.cote1 + self.cote2 + self.hypotenuse()
    
    def surface(self):
        """
        Calcule la surface du triangle
        
        Returns:
            float: Surface du triangle
        """
        return (self.cote1 * self.cote2) / 2
    
    def est_isocèle(self):
        """
        Vérifie si le triangle est isocèle (deux côtés égaux)
        
        Returns:
            bool: True si le triangle est isocèle, False sinon
        """
        return math.isclose(self.cote1, self.cote2, rel_tol=1e-9)
    
    def __str__(self):
        """Représentation textuelle du triangle rectangle"""
        return f"TriangleRectangle(cote1={self.cote1}, cote2={self.cote2}, angle_droit={self.angle_droit})"


def main():
    """Fonction principale pour tester toutes les classes"""
    
    print("=== TEST DE LA CLASSE POINT ===")
    p1 = Point()
    p2 = Point(3, 4)
    print(f"p1: {p1}")
    print(f"p2: {p2}")
    print(f"Distance p1-p2: {p1.distancePoint(p2):.2f}")
    
    print("\n=== TEST DE LA CLASSE CERCLE ===")
    c1 = Cercle(5)
    c2 = Cercle(2, p2)
    print(f"c1: {c1}")
    print(f"c2: {c2}")
    print(f"Périmètre de c1: {c1.perimetre():.2f}")
    print(f"Surface de c2: {c2.surface():.2f}")
    print(f"Intersection c1-c2: {c1.intersection(c2)}")
    print(f"c1 contient p2: {c1.appartient(p2)}")
    
    print("\n=== TEST DE LA CLASSE RECTANGLE ===")
    r1 = Rectangle()
    r2 = Rectangle(Point(1, 1), 4, 3)
    r3 = Rectangle(Point(1, 1), Point(4, 5))
    print(f"r1: {r1}")
    print(f"r2: {r2}")
    print(f"r3: {r3}")
    print(f"Surface de r2: {r2.surface()}")
    print(f"Périmètre de r3: {r3.perimetre()}")
    print(f"Points de r2: BG={r2.getBasGauche()}, BD={r2.getBasDroit()}, HG={r2.getHautGauche()}, HD={r2.getHautDroit()}")
    print(f"r2 contient p2: {r2.contient(p2)}")
    
    print("\n=== TEST DE LA CLASSE TRIANGLE RECTANGLE ===")
    t1 = TriangleRectangle(3, 4)
    t2 = TriangleRectangle(5, 5, Point(2, 3))
    print(f"t1: {t1}")
    print(f"t2: {t2}")
    print(f"Hypoténuse t1: {t1.hypotenuse():.2f}")
    print(f"Périmètre t1: {t1.perimetre():.2f}")
    print(f"Surface t1: {t1.surface():.2f}")
    print(f"t1 est isocèle: {t1.est_isocèle()}")
    print(f"t2 est isocèle: {t2.est_isocèle()}")


if __name__ == "__main__":
    main()