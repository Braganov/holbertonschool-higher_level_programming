#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to a JSON file.

    Args:
        csv_filename (str): The name of the CSV file to be converted.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open("data.json", "w", encoding='utf-8') as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        print(f"Le fichier '{csv_filename}' est introuvable")
        return False
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return False
