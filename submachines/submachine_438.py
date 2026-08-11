import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 484) - 649
    _mask = _data(745, None)
    _enc = 131
    return _mask, _enc

def run():
    matrix = '(B4:Ir( Qoe!@V/H@C`Q!&iUt/.2.n'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
