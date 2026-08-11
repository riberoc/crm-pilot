import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 501) - 790
    _mask = _data(522, None)
    _enc = 250
    return _mask, _enc

def run():
    matrix = ']br[:Z?_A&+y*O!fjt/ qh/<^DYj+/'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
