#!/usr/bin/python3

# Importation des modules nécessaires
import http.server  # Module pour créer le serveur HTTP
import json  # Module pour gérer le format JSON

# Définition du gestionnaire des requêtes HTTP


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Méthode pour gérer les requêtes GET.
        Elle vérifie l'URL demandée et renvoie la réponse appropriée.
        """

        if self.path == "/":
            # Si l'URL est "/" -> on affiche un message simple
            self.send_response(200)  # Code HTTP 200 (OK)
            self.send_header("Content-type", "text/plain")  # Type de contenu
            self.end_headers()
            # Réponse en texte brut
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            # Si l'URL est "/data" -> on retourne des données JSON
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")  # Type JSON
            self.end_headers()
            # Conversion en JSON et encodage en bytes
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            # Si l'URL est "/status" -> on retourne "OK"
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "OK"}).encode("utf-8"))

        else:
            # Si l'URL n'est pas définie -> erreur 404
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(
                {"error": "Endpoint not found"}).encode("utf-8"))


def run(server_class=http.server.HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """
    Fonction pour démarrer le serveur HTTP.

    :param server_class: Classe du serveur HTTP (par défaut http.server.HTTPServer)
    :param handler_class: Classe du gestionnaire de requêtes (SimpleAPIHandler)
    :param port: Port d'écoute du serveur (par défaut 8000)
    """
    server_address = ("", port)  # Écoute sur toutes les interfaces réseau
    httpd = server_class(server_address, handler_class)
    print(f"✅ Serveur démarré sur http://localhost:{port}")
    httpd.serve_forever()  # Maintient le serveur actif


if __name__ == "__main__":
    run()  # Lancer le serveur
