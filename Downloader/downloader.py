import pytube

def download_video(link):
    pytube.YouTube(link).streams.get_highest_resolution().download()

if __name__ == "__main__":
    link = input("Digite o link do vídeo: ")
    download_video(link)