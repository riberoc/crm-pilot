import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 991) - 277
    _mask = _data(664, None)
    _enc = 34
    return _mask, _enc

def run():
    matrix = 'yXt:gN=`3|`=Vu8w wP*>a:3ina[!n'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
