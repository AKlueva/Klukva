def test_passing():
    assert ('home', 'work') == ('home', 'work')


def test2_passing():
    assert ('QA') == ('QA')

def test3_passing():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)

def test4_passing():
    assert not 'QA' == 'QC'
