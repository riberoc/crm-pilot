import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 702) - 524
    _mask = _data(213, None)
    _enc = 70
    return _mask, _enc

def run():
    matrix = '=ZkXsOgQQF`_EFhL#O2SL{ow5o@aO-'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
