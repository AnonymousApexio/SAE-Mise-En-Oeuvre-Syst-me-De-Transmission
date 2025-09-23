# SAE-Mise-En-Oeuvre-Syst-me-De-Transmission
Projet lié à la création d'un dispositif embarqué

Diagramme de la partie web de l'application:
```
  /var/www/html/prise-intelligente/
  ├── index.html                 # Page principale
  ├── login.html                # Page de connexion
  ├── css/
  │   └── style.css            # Styles CSS
  ├── js/
  │   ├── main.js              # JavaScript principal
  │   └── auth.js              # Gestion authentification
  ├── php/
  │   ├── auth.php             # Authentification
  │   ├── commande.php         # Commandes des prises
  │   ├── plages_horaires.php  # Gestion plages horaires
  │   └── temperature.php      # Données température
  └── config/
      └── plages.json          # Configuration plages horaires
```
