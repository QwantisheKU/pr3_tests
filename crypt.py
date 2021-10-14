from itertools import zip_longest

class Coder:
    def coder(msg, key):
        lmsg = len(msg)
        lkey = len(key)
        tmp = dict((k, msg[i:lmsg:lkey]) for i, k in enumerate(key))
        return "".join(tmp[x] for x in sorted(key))

class Decoder:
    def decoder(msg, key):
        lmsg = len(msg)
        lkey = len(key)

        d, m = divmod(lmsg, lkey)
        group = dict((k, d) for k in key)
        for i in range(m):
            group[key[i]] += 1

        tmp = {}
        for k in sorted(key):
            tmp[k], msg = msg[:group[k]], msg[group[k]:]
        return("".join("".join(x) for x in zip_longest(*(tmp[k] for k in key), fillvalue="")))
