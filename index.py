from pushbullet import Pushbullet
API='o.wg7W2sSSDOZVX2IItEhIuSzwXNTg3IRQ'
file='push.txt'
with open(file,mode='r') as f:
    text=f.read()
pb=Pushbullet(API)
push=pb.push_note('Primeira notificação.',text)