import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 251) - 656
    _mask = _data(984, None)
    _enc = 144
    return _mask, _enc

def run():
    matrix = '#;s 2;Iz;|F|Je?^|J:{Ul>2V7<Ot|'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
