import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 537) - 744
    _mask = _data(464, None)
    _enc = 233
    return _mask, _enc

def run():
    matrix = ')RT#LLKQ ,get0<KNS7r3NA;09Us_a'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
