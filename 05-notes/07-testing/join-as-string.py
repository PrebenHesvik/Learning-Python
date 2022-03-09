def join_items(sequence, delimiter):
    return f'{delimiter}'.join([str(x) for x in sequence])
    
def test_join_items_zero_items():
    lst = []
    delimiter = '-'
    assert join_items(lst, delimiter) == ''

def test_join_items_one_item():
    lst = [1]
    delimiter = '-'
    assert join_items(lst, delimiter) == '1'

def test_join_items_two_items():
    lst = [1, 2]
    delimiter = '-'
    assert join_items(lst, delimiter) == '1-2'