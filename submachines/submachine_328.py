import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 623) - 249
    _mask = _data(971, None)
    _enc = 167
    return _mask, _enc

def run():
    matrix = 'NnP,E;pAZF{? RY~V$~VN1vqfzBr<1'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
