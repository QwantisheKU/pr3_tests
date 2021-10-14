from itertools import zip_longest

class Coder:
    def coder(msg, key):
        lmsg = len(msg)
        lkey = len(key)
        tmp = dict((k, msg[i:lmsg:lkey]) for i, k in enumerate(key))
        return "".join(tmp[x] for x in sorted(key))

