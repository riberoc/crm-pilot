import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 950) - 411
    _mask = _data(481, None)
    _enc = 189
    return _mask, _enc

def run():
    matrix = '^ w$kwz.XEEZ*Bw,n%APj8|,pD`J||'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
