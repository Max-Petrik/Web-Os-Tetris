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
	<title>Profil</title>
	<link rel="stylesheet" href="../css/profile.css" type="text/css">
</head>
<body>
	<div class="gameField">
		<iframe src="../game.html" width="100%"></iframe>
	</div>
</body>
</html>""")
