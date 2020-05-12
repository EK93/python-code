import requests, hashlib

def wykop_init():
    appkey = "wPHtU9dZGx"
    secretkey = "kzVIirgn71"
    accountkey = "Fzk6gRIeU2R1IyxcYnIS"
    login = "ShamelessPlug"
    password = "pointrox"
    url = "https://a2.wykop.pl/login/index/appkey/" + appkey + "/"
    logparams = {"login": "ShamelessPlug", "password": "pointrox", "accountkey": accountkey}
    hashstring = (secretkey+url+login+","+password+","+accountkey).encode('utf-8')
    headmd5 = hashlib.md5()
    headmd5.update(hashstring)
    
    logheader = {"apisign": headmd5.hexdigest(), "Content-Type": "application/x-www-form-urlencoded"}
    
    r = requests.post(url = url, data = logparams, headers = logheader)
    content = r.json()
    userkey = content['data']['userkey']
    return userkey


appkey = "wPHtU9dZGx"
secretkey = "kzVIirgn71"
accountkey = "Fzk6gRIeU2R1IyxcYnIS"
userkey = wykop_init()

url = "https://a2.wykop.pl/Entries/Add/appkey/" + appkey + "/userkey/" + userkey + "/"
cmtbody = "#codziennapobudkawpolsce #stonoga #dziendobry"
cmtatch = "https://streamable.com/ugj9ef"
comment = cmtbody + "," + cmtatch
md5key = (secretkey+url+comment).encode('utf-8')

reqdata = hashlib.md5()
reqdata.update(md5key)

wykoparams = {"body": cmtbody, "embed": cmtatch}
wykopmd5 = {"apisign": reqdata.hexdigest()}

r = requests.post(url = url, data = wykoparams, headers = wykopmd5)
print(r.text)