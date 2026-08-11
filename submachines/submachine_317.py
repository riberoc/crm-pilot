import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 716) - 339
    _mask = _data(225, None)
    _enc = 207
    return _mask, _enc

def run():
    matrix = '1O>!,i}[{~UDd3rct@J%U V~?ESjb='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
