#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi   	 # Importiert das Modul cgi, um Formulardaten asuzulesen
import html	 # Importiert html, um Benutzerdaten auslesen zu können

form = cgi.FieldStorage()	# liest Daten aus html-formular

# liest die Nutzerdaten aus den jeweiligen Feldern aus
vorname = html.escape(form.getfirst("vorname", "").strip())
nachname = html.escape(form.getfirst("nachname", "").strip())
email = html.escape(form.getfirst("email", "").strip())

# Falls nichts übergeben wird, dann wird stattdessen not given eingesetzt
# dient jediglich zum debuggen, ist nicht für das Programm relevant
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
	<div class="gitHub">
		<a href="https://github.com/Max-Petrik/Web-Os-Tetris">
			<img src="../images/github_logo.png">
		</a>
	</div>

	<div class="gameField">

		<!-- Formular übermittelt Benutzerdaten an proile.cgi mittels html-post -->
		<form action="profile.cgi" method="post">
			<div class="btnDiv">

				<!-- hidden input speichert die daten und machet es möglich sie in profile.cgi wieder auszulesen -->
				<input type="hidden" name="vorname" value="{vorname}">
				<input type="hidden" name="nachname" value="{nachname}">
				<input type="hidden" name="email" value="{email}">

				<!-- button führt zu profile.cgi, wo Benutzerdaten angezeigt werden -->
				<button type="submit" onclick="window.location.href='http://pan.th-brandenburg.de/~petrik/cgi-bin/profile.cgi'">Profil</button>
			</div>
		</form>

		<!-- iframe fügt unsere seperate tetris(.html) ein  -->
		<div class="iframeDiv">
			<iframe src="../tetris.html" width="100%" height="100%"></iframe>
		</div>
	</div>
</body>
</html>""")
