import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 593) - 795
    _mask = _data(1616, None)
    _enc = 253
    return _mask, _enc

def run():
    matrix = 'tNT;3y;U8C$C[^*in|{9v@!5oude$L'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
