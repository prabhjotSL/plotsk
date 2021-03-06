
def simple_test():
    'Not a real unit test by any stretch of the imagination. Stay tuned.'
    import plotsk
    from numpy import *
    
    p = plotsk.Plot()
    
    a = array([1,2,3,4])
    b = 2*a
    c = (a - 2)**2
    
    p.add_data(a, 'a')
    p.add_data(b, 'b')
    p.add_data(c, 'c')
    p.add_line('a', 'b')
    p.add_points('a', 'c')
    
    p.show()
    

if __name__ == '__main__':
    simple_test()
