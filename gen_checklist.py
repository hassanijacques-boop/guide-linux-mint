#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Checklist d'installation Linux Mint — à cocher avant de toucher au PC."""

import pathlib, asyncio

D = pathlib.Path("/workspace/guide-linux-mint")
D.mkdir(parents=True, exist_ok=True)

CSS = """
@page { size: A4 portrait; margin: 12mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", Arial, sans-serif; color: #1c2331; margin: 0;
  font-size: 8.3pt; line-height: 1.3; }
.pg { page-break-after: always; }
.pg:last-child { page-break-after: auto; }
.ent { border-bottom: 3px solid #12294d; padding-bottom: 8px; margin-bottom: 11px; }
.ent .t1 { font-size: 1.2rem; font-weight: 800; color: #12294d; }
.ent .t2 { font-size: .78rem; color: #5b6779; margin-top: 2px; }
h2 { font-size: .79rem; letter-spacing: .6px; text-transform: uppercase; color: #12294d;
  border-bottom: 2px solid #e2e8f0; padding-bottom: 3px; margin: 9px 0 5px;
  page-break-after: avoid; }
.chk { display: grid; gap: 2px; margin: 4px 0 6px; }
.chk .i { display: flex; gap: 7px; align-items: flex-start; font-size: .79rem;
  background: #fbfcfe; border: 1px solid #e2e8f0; border-radius: 6px; padding: 3px 8px;
  page-break-inside: avoid; }
.chk .b { flex: 0 0 14px; height: 14px; border: 1.8px solid #2563eb; border-radius: 3px; margin-top: 2px; }
.chk .b.r { border-color: #c0392b; }
.chk .c { flex: 1; }
.chk .c b { color: #12294d; }
.chk .c .s { color: #5b6779; font-size: .73rem; }
.alerte { background: #fef2f2; border: 1px solid #fecaca; border-left: 4px solid #c0392b;
  border-radius: 8px; padding: 6px 10px; font-size: .77rem; margin: 5px 0; color: #7f1d1d; }
.info { background: #eff6ff; border: 1px solid #bfdbfe; border-left: 4px solid #2563eb;
  border-radius: 8px; padding: 6px 10px; font-size: .77rem; margin: 5px 0; }
.vert { background: #f0fdf4; border: 1px solid #bbf7d0; border-left: 4px solid #1a7a4a;
  border-radius: 8px; padding: 6px 10px; font-size: .77rem; margin: 5px 0; }
.or { background: #fffbeb; border: 1px solid #fde68a; border-left: 4px solid #b8860b;
  border-radius: 8px; padding: 6px 10px; font-size: .77rem; margin: 5px 0; }
table { width: 100%; border-collapse: collapse; font-size: .76rem; margin: 5px 0; }
th { background: #12294d; color: #fff; padding: 6px 8px; text-align: left; font-size: .66rem;
  text-transform: uppercase; letter-spacing: .4px; }
td { border-bottom: 1px solid #e2e8f0; padding: 4px 7px; vertical-align: top; }
tr { page-break-inside: avoid; }
.et { display: flex; gap: 8px; border: 1px solid #e2e8f0; border-left: 4px solid #2563eb;
  border-radius: 7px; padding: 4px 9px; margin-bottom: 3px; page-break-inside: avoid; }
.et .n { flex: 0 0 20px; height: 20px; border-radius: 50%; background: #2563eb; color: #fff;
  font-weight: 800; font-size: .68rem; display: flex; align-items: center; justify-content: center; }
.et .c { flex: 1; font-size: .78rem; }
.et .c b { color: #12294d; }
.et .d { flex: 0 0 76px; text-align: right; font-size: .7rem; color: #5b6779; font-weight: 700; }
"""

def ent(t1, t2):
    return '<div class="ent"><div class="t1">%s</div><div class="t2">%s</div></div>' % (t1, t2)

def chk(items, rouge=False):
    out = '<div class="chk">'
    for titre, sous in items:
        cls = "b r" if rouge else "b"
        s = '<div class="s">%s</div>' % sous if sous else ""
        out += '<div class="i"><div class="%s"></div><div class="c"><b>%s</b>%s</div></div>' % (cls, titre, s)
    return out + "</div>"

# ─────────── PAGE 1 : SAUVEGARDER ───────────
P1 = ent("AVANT TOUT : SAUVEGARDER", "Ce qui sera effacé et qui ne se récupère pas") + """
<div class="alerte">
  <b>⚠️ L'installation efface TOUT le disque.</b> Bureau, Documents, Images, Vidéos, Téléchargements,
  et toutes les applications installées. <b>Une fois effacé, il n'y a pas de retour en arrière.</b>
</div>
<h2>1 · Ce que je sauvegarde — à cocher</h2>
""" + chk([
    ("Photos et vidéos personnelles", "Bureau · Images · Vidéos · Téléchargements · pellicule du téléphone"),
    ("Papiers administratifs scannés", "impôts · CAF/CSSM · assurances · actes de naissance · bulletins de salaire"),
    ("Documents de l'école", "préparations · évaluations · livrets · emplois du temps · dossiers d'élèves"),
    ("Fichiers de travail", "Word · Excel · PDF · présentations"),
    ("Carnet de contacts", "et numéros importants"),
    ("Signets du navigateur", "⚠️ Firefox et Chrome : <b>exporter les favoris</b> — sinon perdus"),
    ("Mots de passe enregistrés dans le navigateur", "⚠️ les <b>exporter</b> avant, ou vérifier qu'ils sont dans un gestionnaire"),
    ("Musique et films personnels", "pas ceux achetés en ligne : ils se retéléchargent"),
]) + """
<div class="alerte">
  <b>⚠️ Ce qui n'est PAS récupérable après l'installation</b>
</div>
""" + chk([
    ("Les applications Windows installées", "Word, Photoshop… il faudra les remplacer — voir la liste page 3"),
    ("Les sauvegardes de jeux", "si tu y tiens, copie le dossier de sauvegarde"),
    ("Les emails téléchargés en local", "si tu utilises Outlook en local, <b>exporte le .pst</b>"),
    ("Les fichiers chiffrés (BitLocker)", "sans la clé de récupération, ils sont perdus pour toujours"),
], rouge=True) + """
<div class="alerte" style="background:#fff1f1">
  <b>🔑 La clé de licence Windows</b> — note-la si tu penses revendre le PC un jour.
  Elle est dans le BIOS ou via un logiciel de lecture de clé. <b>Après l'installation, elle n'est plus accessible.</b>
</div>
<h2>2 · Où je sauvegarde — et jamais un seul endroit</h2>
<div class="info">
  <b>Règle : deux supports différents.</b> Un disque externe <b>et</b> un cloud (Drive, OneDrive),
  ou un disque externe <b>et</b> une seconde clé USB.<br>
  <b>⚠️ Attention :</b> la clé USB qui servira à installer Linux <b>sera effacée</b>. Ne mets pas ta
  sauvegarde dessus.
</div>
""" + chk([
    ("Disque externe branché et vérifié", "je rouvre 3 fichiers au hasard pour vérifier qu'ils s'ouvrent"),
    ("Deuxième copie faite ailleurs", "cloud, autre disque, ou clé USB différente"),
    ("Le disque <b>Y:</b> des vidéos de formation", "⚠️ <b>ON N'Y TOUCHE PAS</b> — il est protégé, le guide ne l'efface pas"),
])

# ─────────── PAGE 2 : LE JOUR J ───────────
P2 = ent("LE JOUR J — DANS L'ORDRE", "Compte 1 h 30 devant toi, sans être pressé") + """
<div class="or">
  <b>⭐ L'étape qui protège tout : TESTER EN « LIVE » AVANT D'INSTALLER.</b><br>
  Une clé Linux Mint permet de <b>démarrer sur le système sans rien installer</b>.
  Tu vérifies que le Wi-Fi, le son, l'écran et le clavier fonctionnent — <b>et si ça ne marche pas,
  tu retires la clé et Windows redémarre normalement, sans aucune perte.</b>
</div>
<h2>Les 8 étapes</h2>
<div class="et"><div class="n">1</div><div class="c"><b>Vérifier le matériel</b> — 4 Go de RAM minimum (8 recommandé), 25 Go de disque libre, et note le <b>modèle exact du PC</b>.</div><div class="d">10 min</div></div>
<div class="et"><div class="n">2</div><div class="c"><b>Dernière sauvegarde</b> — refais-la juste avant. C'est celle-là qui compte.</div><div class="d">15 min</div></div>
<div class="et"><div class="n">3</div><div class="c"><b>Télécharger l'ISO</b> Linux Mint 22.3 Cinnamon depuis <b>linuxmint.com</b> (le site officiel, pas un lien de forum).</div><div class="d">20 min</div></div>
<div class="et"><div class="n">4</div><div class="c"><b>Vérifier l'empreinte</b> du fichier téléchargé <i>(le guide page 4 explique la commande exacte)</i>. <b>Ne saute pas cette étape.</b></div><div class="d">5 min</div></div>
<div class="et"><div class="n">5</div><div class="c"><b>Créer la clé USB</b> avec <b>Rufus</b> — clé de 4 à 16 Go. <b>⚠️ Jamais un disque de 500 Go : Rufus efface tout ce qu'il trouve.</b></div><div class="d">15 min</div></div>
<div class="et"><div class="n">6</div><div class="c"><b>Démarrer sur la clé</b> — touche F2 / F12 / Échap au démarrage selon la marque du PC.</div><div class="d">5 min</div></div>
<div class="et"><div class="n">7</div><div class="c">⭐ <b>TESTER EN LIVE</b> — Wi-Fi · son · écran · clavier · clé USB · souris. <b>Rien n'est installé à ce stade.</b></div><div class="d">10 min</div></div>
<div class="et"><div class="n">8</div><div class="c"><b>Installer</b> seulement si tout marche en live. Sinon : tu retires la clé, tu redémarres, Windows est intact.</div><div class="d">20 min</div></div>

<h2>À vérifier pendant le test en live — si un seul échoue, on ne va pas plus loin</h2>
""" + chk([
    ("Le <b>Wi-Fi</b> se connecte", "c'est le point n°1 qui pose problème — s'il ne marche pas, on règle le pilote avant d'installer"),
    ("Le <b>son</b> sort des haut-parleurs", "et le casque"),
    ("L'<b>écran</b> est net, à la bonne résolution", "pas de bandes, pas de flou"),
    ("Le <b>clavier</b> tape les accents", "é à ç ù — indispensable pour toi"),
    ("La <b>souris / le pavé tactile</b> répond", "y compris le clic droit"),
    ("Une <b>clé USB</b> est reconnue", "branche-la et ouvre-la"),
    ("Le <b>PC ne chauffe pas et ne s'éteint pas</b>", "10 minutes en live suffisent à voir"),
])

# ─────────── PAGE 3 : APRÈS ───────────
P3 = ent("APRÈS L'INSTALLATION", "Les 4 réglages à faire tout de suite, et les équivalents de tes logiciels") + """
<h2>1 · Les 4 choses à faire dans les 30 premières minutes</h2>
""" + chk([
    ("<b>Connecter le Wi-Fi</b>", "icône en bas à droite de l'écran"),
    ("<b>Installer toutes les mises à jour</b>", "Menu → Mises à jour. Peut prendre 15 à 30 min. <b>Ne coupe pas.</b>"),
    ("⭐ <b>Activer TIMESHIFT</b>", "c'est l'assurance-vie du système : des points de restauration. <b>Le guide page 9 explique comment.</b>"),
    ("<b>Vérifier les pilotes</b>", "Menu → Gestionnaire de pilotes : Wi-Fi, carte graphique"),
]) + """
<div class="vert">
  <b>✅ Si Timeshift est activé</b>, tu peux casser quelque chose sans stress : tu reviens
  20 minutes en arrière. <b>C'est ce qui fait la différence entre « j'ai essayé Linux » et
  « j'utilise Linux depuis deux ans ».</b>
</div>
<h2>2 · Tes logiciels Windows et leurs équivalents</h2>
<table>
  <tr><th style="width:36%">Sur Windows</th><th>Sur Linux Mint</th><th style="width:22%">Où le trouver</th></tr>
  <tr><td>Word</td><td><b>LibreOffice Writer</b> — lit et enregistre les .docx</td><td>déjà installé</td></tr>
  <tr><td>Excel</td><td><b>LibreOffice Calc</b></td><td>déjà installé</td></tr>
  <tr><td>PowerPoint</td><td><b>LibreOffice Impress</b></td><td>déjà installé</td></tr>
  <tr><td>Chrome / Edge</td><td><b>Firefox</b> (installé) ou <b>Chromium</b></td><td>déjà installé</td></tr>
  <tr><td>Photos / visionneuse</td><td><b>Xviewer</b></td><td>déjà installé</td></tr>
  <tr><td>Lecteur PDF</td><td><b>Xreader</b> — et LibreOffice</td><td>déjà installé</td></tr>
  <tr><td>Bloc-notes</td><td><b>Xed</b></td><td>déjà installé</td></tr>
  <tr><td>WhatsApp</td><td>WhatsApp Web, ou l'application via <b>Flatpak</b></td><td>logiciels</td></tr>
  <tr><td>Zoom / Teams</td><td>version Linux sur leur site, ou dans le navigateur</td><td>site officiel</td></tr>
  <tr><td>Antivirus</td><td><b>pas nécessaire</b> — et ClamAV si tu veux quand même</td><td>logiciels</td></tr>
</table>
<h2>3 · Ce que je vérifie avant de dire « c'est bon »</h2>
""" + chk([
    ("Le PC démarre normalement, sans la clé USB", "retire la clé et redémarre"),
    ("Le Wi-Fi se reconnecte tout seul", "après un redémarrage"),
    ("Le son marche", "teste une vidéo"),
    ("Je retrouve <b>tous mes fichiers sauvegardés</b>", "recopie-les dans Documents, Images, Vidéos"),
    ("L'imprimante fonctionne", "si tu en as une — sinon, on verra plus tard"),
    ("Un point <b>Timeshift</b> est créé", "vérifie dans le menu Timeshift"),
]) + """
<div class="or">
  <b>📌 La règle d'or : ne fais qu'UNE chose à la fois.</b><br>
  Si quelque chose ne marche pas, <b>arrête-toi et fais une photo de l'écran</b>.
  La photo dit tout : le message exact, l'étape, l'écran. Avec ça, je te débloque en une réponse.
</div>
"""

html = ('<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">'
        '<title>Checklist installation Linux Mint</title><style>' + CSS + '</style>'
        '</head><body>'
        '<div class="pg">' + P1 + '</div>'
        '<div class="pg">' + P2 + '</div>'
        '<div class="pg">' + P3 + '</div>'
        '</body></html>')

(D / "checklist.html").write_text(html, encoding="utf-8")
print("  ✅ checklist.html — %d Ko" % (len(html) // 1024))


async def pdf():
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        p = await b.new_page()
        await p.goto("file://%s/checklist.html" % D, wait_until="load")
        await p.wait_for_timeout(700)
        await p.pdf(path=str(D / "CHECKLIST_INSTALLATION_LINUX_MINT.pdf"),
                    format="A4", print_background=True)
        await b.close()

asyncio.run(pdf())
import fitz
f = D / "CHECKLIST_INSTALLATION_LINUX_MINT.pdf"
d = fitz.open(f)
print("  ✅ %s — %d pages — %d Ko" % (f.name, d.page_count, f.stat().st_size // 1024))
for i in range(d.page_count):
    d[i].get_pixmap(dpi=105).save("/tmp/ck_p%d.png" % (i + 1))
