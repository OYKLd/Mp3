# Compresseur MP3

Outil simple pour compresser des fichiers MP3 en utilisant FFmpeg.

## Prérequis

- Python 3.6 ou supérieur
- FFmpeg installé et ajouté au PATH

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers
2. Créez un environnement virtuel :
   ```bash
   python -m venv venv
   ```
3. Activez l'environnement virtuel :
   - Sur Windows :
     ```
     .\venv\Scripts\activate
     ```
   - Sur macOS/Linux :
     ```bash
     source venv/bin/activate
     ```
4. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Installation de FFmpeg

1. Téléchargez FFmpeg depuis [ffmpeg.org](https://ffmpeg.org/download.html)
2. Installez-le en suivant les instructions pour votre système d'exploitation
3. Vérifiez l'installation avec :
   ```bash
   ffmpeg -version
   ```

## Utilisation

```bash
python compress.py fichierMp3.mp3 [options]
```

### Options
- `-o, --output` : Spécifiez un nom de fichier de sortie
- `-b, --bitrate` : Débit binaire (par défaut: 64k)
  - Valeurs courantes : 64k, 96k, 128k, 192k, 256k, 320k
  - Plus le chiffre est bas, plus la compression est importante

### Exemples

Compression avec les paramètres par défaut (64k) :
```bash
python compress.py fichierMp3.mp3
```

Compression avec un débit binaire spécifique :
```bash
python compress.py fichierMp3.mp3 -b 128k
```

Spécifier un fichier de sortie :
```bash
python compress.py fichierMp3 -o musique.mp3 -b 96k
```

## Fonctionnalités

- Compression de fichiers MP3 avec différents débits binaires
- Conservation des métadonnées
- Affichage des statistiques de compression
- Gestion des erreurs complète

## Auteur

Ouattara Yeo Kassahm Lydie
