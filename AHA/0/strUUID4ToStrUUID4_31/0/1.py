def strUUID4ToStrUUID4_31 ( u ) :
    U = u . upper ( )
    V = {
        0 : U [  0 :  8 ] ,
        1 : U [  9 : 13 ] ,
        2 : U [ 14 : 15 ] ,
        3 : U [ 15 : 18 ] ,
        4 : U [ 19 : 20 ] ,
        5 : U [ 20 : 23 ] ,
        6 : U [ 24 : 36 ] }
    MAP = {
        '8' : 'E' ,
        '9' : 'F' ,
        'A' : 'A' ,
        'B' : 'B' }
    remap = lambda h : MAP [ h ]
    LIST = [ ] \
        + [ remap ( V [ 4 ] ) ] \
        + [ V [ k ] for k in ( 5 , 6 , 0 , 1 , 3 ) ]
    return '' . join ( LIST )
  
