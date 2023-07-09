import glob,os
file_path = r"C:\Users\admin\Desktop\live"
xlsx_files = glob.glob(file_path + "/*.session")
ip_list=['2404:8c80:0:1009:5c:e8f4:f8c0:2d3b','2404:8c80:0:1009:ce:1165:1d01:cb9c']
index=1
for i in xlsx_files:
    all=len(xlsx_files)
    ip=ip_list[0]
    if index>all/2:
        ip=ip_list[1]
    ii=i.replace(file_path,'/root/work')
    py_file=ii.replace('.session','.py')
    msg='from dj import work'+'\n'+'phone="'+i+'"\n'+'work(phone,'+ip+')'
    print(msg)
    index+=1
    #open(py_file,'a+').write(msg)
    #print(i)
