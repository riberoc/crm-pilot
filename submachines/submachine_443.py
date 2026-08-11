import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 729) - 539
    _mask = _data(232, None)
    _enc = 16
    return _mask, _enc

def run():
    matrix = '0=O+^V 5=0/e~UGB2EU);x?~CSF3uY'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
