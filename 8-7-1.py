#coding:gbk
from random import randint
game=r'E:\OPS\����\pylearn\crossin\game.txt'
name=raw_input('�������������:')
with open(game) as r:
    scores={}
    lines=r.readlines()
    for l in lines:
        s=l.split()
        scores[s[0]]=s[1:]
    score=scores.get(name)
    if score is None:
        score=[0,0,0]
    game_times = int(score[0])
    min_times = int(score[1])
    total_times = int(score[2])
if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0
print type(game_times),type(min_times),type(avg_times)
print '%s,���Ѿ�����%d�Σ�����%d�ֲ³��𰸣�ƽ��%.2f�ֲ³���' % (name,game_times,min_times,avg_times)
num = randint(1,100)
times =0
print 'Guess what i think?'
bingo = False
while bingo == False:
    times += 1
    answer = input()
    if answer < num:
        print 'too small!'
    if answer > num:
        print 'too big!'
    if answer == num:
        print 'BINGO!'
        bingo=True
if game_times ==0 or times < min_times:
    min_times = times
total_times += times
game_times += 1
scores[name]=[str(game_times),str(min_times),str(total_times)]
result=''
for n in scores:
    line=n+' '+' '.join(scores[n])+'\n'
    result += line
                        
#result = '%d %d %d'%(game_times,min_times,total_times)
with open(r'E:\OPS\����\pylearn\crossin\game.txt','w') as outf:
    outf.write(result)
