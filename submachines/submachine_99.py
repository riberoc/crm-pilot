import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 954) - 586
    _mask = _data(336, None)
    _enc = 171
    return _mask, _enc

def run():
    matrix = 'r#CPOISj|1F rFkLFVjLb2u-A~(zA4'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
