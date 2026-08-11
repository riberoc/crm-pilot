import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 189) - 809
    _mask = _data(878, None)
    _enc = 170
    return _mask, _enc

def run():
    matrix = 'e;=t.7PT~1J0IkY7Fq`iMS2UBs5M3}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
