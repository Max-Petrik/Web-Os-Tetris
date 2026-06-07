#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html

form = cgi.FieldStorage()

vorname = html.escape(form.getfirst("vorname", "").strip())
nachname = html.escape(form.getfirst("nachname", "").strip())
email = html.escape(form.getfirst("email", "").strip())

if vorname == "":
	vorname="not given"
if nachname == "":
	vorname="not given"
if email == "":
	vorname="not given"


print("Content-Type: text/html; charset=utf-8")
print()

print(f"""<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Profil</title>
	<link rel="stylesheet" href="../css/game.css" type="text/css">
</head>
<body>
	<div class="gameField">
		<form action="profile.cgi" method="post">
			<div class="btnDiv">
				<input type="hidden" name="vorname" value="{vorname}">
				<input type="hidden" name="nachname" value="{nachname}">
				<input type="hidden" name="email" value="{email}">
				<a href="http://pan.th-brandenburg.de/~petrik/cgi-bin/profile.cgi">
					<button>Profil</button>
				</a>
			</div>
		</form>
		<div class="iframeDiv">
			<iframe src="../tetris.html" width="100%" height="100%"></iframe>
		</div>
	</div>
</body>
</html>""")
