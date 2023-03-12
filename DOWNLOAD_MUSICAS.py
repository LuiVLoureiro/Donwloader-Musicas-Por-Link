import os
from pytube import YouTube
import moviepy.editor
import re 

generos = ['Rock', 'Pop', 'Rap', 'Funk', 'Jazz', 'Blues', 'Sertanejo', 'Reggae', 'Classica', 'Favoritos', 'Dormir', 'Thayna']


class Downloader:
    def __init__(self):
        pass

    
    def save_to_temporary_file(new_file_name):
        with open(f'temporaria/variavel.txt', 'w') as file:
            file.write(new_file_name)

    

    def main():
        # criar pasta musicas caso ela não exista
        if not os.path.exists("musicas"):
            os.mkdir("musicas")

        # solicitar link do vídeo
        video_link = input('Digite o link do vídeo para baixar: ')

        # buscar o vídeo no YouTube
        video_id = video_link.split('v=')[1]
        video = YouTube('https://www.youtube.com/watch?v=' + video_id)

        # selecionar o melhor stream disponível em mp3
        video_stream = video.streams.get_by_itag(140)

        # baixar o vídeo
        video_stream.download(output_path='musicas/')

        # renomear o arquivo baixado e trocar os espaços por "_"
        global nome_musica
        new_file_name = re.sub(' ', '_', video_stream.default_filename)
        os.rename(f"musicas/{video_stream.default_filename}", f"musicas/{new_file_name}")

        # converter o vídeo para mp3
        clip = moviepy.editor.AudioFileClip(f"musicas/{new_file_name}")
        clip.write_audiofile(f"musicas/{video_id}.mp3")

        # renomear o arquivo convertido e excluir o arquivo mp4
        os.rename(f"musicas/{video_id}.mp3", f"musicas/{new_file_name.split('.mp4')[0]}.mp3")
        os.remove(f"musicas/{new_file_name}")

        # Solicitar gênero de música
        genero = input('Escolha o gênero da música (1 - Rock, 2 - Pop, 3 - Rap, 4 - Funk, 5 - Jazz, 6 - Blues, 7 - Sertanejo, 8 - Reggae, 9 - Clássica, 10 - Favoritos, 11 - Dormir, 12- Thayna): ')

        # Criar pasta com o nome do gênero de música
        if not os.path.exists(f"musicas/{generos[int(genero)-1]}"):
            os.mkdir(f"musicas/{generos[int(genero)-1]}")

        # Mover o arquivo de música para dentro da pasta do gênero
        os.rename(f"musicas/{new_file_name.split('.mp4')[0]}.mp3", f"musicas/{generos[int(genero)-1]}/{new_file_name.split('.mp4')[0]}.mp3")

        # Mensagem de confirmação
        print(f"Música baixada e adicionada na playlist {generos[int(genero)-1]}")


        Discord = input('Quer Enviar ao Discord? 1 - Sim, 2 - Não: ')

        if Discord == '1':
            # Criar pasta temporaria caso ela não exista
            if not os.path.exists("temporaria"):
                os.mkdir("temporaria")
            # Copiar o arquivo de música para dentro da pasta temporaria
            os.system(f"copy musicas\\{generos[int(genero)-1]}\\{new_file_name.split('.mp4')[0]}.mp3 temporaria\\{new_file_name.split('.mp4')[0]}.mp3")
            Downloader.save_to_temporary_file(new_file_name)
            os.system("python3 MUSICA_DISCORD.py")
            pasta = 'temporaria'
            for root, dirs, files in os.walk(pasta, topdown=False):
                    for name in files:
                        os.remove(os.path.join(root, name))
                    for name in dirs:
                        os.rmdir(os.path.join(root, name))
            os.rmdir('temporaria')
            os.system('cls')
            print("Música enviada para o Discord")
        else:
            print("Música não foi enviada para o Discord")



Downloader.main()
        