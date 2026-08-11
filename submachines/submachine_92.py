import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 431) - 169
    _mask = _data(40, None)
    _enc = 202
    return _mask, _enc

def run():
    matrix = 'VQ,&VBzE5*SM8Ts;t7T!_r9#qF,sGZ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
