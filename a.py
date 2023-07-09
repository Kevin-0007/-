import glob,os
file_path = "/root/work/session"
xlsx_files = glob.glob(file_path + "/*.session")
ip_list=['2404:8c80:0:1007:1f:a279:4446:b6f3','2404:8c80:0:1007:dd:1fa5:7de0:9d01']
index=1
for i in xlsx_files:
    all=len(xlsx_files)
    ip=ip_list[0]
    if index>all/2:
        ip=ip_list[1]
    ii=i.replace(file_path,'/root/work')
    py_file=ii.replace('.session','.py')
    msg='from dj import work'+'\n'+'phone="'+i+'"\n'+'work(phone,"'+ip+'")'
    index+=1
    open(py_file,'a+').write(msg)
    print(i)
