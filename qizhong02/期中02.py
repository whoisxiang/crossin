#coding:gbk
from random import randint

name = raw_input('�������������:')
while True:
    with open('game.txt','a+') as r:
        scores = {}
        lines = r.readlines()
        for l in lines:
            s = l.split()
            scores[s[0]] = s[1:]
        score = scores.get(name)
        if score is None:
            score = [0, 0, 0]
            game_times = int(score[0])
            min_times = int(score[1])
            total_times = int(score[2])
            print '��ӭ\t'
            print '��ӭ', name, '�״����棡'
        else:
            game_times = int(score[0])
            min_times = int(score[1])
            total_times = int(score[2])
            avg_times = float(total_times) / game_times
            print '��ӭ%sף����Ϸ��죡\n���Ѿ�����%d�Σ�����%d�ֲ³��𰸣�ƽ��%.2f�ֲ³���' % (name, game_times, min_times, avg_times)
    num = randint(1, 100)
    times = 1
    print '����Ǽ�',num
    bingo = False
    while bingo == False:
        while True:
            print '�� %d ��' % times
            answer = raw_input('������1-100������:')
            if answer.isdigit():
                answer=int(answer)
                if  1 <= answer <= 100:
                    print answer

                    # print times
                    if answer < num:
                        print '%d ̫С��!\n' % answer
                    if answer > num:
                        print '%d ̫����!\n' % answer
                    if answer == num:
                        print '�����ˣ����𰸾���%d \n' % answer
                        bingo = True
                        break
                    times += 1
            else:
                break
    total_times += times
    game_times += 1
    if game_times == 1:
        min_times = times
        avg_times = times
    else:
        avg_times=float(total_times)/game_times
    if  times < min_times:
        min_times = times
    scores[name] = [str(game_times), str(min_times), str(total_times)]
    print '��ϲ������˴𰸾���',num
    print '��һ������ %d ��\n��һ������%d����Ϸ\n��ƽ��%.2f�β��д�\n����õĳɼ���%d�Σ�\n' % (total_times, game_times, avg_times, min_times)
    result = ''
    for n in scores:
        line = n + ' ' + ' '.join(scores[n]) + '\n'
        result += line
    with open(r'game.txt', 'w') as outf:
        outf.write(result)
    g=raw_input('���롰go������һ�Σ������˳���Ϸ   ')
    if g=='go':
        print '����Ϸ'
        continue
    else:
        break
    break