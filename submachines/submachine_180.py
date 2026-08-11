import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 704) - 796
    _mask = _data(334, None)
    _enc = 126
    return _mask, _enc

def run():
    matrix = 'F<Si^+e_@D_AIPk,z~sL$rZ:vKcfw_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
