import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 949) - 395
    _mask = _data(485, None)
    _enc = 221
    return _mask, _enc

def run():
    matrix = ')H9j1!TE.wP/Ss;,X0ltFA>7 2<Cp%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
