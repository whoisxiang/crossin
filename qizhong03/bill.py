#coding:gbk
import time,linecache
while True:
    print "1.����;2.����"
    c = raw_input('��ѡ�����:')
    if c.isdigit():
        try:
            c=int(c)
            if c==1:
                print '����ģʽ\n1.��ѯ���ʮ�ʽ��׼�¼\n2.��ѯ��ĳ��˾��������\n3.��ѯ����ʲ���ծ״��'
                cc=input('��ѡ���ѯ��Ŀ:')
                if cc==1:
                    print '\n'.join(linecache.getlines('��ˮ�˵�.txt')[-8:])
            elif c==2:
                print "����ģʽ"
                ob = raw_input('���׶���:')
                sr = str(input('����/��'))
                zc = str(input('֧��/��'))
                ys = str(input('Ӧ���˿�/��'))
                yc = str(input('Ӧ���ʿ�/��'))
                line='\n'+ob+'\t'+sr+'\t'+zc+'\t'+ys+'\t'+yc+'\t'+time.strftime('%Y-%m-%d',time.localtime())
                print line
                with open(r'��ˮ�˵�.txt','a') as jz:
                    jz.write(line)

        except:
            print '�������'
            continue
    else:
        continue
