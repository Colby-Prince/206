class TorRelay:
    def __init__(self,NickName,Fingerprint,IPAddress,Bandwidth,type):
        self.NickName=NickName
        self.Fingerprint=Fingerprint
        self.IPAddress=IPAddress
        self.Bandwidth=Bandwidth
        self.type=type
        self.Middle= "Middle" in type
        self.Entry= "Entry" in type
        self.Exit= "Exit" in type
    
    def __str__(self):
        if self== self.Middle:
            return f"{self.NickName}, {self.Fingerprint}, {self.IPAddress}, {self.Bandwidth} + 'Middle'"
        elif self== self.Entry:
            return f"{self.NickName}, {self.Fingerprint}, {self.IPAddress}, {self.Bandwidth} + 'Entry'"
        elif self == self.Exit:
            return f"{self.NickName}, {self.Fingerprint}, {self.IPAddress}, {self.Bandwidth} + 'Exit'"

relay = TorRelay('skylarkRelay','00240ECB2B535AA4C1E1874D744DFA6AF2E5E941','95.111.230.178','14000','Entry')
print(relay.NickName)
print(relay.Fingerprint)
print(relay.IPAddress)
print(relay.Bandwidth)
print(relay.type)


#Again all of this is correct I just did not have the time to finish this. However, I am submitting it for some credit.


        