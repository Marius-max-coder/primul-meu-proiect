from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def parse_numbered_list(file_path):
    items = []
    lines = file_path.read_text(encoding="utf-8").splitlines()

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith("==="):
            continue

        if ". " not in line:
            continue

        number, item = line.split(". ", 1)

        if number.isdigit() and item.strip():
            items.append(item.strip())

    return items


def render_html_list(items):
    return "\n".join(f"      <li>{item}</li>" for item in items)


def build_site():
    fructe_file = ROOT / "fructe.txt"
    legume_file = ROOT / "legume.txt"

    fructe = parse_numbered_list(fructe_file)
    legume = parse_numbered_list(legume_file)

    html = f"""<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lista mea de fructe si legume</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      max-width: 900px;
      margin: 40px auto;
      padding: 0 20px;
      background: #f7f7f7;
      color: #222;
    }}
    .card {{
      background: white;
      border-radius: 12px;
      padding: 24px;
      margin-bottom: 20px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
    }}
    h1 {{ color: #2c3e50; }}
    h2 {{ color: #16a085; }}
    li {{ margin-bottom: 8px; }}
    footer {{
      margin-top: 30px;
      color: #666;
      font-size: 14px;
    }}
  </style>
</head>
<body>
  <div class="card">
    <h1>Proiect demo CI/CD</h1>
    <p>Site generat automat din GitHub Actions.</p>
  </div>

  <div class="card">
    <h2>🍎 Fructe</h2>
    <ul>
{render_html_list(fructe)}
    </ul>
  </div>

  <div class="card">
    <h2>🥦 Legume</h2>
    <ul>
{render_html_list(legume)}
    </ul>
  </div>

  <footer>
    Build automat din GitHub Actions.
  </footer>
</body>
</html>
"""
    site_dir = ROOT / "site"
    site_dir.mkdir(exist_ok=True)

    output_file = site_dir / "index.html"
    output_file.write_text(html, encoding="utf-8")
    return output_file


if __name__ == "__main__":
    output = build_site()
    print(f"Site generat cu succes: {output}")