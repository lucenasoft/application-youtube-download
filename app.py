from pytube import YouTube

print('-='*30)
print('SEJA BEM VINDO')
print('-='*30)

download = 'S'

while download != 'N':
    url = str(input('Cole aqui a URL: '))
    yt = YouTube(url)
    validation_d = 'N'
    while validation_d == 'N':
        validation = str(input(f'Deseja baixar esse vídeo? {yt.title} [S/N] ')).upper()
        if validation == 'S':
            print("Downloading...")
            ys = yt.streams.get_highest_resolution()
            ys.download()
            validation_d = 'S'
        else:
            print('Tente novamente!')
            break
    download = str(input('Deseja baixar outros? [S/N]  ')).upper()
