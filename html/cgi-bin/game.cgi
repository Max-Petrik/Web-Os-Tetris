#!/usr/bin/env python3

import cgi
import html

form = cgi.FieldStorage()

vorname = html.escape(form.getfirst("fvorname", "").strip())
nachname = html.escape(form.getfirst("fnachname", "").strip())
email = html.escape(form.getfirst("femail", "").strip())

print("Content-Type: text/html; charset=utf-8")
print()

print(f"""<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Profil</title>
	<link rel="stylesheet" href="../css/profile.css" type="text/css">
</head>
<body>
	<div class="gameField">
		<div class="btnDiv">
			<button>Profil</button>
		</div>
		<div class="iframeDiv">
			<iframe src="../game.html" width="100%" height="100%"></iframe>
		</div>
	</div>
</body>
</html>""")
