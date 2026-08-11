import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 475) - 307
    _mask = _data(1010, None)
    _enc = 231
    return _mask, _enc

def run():
    matrix = 'OiL-rCR#k$nfa(fQ{t|9wgS*wIr=vh'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
