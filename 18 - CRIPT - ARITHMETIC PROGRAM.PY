import itertools

def solve():
    letters = "SENDMORY"   
    for perm in itertools.permutations("0123456789", len(letters)):
        s = dict(zip(letters, perm))
        if s['S']=='0' or s['M']=='0': continue  
        send = int(s['S']+s['E']+s['N']+s['D'])
        more = int(s['M']+s['O']+s['R']+s['E'])
        money= int(s['M']+s['O']+s['N']+s['E']+s['Y'])
        if send + more == money:
            print(f"SEND={send}, MORE={more}, MONEY={money}")
            return

solve()
