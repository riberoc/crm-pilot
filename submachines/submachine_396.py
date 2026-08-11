import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 163) - 176
    _mask = _data(424, None)
    _enc = 80
    return _mask, _enc

def run():
    matrix = 'oil%Pv7b}Ee =s.295+R5.9,fDAkA7'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
