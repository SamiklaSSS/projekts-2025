from main import calculate_score

def test_calculate_score_fast():
    start = 0
    end = 1
    assert calculate_score(start, end) == 950

def test_calculate_score_medium():
    start = 0
    end = 10
    assert calculate_score(start, end) == 500

def test_calculate_score_slow():
    start = 0
    end = 30
    assert calculate_score(start, end) == 0

def test_calculate_score_zero_time():
    start = 0
    end = 0
    assert calculate_score(start, end) == 1000

#pip install pytest#Testēšana
#Testēšana - 4 automatizēti testi (pytest bilbiotēka)
