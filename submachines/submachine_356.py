import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 305) - 678
    _mask = _data(514, None)
    _enc = 138
    return _mask, _enc

def run():
    matrix = '0Hn>rqX.B|Kv3#K+EIJ+3WYP}w+X>+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
