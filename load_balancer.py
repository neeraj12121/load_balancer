import server1
import server2
import server3

servers=[server1,server2,server3]

n=-1
def get_server():
    global n
    n+=1
    return servers[n%len(servers)]


if __name__ == '__main__':

    from random import randint

    for i in range(18):
        a=randint(2,8)
        b=randint(2,8)
        

        server=get_server()
        print(server.print_name())
        print("Rectangle of {}*{}".format(a,b))
        print(server.CountSqHandler(a,b))
        print(server.lastCountSqHandler())
        print("  ")

        
