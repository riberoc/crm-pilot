import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 412) - 230
    _mask = _data(212, None)
    _enc = 120
    return _mask, _enc

def run():
    matrix = 'sXH[IRB1.eK,D!&BM$>H48U-=GeH(&'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
