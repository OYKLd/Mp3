import os
import sys
import subprocess
import argparse

def compress_mp3_ffmpeg(input_file, output_file, bitrate='64k'):
    """
    Compresse un fichier MP3 en utilisant FFmpeg directement
    """
    try:
        # Vérifier si le fichier source existe
        if not os.path.exists(input_file):
            print(f"Erreur: Le fichier {input_file} n'existe pas.")
            return False
            
        # Vérifier si FFmpeg est installé
        try:
            subprocess.run(['ffmpeg', '-version'], 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE)
        except FileNotFoundError:
            print("Erreur: FFmpeg n'est pas installé ou n'est pas dans le PATH.")
            print("Veuillez installer FFmpeg depuis https://ffmpeg.org/download.html")
            return False
            
        # Compression avec FFmpeg
        cmd = [
            'ffmpeg',
            '-i', input_file,
            '-codec:a', 'libmp3lame',
            '-b:a', bitrate,
            '-ar', '44100',  # Fréquence d'échantillonnage standard
            '-ac', '2',      # Stéréo
            '-y',            # Écraser le fichier de sortie s'il existe
            output_file
        ]
        
        print(f"Compression en cours de {input_file}...")
        result = subprocess.run(cmd, 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE,
                              text=True)
        
        if result.returncode != 0:
            print("Erreur lors de la compression:")
            print(result.stderr)
            return False
            
        # Afficher les informations de compression
        if os.path.exists(output_file):
            original_size = os.path.getsize(input_file) / (1024 * 1024)  # Mo
            compressed_size = os.path.getsize(output_file) / (1024 * 1024)  # Mo
            ratio = (1 - (compressed_size / original_size)) * 100
            
            print("\nCompression réussie !")
            print(f"Fichier original : {original_size:.2f} Mo")
            print(f"Fichier compressé : {compressed_size:.2f} Mo")
            print(f"Taux de compression : {ratio:.1f}% d'économie d'espace")
            return True
        else:
            print("Erreur: Le fichier compressé n'a pas été créé.")
            return False
            
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Compresseur de fichiers MP3 utilisant FFmpeg')
    parser.add_argument('input', help='Fichier MP3 source')
    parser.add_argument('-o', '--output', help='Fichier de sortie (optionnel)')
    parser.add_argument('-b', '--bitrate', default='64k', 
                      help='Débit binaire (ex: 64k, 96k, 128k, 192k, 256k, 320k)')
    
    args = parser.parse_args()
    
    # Vérifier que le fichier source existe
    if not os.path.exists(args.input):
        print(f"Erreur: Le fichier source {args.input} n'existe pas.")
        sys.exit(1)
    
    # Déterminer le fichier de sortie
    if not args.output:
        filename, ext = os.path.splitext(args.input)
        args.output = f"{filename}_compressed{ext}"
    
    # Lancer la compression
    success = compress_mp3_ffmpeg(args.input, args.output, args.bitrate)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
