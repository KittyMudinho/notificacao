from pushbullet import Pushbullet
API='INSERT YOUR API'
file='push.txt'
with open(file,mode='r') as f:
    text=f.read()
pb=Pushbullet(API)
push=pb.push_note('Primeira notificação.',text)