import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 241) - 747
    _mask = _data(925, None)
    _enc = 136
    return _mask, _enc

def run():
    matrix = 'EgO&|[#56 J!qUj/eUv~&G`Nn{,<Oc'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
