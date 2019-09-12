#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py





os.getcwd()                          #获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")                  #改变当前脚本工作目录；相当于shell下cd
os.curdir                            #返回当前目录: ('.')
os.pardir                            #获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')     #可生成多层递归目录
os.removedirs('dirname1')            #若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')                  #生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')                  #删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')                #列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()                          #删除一个文件
os.rename("oldname","newname")       #重命名文件/目录
os.stat('path/filename')             #获取文件/目录信息
os.sep                               #输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep                           #输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep                           #输出用于分割文件路径的字符串
os.name                              #输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")            #运行shell命令，直接显示
os.environ                           #获取系统环境变量
os.path.abspath(path)                #返回path规范化的绝对路径
os.path.split(path)                  #将path分割成目录和文件名二元组返回
os.path.dirname(path)                #返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)               #返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)                 #如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)                  #如果path是绝对路径，返回True
os.path.isfile(path)                 #如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)                  #如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)               #返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)               #返回path所指向的文件或者目录的最后修改时间

>> > import os               #导入模块
>> > os.getcwd()             #获取当前工作目录
'/root'
>> > os.chdir("/tmp")        #切换工作目录，相当于shell的cd /tmp
>> > os.getcwd()
'/tmp'
>> > os.curdir               #返回当前目录（.）
'.'
>> > os.pardir               #返回上一级目录(..)
'..'
>> > os.makedirs("dirname1/dirname2/dirname3")             #创建多级目录，相当shell里的mkdir -p参数
>> > os.removedirs("dirname1/dirname2/dirname3")           #若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
>>> os.mkdir("dirname")                                    # 创建单个目录，相当于shell中的mkdir dirname
>> > os.rmkdir("dirname")                                  #删除单个空目录，如果目录里有文件或数据，则无法删除
>> > os.getcwd()
'/tmp'
>> > os.listdir("dirname")                                 #列出指定目录下的所有的文件和子目录，包括隐藏文件，并以列表方式打印出来
['a.html']
>> > os.listdir()                                          #列出指定目录下的所有的文件和子目录，包括隐藏文件，并以列表方式打印出来
['.Test-unix', '.font-unix', '.XIM-unix', '.ICE-unix', '.X11-unix',
 'systemd-private-0922d2b0d23c4a9fbb9427020fbe7bc1-chronyd.service-0kuGwG', 'dirname']

>> > os.stat("dirname")                                   #获取目录或文件信息
os.stat_result(st_mode=16877, st_ino=100872385, st_dev=64768, st_nlink=2, st_uid=0, st_gid=0, st_size=20,
               st_atime=1566960224, st_mtime=1566960149, st_ctime=1566960149)

>> > os.rename("dirname", "dirname1")                     #重命名文件或目录
>> > os.listdir()
['.Test-unix', '.font-unix', '.XIM-unix', '.ICE-unix', '.X11-unix',
 'systemd-private-0922d2b0d23c4a9fbb9427020fbe7bc1-chronyd.service-0kuGwG', 'dirname1']

>> > os.system("ls -a")                                   #运行shell命令，直接显示
.dirname1.ICE - unix								.Tt-un i x  .XIM- \
unix ..  .
font-un i x	syste m d
-pr
ivate-0922d2b0d23c4a9fbb9427 0 20fbe7bc1-chron y d
.serve-0k u GwG  .X11 -unix
0

>>> os.environ                                           #获取系统环境变量
environ({'XDG_SESSION_ID': '303', 'HOSTNAME': 'python', 'TERM': 'xterm', 'SHELL': '/bin/bash', 'HISTSIZE'
         : '1000', 'SSH_CLIENT': '192.168.200.1 55253 22', 'SSH_TTY': '/dev/pts/0', 'USE
         ': 'root', 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=01;05;37;41:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=01;36:*.au=01;36:*.flac=01;36:*.mid=01;36:*.midi=01;36:*.mka=01;36:*.mp3=01;36:*.mpc=01;36:*.ogg=01;36:*.ra=01;36:*.wav=01;36:*.axa=01;36:*.oga=01;36:*.spx=01;36:*.xs
         f=01;36:', 'MAIL': '/var/spool/mail/root', 'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:
         root/bin', 'PWD': '/root', 'LANG': 'en_US.UTF-8', 'HISTCONTROL': 'ignoredups', 'SHLVL': '1', 'HOME'
         : '/root', 'LOGNAME': 'root', 'SSH_CONNECTION': '192.168.200.1 55253 192.168.
         00.130 22', 'LESSOPEN': '||/usr/bin/lesspipe.sh %s', 'XDG_RUNTIME_DIR': '/run/user/0', '_': '/usr/bin/py thon3'})

>>> os.path.abspath("dirname1")                          #返回目录或文件的绝对路径
'/tmp/ dirname1'

>>> os.path.split("/tmp/dirname1/a.html")                #把目录和文件分隔成元组返回
('/tmp/dirname1', 'a.html')

>>> os.path.dirname("/tmp/dirname1/a.html")             #只显示目录
'/tmp/dirname1'
>>> os.path.basename("/tmp/dirname1/a.html")            #只显示文件
'a.html'
>>> os.path.exists("/tmp ")                             #判断是否目录或文件存在，存在就返回True为真。不存在就为假就返回False
True
>>> os.path.exists("/tmp/aa" )                          #判断是否目录或文件存在，存在就返回True为真。不存在就为假就返回False
False
>>> os.path.isabs("/tmp/dirname1 ")                    #判断是否是绝对路径，是绝对路径就返回True为真。不是绝对路径就为假就返回False
True
>>> os.path.isabs("dirname1" )                          #判断是否是绝对路径，是绝对路径就返回True为真。不是绝对路径就为假就返回False
False
>>> os.path.isfile("/tmp/dirname1/a.html ")            #判断文件是否存在，存在就返回True为真。不存在就为假就返回False
True
>>> os.path.isfile("/tmp/dirname1/b.html" )            #判断文件是否存在，存在就返回True为真。不存在就为假就返回Fals
False
>>> os.path.isdir("/tmp/dirname1 ")                    #判断目录是否存在，存在就返回True为真。不存在就为假就返回Fals
True
>>> os.path.isdir("/tmp/dirname2" )                    #判断目录是否存在，存在就返回True为真。不存在就为假就返回Fals
False
>>> os.path.jo in('/tmp','/ dirname1','a.html')        #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
'/dirname1/ a.html'
>>> os.path.getatime("dirname1")                       #返回path所指向的文件或者目录的最后存取时间
1566960224. 9806259
>>> os.path.getmtime("dirname1")                       ##返回path所指向的文件或者目录的最后修改时间
1566960149.6131687
