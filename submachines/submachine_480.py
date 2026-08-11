import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 588) - 418
    _mask = _data(6, None)
    _enc = 177
    return _mask, _enc

def run():
    matrix = 'xz$;C64Pi+/PJ[)~U^!h^32bY `meq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
