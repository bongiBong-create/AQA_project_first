import json
import os
import webbrowser

from api_client import get_photos
from tests.tests import check_status, check_object

tests = [check_status, check_object]

with open("handmade_allure/results.json", "w", encoding="utf-8") as f:
    results = []
    for test in tests:
        result = test(get_photos())
        results.append(result)

    json.dump(results, f, ensure_ascii=False, indent=4)

webbrowser.open(f"http://localhost:8000")