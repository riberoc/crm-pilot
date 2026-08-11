import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 106) - 173
    _mask = _data(376, None)
    _enc = 113
    return _mask, _enc

def run():
    matrix = '6E`E/U-pxVvr9Kr3L7:D %Mm[4^,Zd'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
