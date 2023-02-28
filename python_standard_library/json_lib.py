import json
from pathlib import Path

# movies = [
#     {"id":1, "title": "Terminator", "year": 1989},
#     {"id":2, "title": "Kindergarten Cop", "year": 1990}
#     # {"id":1, "title": "Terminator", "year": 1989},
# ]

# data = json.dumps(movies)
data = Path("movies.json").read_text()
print(data)
movies = json.loads(data)
print(movies[1]["title"])
