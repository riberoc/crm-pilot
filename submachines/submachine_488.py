import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 218) - 901
    _mask = _data(830, None)
    _enc = 69
    return _mask, _enc

def run():
    matrix = '0bh5,T=ZcvRPU^^VLH^,7y7d#D QGV'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
