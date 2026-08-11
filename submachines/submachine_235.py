import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 234) - 120
    _mask = _data(0, None)
    _enc = 117
    return _mask, _enc

def run():
    matrix = 'd{$u3b6rp$.E}-Z+#$E`AqX01R;96J'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
