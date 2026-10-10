import pygame
pygame.init()
pygame.mixer.init()
songs={"Lover Without A Heart": "CG5 - Lover Without A Heart (SPOTISAVER).mp3", "Artificial Suicide": "ARTIFICIAL SUICIDE.mp3", "Pain": "Pain_spotdown.app.mp3"}
TitleFont=pygame.font.Font(None, 40)
InfoFont=pygame.font.Font(None, 15)
screen=pygame.display.set_mode((600, 600))
running=True
pygame.time.set_timer(pygame.USEREVENT+1, 1)
playbacktime=0
status="Paused"
requests=[]
targetsong="None"
def handle_song_request(song):
    songdir=songs[song]
    pygame.mixer.music.load(songdir)
    if song!=targetsong:
        requests.append("Switch")
        requests.append("Play")
    else:
        if status=="Paused":
            requests.append("Play")
        elif status=="Playing":
            requests.append("Pause")
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.USEREVENT+1:
            if status=="Playing":
                playbacktime+=1
        if event.type==pygame.MOUSEBUTTONDOWN:
            for num, song in enumerate(songs):
                if pygame.Rect(20, 20+num*150, 300, 120).collidepoint(*pygame.mouse.get_pos()):
                    handle_song_request(song)
                    targetsong=song
    screen.fill((255, 255, 255))
    for request in requests:
        if request=="Play":
            pygame.mixer.music.play(start=playbacktime/1000)
            status="Playing"
        if request=="Pause":
            pygame.mixer.music.stop()
            status="Paused"
        if request=="Switch":
            playbacktime=0
    requests=[]
    for num, song in enumerate(songs):
        pygame.draw.rect(screen, (230, 230, 230), pygame.Rect(20, 20+num*150, 300, 120))
        screen.blit(TitleFont.render(song, True, (0, 0, 0)), (30, 30+num*150))
        if song==targetsong:
            if status=="Paused":
                pygame.draw.circle(screen, (200, 200, 200), [290, 110+num*150], 20)
            if status=="Playing":
                pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(270, 90+num*150, 40, 40))
    screen.blit(InfoFont.render(f"The current song is:{targetsong}", True, (0, 0, 0)), (320, 20))
    pygame.display.flip()