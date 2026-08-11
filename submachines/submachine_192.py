import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 230) - 299
    _mask = _data(739, None)
    _enc = 213
    return _mask, _enc

def run():
    matrix = ']{F`H|Io,PI6o,L n/vfPS%1Q&N?yA'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
