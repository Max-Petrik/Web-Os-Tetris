#!/usr/bin/env python3

import cgi	# Importiert das Modul cgi, um Formulardaten auszulesen
import html	# Importiert html, um Benutzerdaten auslesen zu können

form = cgi.FieldStorage()	# liest Daten aus html-formular

# liest die Nutzerdaten aus den jeweiligen Feldern aus
vorname = form.getfirst("vorname", "").strip()
nachname = form.getfirst("nachname", "").strip()
email = form.getfirst("email", "").strip()

print("Content-Type: text/html; charset=utf-8")
print()

print(f"""<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="UTF-8">
	<title>Profile</title>
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
			<div class="data">
				<label>Nachname: {nachname}</label>
			</div>
			<div class="data">
				<label>Email: {email}</label>
			</div>
			<div class="back">

				<!-- Formular übermittelt Benutzerdaten mittels html-post an game.cgi zurück -->
				<form action="game.cgi" method="post">

					<!-- hidden input speichert die daten und macht es möglich sie in profile.cgi wieder auszulesen -->
					<input type="hidden" name="vorname" value="{vorname}">
					<input type="hidden" name="nachname" value="{nachname}">
					<input type="hidden" name="email" value="{email}">

					<!-- button führt zu profile.cgi, wo Benutzerdaten gespeichert werden, damit sie nicht verloren gehen -->
					<button type="submit" onclick="window.location.href='http://pan.th-brandenburg.de/~petrik/cgi-bin/game.cgi'">Zurück</button>
				</form>
			</div>
		</div>

		<!-- -->
		<div class="gitHub">
			<a href="https://github.com/Max-Petrik/Web-Os-Tetris">
				<img src="../images/github_logo.png" alt="Error">
			</a>
		</div>
	</div>
</body>
</html>""")
