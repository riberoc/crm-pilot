import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 573) - 727
    _mask = _data(509, None)
    _enc = 233
    return _mask, _enc

def run():
    matrix = ' Q;yr%tFeF/svmhdZyjrDGTYk;:yBd'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
