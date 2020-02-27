from example_package import example

def test_fahrToKelv():
    '''
    make sure freezing is calculated correctly
    '''

    
    assert example.fahrToKelv(32) == 273.15, 'incorrect freezing point!'
