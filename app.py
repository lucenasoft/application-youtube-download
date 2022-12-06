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
            resolucoes = int(input('Verifique as resoluções do vídeo disponive e digite a escolhida: [EX: 480, 720, 1080]  '))
            yt.streams.filter(resolution=f'{resolucoes}p',progressive=True, file_extension='mp4').first().download()
            validation_d = 'S'
        else:
            print('Tente novamente!')
            break
    download = str(input('Deseja baixar outros? [S/N]  ')).upper()



    