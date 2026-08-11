import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 152) - 961
    _mask = _data(1223, None)
    _enc = 145
    return _mask, _enc

def run():
    matrix = '4uBBihXb8!UjM6a Zh#Mg!.9|heB|J'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
