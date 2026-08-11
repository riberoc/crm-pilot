import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 524) - 660
    _mask = _data(373, None)
    _enc = 248
    return _mask, _enc

def run():
    matrix = 'bcsJHM=.j69gbTd<qM!l3-gkrfIC~b'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
