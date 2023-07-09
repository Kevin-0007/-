import glob,os
file_path = "/root/work/session"
xlsx_files = glob.glob(file_path + "/*.session")
ip_list=
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
    open(py_file,'w+').write(msg)
    print(i)
