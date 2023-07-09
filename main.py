import glob,os,random,time
import datetime
def main():
    all_file = glob.glob("/root/work/" + "/*.py")
    ii=1
    x = []
    for i in range(0,len(all_file)):
        x.append(i)
    random.shuffle(x)
    starttime = datetime.datetime.now()
    for i in x:
        if all_file[i]=='/root/work/main.py' or all_file[i]=='/root/work/dj.py':
            pass
        else:
            print(ii,all_file[i])
            os.system('python '+all_file[i])
            ii+=1
            time.sleep(random.randint(666,888))
    endtime = datetime.datetime.now()
    print('---------------------------------')
    print ('run time',endtime - starttime)
    print('totle user:',len(glob.glob("/root/work/" + "/*.py")))
    print('---------------------------------')

main()
