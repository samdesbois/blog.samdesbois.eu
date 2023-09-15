Title: Comment installer son blog Pelican
Date: 2023-08-14
Modified: 2023-08-15
Category: Informatique
Tags: python, web, blog, apache2
Summary: Installation d'une application de blog sur serveur apache2.

## Pourquoi Pelican ?

J'utilise [**Pelican**](https://getpelican.com/) (version 4.8) car c'est un *CMS* écrit en **python**. C'est un langage que j'aime étudier actuellement. Je vais pouvoir ainsi mettre en pratique mes connaissances si je souhaite créer un plugin avec ce CMS.
> CMS est l'acronyme de Content Management System, c'est-à-dire système de gestion de contenu. Il s'agit d'un logiciel en ligne grâce auquel il est possible de créer, de gérer et de modifier facilement un site web, sans avoir besoin de connaissances techniques en langage informatique. ~ https://www.salesforce.com/fr/resources/articles/definition-cms/

De plus il utilise les fichiers au format markdown pour pouvoir écrire les articles. C'est ainsi plus facile de conserver lezs érits que je peux produire. Ce n'est pas dépendand d'un CMS. Il suffit, par exemple, de conserver les fichier .md dans son cloud préféré.

## Créer répertoire sur serveur distant avec les bons droits

J'ai déjà *apache2* d'installé sur mon ordinateur. Je crée d'abor le répertoire qui va acceuiilir le site :

```sh
cd /var/www/html
sudo mkdir toto.samdesbois.eu
sudo chown -R www-data:www-data toto.samdesbois.eu/
```

L'utilisateur *www-data* est un utilisateur virtuel utilisé par apache2. Il faut ajouter l'utilisateur au groupe du même nom www-data et donner les droits d'écriture au répertoire créer pour le membres de ce groupe. La première commande est pour vérifier que nous sommes ou non dans le groupe www-data.

```sh
getent group www-data
sudo usermod -a -G www-data mon-nom-utilisateur
sudo chmod -R g+w toto.samdesbois.eu/
```

## Installer Pelican sur sa machine locale

C'est une subtilité que je n'ai pas comprise tout de suite. Pour des raisons de sécurité, il faut évidemment installer pelican sur la machine du quotidien par cette simple ligne de commande me concernant :

```
python3 -m pip install "pelican[markdown]"
```

Donc vous avez bien compris qu'on écrit cela dans le terminal de son ordinateur personnel et non sur le serveur où les pages html seront acessibles en permanence !

Vous créez le répertoire localement par exemple par ces commandes :

```
mkdir -p ~/pelican-cms-projects/toto.samdesbois.eu
cd ~/pelican-cms-projects/toto.samdesbois.eu
pelican-quickstart
```

Lorsque vous lancez le dernier script, vous avez à répondre à des questions pour faciliter l'installation et surtout la gestion future du site. Renseignez bien avevc les bon paramètres comme votre nom d'utilisateur au serveur distant qui a accès au groupe www-data si vous avez bien suivi et le chemin complet vers le répertoire où sera présent le site. Valider la création du script *make* qui permettra la gestion facile. Vous pouvez utiliser personnellement plusieurs protocole pour uploader le site une fois qu'il y a une modification. Je choisis personnellement `rsync`.

> **rsync** (pour remote synchronization ou synchronisation à distance), est un logiciel de synchronisation de fichiers. Il est fréquemment utilisé pour mettre en place des systèmes de sauvegarde distante... ~ source : https://doc.ubuntu-fr.org/rsync

Je vous recopie ce dialogue :

```
> Where do you want to create your new web site? [.] 
> What will be the title of this web site? Le Blog de toto
> Who will be the author of this web site? toto
> What will be the default language of this web site? [en] fr
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) 
> What is your URL prefix? (see above example; no trailing slash) https://toto.samdesbois.eu
> Do you want to enable article pagination? (Y/n) 
> How many articles per page do you want? [10] 
> What is your time zone? [Europe/Rome] 
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) 
> Do you want to upload your website using FTP? (y/N) 
> Do you want to upload your website using SSH? (y/N) y
> What is the hostname of your SSH server? [localhost] blog.samdesbois.eu
> What is the port of your SSH server? [22] 
> What is your username on that server? [root] mon-nom-utilisateur
> Where do you want to put your web site on that server? [/var/www] /var/www/toto.samdesbois.eu
> Do you want to upload your website using Dropbox? (y/N) 
> Do you want to upload your website using S3? (y/N) 
> Do you want to upload your website using Rackspace Cloud Files? (y/N) 
> Do you want to upload your website using GitHub Pages? (y/N) 
Done. Your new project is available at /Users/mon-nom-utilisateursamson/p
```

Vous pouvez maintenant écrire votre premier article (un fichier .md que vous placez dans le répertoire *content*). Le nom du fichier est ce qui apparaîtra dans la barre d'adress. Voici donc mon fichier mon-super-titre.md :

```
Title: Mon super titre
Date: 2023-01-01 10:20
Category: Tuto

Ceci est du texte.
```

Et si tout s'est bien passé le site sera actualisé vers le répertoire à distance par la simple commande :

```
make rsync_upload
```

Vous pouvez vérifier dans le répertoir du site sur serveur distant que les fichiers sont bien là avec la commande `ls -lh`.

## Rediriger son nom de domaine vers le site

Il convient maintenant d'utiliser son nom de domaine pour que tout le monde puisse accéder au site.

Vous avez déjà redirigé le nom de domaine vers l'ip du serveur distant.

Il faut ensuite se rendre dans le serveur distant pour créer les *virtual hosts* pour Apache2 avec le certificat SSL. On va tout d'abord créer un *virtual host* classique, c'est à dire sans certification :

```
cd /etc/apache2/sites-available/
sudo vim toto.samdesbois.eu.conf
```

Et dans ce fichier on écrit l'équivalent de ma configuration (à chaque fois changer avec vos paramètres à vous) :

```
<VirtualHost *:80>
    ServerName toto.samdesbois.eu
    ServerAlias toto.samdesbois.eu 
    ServerAdmin super@email.com
    DocumentRoot /var/www/html/toto.samdesbois.eu
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
RewriteEngine on
RewriteCond %{SERVER_NAME} =toto.samdesbois.eu
RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>
```

 On va créer les liens symboliques et redémarrer apache2 pour que le lien soit effectif et on redémarre le programme apache2 :
 
```
sudo a2ensite toto.samdesbois.eu.conf
sudo systemctl reload apache2
```

Et là on dit merci au programme `certbot`[^1] qui permet de créer son *virtual host* avec certificat *SSL* facilement et surtout gratuitement car j'ai vu que certaines entreprises qui facturent ce service.

```
sudo apt install certbot
sudo certbot --apache
```

Vous pouvez ouvrir le fichier *toto.samdesbois.eu-le-ssl.conf* pour voir ce qui a été fait mais surtout teste votre site à l'adresse choisie (pour moi sur https://toto.samdesbois.eu/).

## Conclusion

Ce petit tutoriel me permet de sauvegarder les recherches que j'ai pu faire durant une partie de mon week-end pour pouvoir installer le programme Pelican qui je l'espère me donnera du plaisir à ridiger des textes sans avoir trop de distraction lors de l'écriture. Il y a plein d'avantages à utiliser ce site qui est gratuit et modifiable sans autorisation.

Cela permet également d'héberger son propre site sur son serveur. J'utilise personnellement un VPS qui me coûte 4 euros par mois, mais vous pouvez-tout à fait héberger ce site sur un petit serveur qui tourne chez vous.

[^1]: [doc.ubuntu-fr.org/tutoriel/securiser_apache2_avec_ssl](https://doc.ubuntu-fr.org/tutoriel/securiser_apache2_avec_ssl)

