from main import *

def test_simple_work():
	assert work_calc(10, 2, 2) == 36
	assert work_calc(20, 3, 2) == 230
	assert work_calc(30, 4, 2) == 650

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 230
