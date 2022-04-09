from asyncore import write
import dbconf

db = dbconf.DataBase()
host_path ="/etc/hosts"

redirection="proyectoadrianitt.ddns"

class block_host:
    def __init__(self):
        pass
    
        
    def BlockListStatus(self,address_type):
        
        if address_type==1:
            # inicial cofiguration
            default=["127.0.0.1	localhost","127.0.1.1	adrian-VirtualBox","# The following lines are desirable for IPv6 capable hosts","::1     ip6-localhost ip6-loopback","fe00::0 ip6-localnet","ff00::0 ip6-mcastprefix","ff02::1 ip6-allnodes","ff02::2 ip6-allrouters"]
        
            # add blacklist   
            blacklist=[]
            for r in db.select_allip_blacklist():
                blacklist.append(r[0])

            # check if the list is not enty
            if len(blacklist) > 0:
               for nw in blacklist:
                   default.append("localhost " + nw)

            #write host file   
            with open(host_path, 'w') as file:
                for df in default:
                    file.write(df+"\n")
            

        elif address_type ==3:

            # inicial cofiguration
            default=["127.0.0.1	localhost","127.0.1.1	adrian-VirtualBox","# The following lines are desirable for IPv6 capable hosts","::1     ip6-localhost ip6-loopback","fe00::0 ip6-localnet","ff00::0 ip6-mcastprefix","ff02::1 ip6-allnodes","ff02::2 ip6-allrouters"]
        
            # add blacklist   
            blacklist=[]
            for r in db.select_all_blacklist():
                blacklist.append(r[0])

            # check if the list is not enty
            if len(blacklist) > 0:
                for nw in blacklist:
                    default.append("proyectoadrianitt.ddns.net " + nw)

            #write host file   
            with open(host_path, 'w') as file:
                for df in default:
                    file.write(df+"\n")
