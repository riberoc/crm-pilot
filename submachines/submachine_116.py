import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 227) - 797
    _mask = _data(863, None)
    _enc = 140
    return _mask, _enc

def run():
    matrix = 'sOp+%A}TCFVlh-iB5;8 bXf}sb-B/='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
