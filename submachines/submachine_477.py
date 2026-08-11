import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 700) - 746
    _mask = _data(502, None)
    _enc = 103
    return _mask, _enc

def run():
    matrix = 'mkyYAWid@J:Yqr=pmMrlNh#Ov};l0`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
