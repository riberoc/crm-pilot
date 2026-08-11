import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 720) - 347
    _mask = _data(841, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = '4w.`63T+g3 ?d9_e$8)Ib#5f=Q{,GV'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
