import subprocess
log = subprocess.check_output(["git", "log", "--oneline"])
ss = log.splitlines();
#name="setter based dependency injection"
#ff=subprocess.check_output(["git", "archive", "--format","zip", "--output",name+".zip","5d09988"])
num = len(ss)
print num
for commit in ss:    
    sha=commit[:7]
    name=commit[8:]
    print sha+" "+name
    if "/" in name:
        name= name.replace("/"," ")
    name="../"+str(num)+" "+name+".zip"
    try:
        ff=subprocess.check_output(["git", "archive", "--format","zip" ,"--output",name,sha])
        num=num-1
    except: 
        None
    
