import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 362) - 945
    _mask = _data(1506, None)
    _enc = 198
    return _mask, _enc

def run():
    matrix = 'Q~tb7vD`bamY;k9sO c[+iL&|TN@v_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
