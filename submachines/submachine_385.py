import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 867) - 213
    _mask = _data(616, None)
    _enc = 34
    return _mask, _enc

def run():
    matrix = ']W^Wr.9+*%Gm>;fH0:Hl ~RtNKSfnv'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
