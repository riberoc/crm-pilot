import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 388) - 878
    _mask = _data(567, None)
    _enc = 94
    return _mask, _enc

def run():
    matrix = '52EA`?vua[@y26$&%=JZ=Q-%T5Q.ri'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
