#!/usr/bin/env python3

import cgi
import html

form = cgi.FieldStorage()

vorname = form.getfirst("vorname", "").strip()
nachname = form.getfirst("nachname", "").strip()
email = form.getfirst("email", "").strip()

print("Content-Type: text/html; charset=utf-8")
print()

print(f"""<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="../css/profile.css" type="text/css">
</head>
<body>
	<div class="wrapper">
		<div class="box">
			<div class="headline">
				<h1>Profil</h1>
			</div>
			<div class="data">
				<label>Vorname: {vorname}</label>
			</div>
			<div class="data";
				<label>Nachname: {nachname}</label>
			</div>
			<div class="data">
				<label>Email: {email}</label>
			</div>
			<div class="back">
				<form action="game.cgi" method="post">
					<input type="hidden" name="vorname" value="{vorname}">
					<input type="hidden" name="nachname" value="{nachname}">
					<input type="hidden" name="email" value="{email}">
					<a href="http://pan.th-brandenburg.de/~petrik/cgi-bin/game.cgi">
						<button>Zurück</button>
					</a>
				</form>
			</div>
		</div>
		<div class="gitHub">
			<a href="https://github.com/Max-Petrik/Web-Os-Tetris">
				<img src="../images/github_logo.png">
			</a>
		</div>
	</div>
</body>
</html>""")
