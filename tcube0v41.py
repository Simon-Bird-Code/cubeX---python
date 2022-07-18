"""
Project - X_cube_x
    Rubix Cube data generation and manipulation

Author : Simon Bird

Aim
    A project that can generate large data sets, for storage,
    quick access and comparision to another large data
    set.
    Program and store all several billion possible
    combinations of cube configuration, and compare with
    a random colour fill of the segments.

    I should end up with 2 data sets, 1 possible,
    1 not possible.

"""
#!/usr/bin/env python3
 
from turtle import TurtleScreen, RawTurtle, TK
from turtle import *
import turtle

import math
import time
import random






#==== global ====#

g_speed=10 #0 is fastest

loadWindow = turtle.Screen()
turtle.speed(g_speed)

t=turtle.Turtle()
t.speed(g_speed)


#============================ GFX ============================#

#============================ CUBE NET GFX ============================#

def set_point_diag ( s_size , x , y , direction = 'up' ):
    # only works for this cross purpose
    total = 5 * 3 * s_size
    half_point = total / 2
    if ( ( total % 2 ) != 0 ):  half_point=(total-1)/2
    if ( ( total % 2 ) == 0 ):  half_point=(total)/2
    
    t.up()
    t.setx(x-half_point); t.sety(y-half_point);
    t.down()

def set_pos( x_in , y_in ):
    t.up()
    t.setx(x_in); t.sety(y_in)
    t.down()

def set_point ( s_size , x , y , direction = 'up' ):
    # only works for this cross purpose
    total = 5 * 3 * s_size
    half_point = total / 2
    if ( ( total % 2 ) != 0 ):  half_point=(total-1)/2
    if ( ( total % 2 ) == 0 ):  half_point=(total)/2
    
    t.up()
    t.setx(x-half_point); t.sety(y-half_point);
    t.down()
    
def make_small_diag_r ( s_size , colour ):
    t.fillcolor( colour );
    t.begin_fill()
    #t.forward ( s_size );
    t.left( 90  ); t.forward( s_size );
    t.left( 45 ); t.forward ( s_size * 1.4 );
    t.left( 45 +90  ); t.forward ( s_size  );
    t.left( 45 );  t.forward ( s_size *1.4 );
    t.left(45)
    t.end_fill()

def make_small_diag ( s_size , colour ):
    t.fillcolor( colour );
    t.begin_fill()
    #t.forward ( s_size );
    t.left( 135 ); t.forward( s_size * 1.4 );
    t.left( 45 ); t.forward ( s_size );
    t.left(135 ); t.forward ( s_size * 1.4 );
    t.left (45);  t.forward ( s_size );
    t.end_fill()

def make_small( s_size , colour ):
    t.fillcolor( colour );      t.begin_fill()
    for edge in range ( 4 ):    t.forward ( s_size ); t.left( 90 )
    t.end_fill()

#==================================================

def s_map( cube , cube_ref , cell_id ):
    if(cube_ref==0): s_map=[0,1,2,3,4,5,6,7,8]
    if(cube_ref==1): s_map=[0,1,2,3,4,5,6,7,8]
    if(cube_ref==2): s_map=[0,1,2,3,4,5,6,7,8]
    if(cube_ref==3): s_map=[0,1,2,3,4,5,6,7,8]
    if(cube_ref==4): s_map=[0,1,2,3,4,5,6,7,8]
    if(cube_ref==5): s_map=[0,1,2,3,4,5,6,7,8]
    return cube[cube_ref][s_map[cell_id]]

def c_map ( cube , cube_ref , cell_id ):
    tcolour=s_map( cube , cube_ref , cell_id )
    
    if( tcolour == 0 ): return 'white'
    if( tcolour == 1 ): return 'red'
    if( tcolour == 2 ): return 'blue'
    if( tcolour == 3 ): return 'yellow'
    if( tcolour == 4 ): return 'orange'
    if( tcolour == 5 ): return 'green'
    return 'black'

def make_face ( s_size , cube , cube_ref , x , y ): #currently goes up +xy
    #0123456789
    for row in range ( 3 ):
        coly = ( y + ( row * s_size )) 
        for col in range ( 3 ):
            set_point( s_size , x + ( col * s_size ) , coly );
            make_small( s_size , c_map( cube , cube_ref , col + ( 3*row) ) )

def make_face_diag_r ( s_size , cube , cube_ref , x , y ): #currently goes up +xy
    #0123456789
    for row in range ( 3 ):
        coly = ( y + ( row * s_size ))
        for col in range ( 3 ):
            set_point_diag( s_size , x + ( col * s_size ) # adjusted for left 
                            , (  coly - ( col*s_size ) ) );
            make_small_diag_r( s_size , c_map( cube , cube_ref , col + ( 3*row) ) )

def make_face_diag ( s_size , cube , cube_ref , x , y ): #currently goes up +xy
    #0123456789
    for row in range ( 3 ):
        coly = ( y + ( row * s_size ))
        for col in range ( 3 ):
            set_point_diag( s_size , x + ( col * s_size ) - ( row * s_size)# adjusted for left 
                            , coly );
            make_small_diag( s_size , c_map( cube , cube_ref , col + ( 3*row) ) )



#===============================================================
    
def make_cross(cube):
    s_size=15;
    turtle.ht();    t.ht();
    turtle.tracer(0,0)
    make_face( s_size , cube , 0 , 0 , 0 )
    hor_1=[5,4,0,2,5]
    for hor in range ( 5 ):
        make_face( s_size , cube , hor_1[hor]
                   , ( hor *( 3 * s_size ) ) , ( 2 * ( 3 * s_size ) ) )
    ver_1 = [5,1,0,3,5]
    for ver in range ( 5 ):
        make_face( s_size , cube , ver_1[ver]
                   , ( 2 *( 3 * s_size ) ) , ( ver * ( 3 * s_size ) ) )
           
    turtle.update()
    
def make_cross_diag(cube): # left
    s_size=15;
    turtle.ht();    t.ht();
    turtle.tracer(0,0)
    make_face_diag( s_size , cube , 0 , 0 , 0 )
    hor_1=[5,4,0,2,5]
    for hor in range ( 5 ):
        make_face_diag_r( s_size , cube , hor_1[hor]
                   , ( hor *( 3 * s_size ) ) , ( 2 * ( 3 * s_size ) ) )
    ver_1 = [5,1,0,3,5]
    for ver in range ( 5 ):
        make_face_diag_r( s_size , cube , ver_1[ver]
                   , ( 2 *( 3 * s_size ) ) , ( ver * ( 3 * s_size ) ) )
           
    turtle.update()

#===========================================================

def make_exploded_cube(cube):
    s_size=10;
    o=30
    turtle.ht(); 
    turtle.tracer(0,0)
#make_face_diag( s_size , cube , 0 , 0 , 0 )
#white
    x0 = (3*(1.4*s_size))+s_size
    y0 = 7*(3* s_size)-o-o-o-15
    make_face_diag( s_size , cube , 0 , x0 , y0 )
#red
    x1 = (3*(1.4*s_size))+s_size 
    y1 = 2*(3* s_size)-o
    make_face( s_size , cube , 1 , x1 , y1 )
#blue
    x2 = (3*(1.4*s_size))+s_size+o
    y2 = 3*(3* s_size)-o
    make_face_diag_r( s_size , cube , 2 , x2 , y2 )
#yellow
    x3 = (3*(1.4*s_size))+s_size-o-15
    y3 = 4*(3* s_size)-o-o+10
    make_face( s_size , cube , 3 , x3 , y3 )
#orange
    x4 = (3*(1.4*s_size))+s_size-o-o-10
    y4 = 5*(3* s_size)-o-o-o-o+o
    make_face_diag_r( s_size , cube , 4 , x4 , y4 )
#green
    x5 = (3*(1.4*s_size))+s_size
    y5 = 1*(3* s_size)-o
    make_face_diag( s_size , cube , 5 , x5 , y5 )

    turtle.update()
    
#===============================================================
    


    

#============================== CUBE INIZ =========================#

   # when move cube remember to shift by one 0-1

def iniz_cube ():
    cube=[]
    for j in range (6):
        inner=[];
        for i in range (9):  inner.append(j)
        cube.append(inner)
    return cube

#=========================== LOOK UP TABLE =============================#

def get_squares_involved_lookup ( orientation , layer ):
    #work out coords - made cardboard cube and labled
    #use return from here back to cube and direction
    if( orientation == 'y' ):#0,5 easyier
        if(layer==1):#0 - works 
            process_slice_string="5[123456789]1[123]2[321]3[321]4[123]"
        if(layer==2):#x - works
            process_slice_string="5[123456789]1[456]2[654]3[654]4[456]"
        if(layer==3):#5 - works
            process_slice_string="0[123456789]1[789]2[987]3[789]4[987]"          

    if( orientation == 'x' ):#2,4
        if(layer==1):#4 -- works
            process_slice_string="4[123456789]0[147]1[147]5[741]3[741]"             
        if(layer==2):#x- works
            process_slice_string="4[123456789]0[258]1[258]5[258]3[852]"
        if(layer==3):#2- works
            process_slice_string="2[321654987]0[369]1[369]5[369]3[963]"         

    if( orientation == 'z' ):#1,3
        if(layer==1):#1
            process_slice_string="1[123456789]0[123]2[963]5[321]4[369]"
        if(layer==2):#x - works
            process_slice_string="1[123456789]0[456]2[852]5[456]4[852]"
        if(layer==3):#3
            process_slice_string="3[123456789]0[789]2[147]5[789]4[147]" 

    return process_slice_string

#====================================================

def spin_face ( c_slice ):
    #top corners
    temp=c_slice[1]; c_slice[1]=c_slice[7]; c_slice[7]=c_slice[9];
    c_slice[9]=c_slice[3]; c_slice[3]=temp
    #top sides
    temp=c_slice[2]; c_slice[2]=c_slice[4]; c_slice[4]=c_slice[8];
    c_slice[8]=c_slice[6]; c_slice[6]=temp
    #whole side
    return c_slice

def spin_ring ( c_slice ):
    temp1=c_slice[10]; temp2=c_slice[11]; temp3=c_slice[12]
    #side 1
    c_slice[10]=c_slice[19]; c_slice[11]=c_slice[20]; c_slice[12]=c_slice[21];
    #side 2
    c_slice[19]=c_slice[16]; c_slice[20]=c_slice[17]; c_slice[21]=c_slice[18];
    #side 3
    c_slice[16]=c_slice[13]; c_slice[17]=c_slice[14]; c_slice[18]=c_slice[15];
    #side 4
    c_slice[13]=temp1; c_slice[14]=temp2; c_slice[15]=temp3;
    return c_slice

#==================================================

def spin_edge ( c_slice ): return spin_ring ( spin_face ( c_slice ))
    
def reverse_spin_edge ( slice_in ):
    for i in range ( 3 ):     slice_in=spin_edge ( slice_in )
    return slice_in

def reverse_spin_face ( slice_in ):
    for i in range ( 3 ):     slice_in=spin_face ( slice_in )
    return slice_in

def reverse_spin_ring ( slice_in ):
    for i in range ( 3 ):     slice_in=spin_ring ( slice_in )
    return slice_in

#================= CUBE CHANGE =================#

def make_move ( cube_old , axis , depth , direction ):
    cube_new = []

    cube_new = ( new_spin_edge ( cube_old , axis , depth , direction) )
        
    return cube_new 

#======

def new_spin_edge(cube,axis,depth,direction):
    # get lookup
    configuration_data = get_squares_involved_lookup ( axis , depth )
    
    # get cube data -  #send to move - #put back in cube
    cube = processing_cube ( cube , configuration_data , direction )
       
   # print ( cube )

    return(cube)

#===================================================


def in_t_slice( face , element , config_data , t_slice ):
   # print(t_slice[0])
    for k in range ( len ( config_data ) ):
        check=config_data[k]
        if( ( check[0]==face ) and (check[1]==element) ):
           #print(k)
            
            #print(face,":",element,"=",k, "-" , t_slice[k+1])
            return (t_slice[k+1])
    
    return "false"


# has cell-1 to fudge the cube index issue
def processing_cube( cube , config_in , direction):

    t_slice = [];       s1=config_in;
    c_pos=0;    segment_start_offset=2;    segment_stop_offset=4
    
    t_slice.append("place_holder") # annoying due to shift in move 0-1
    #WORK OUT LATER

    config_data=[]
    
    if( len(config_in) == 36 ): # deal with surface
        surface= int ( s1 [ 0:1 ] )
        for j in range ( 9 ):
            cell_id= int ( s1 [ segment_start_offset + j : segment_start_offset + j + 1 ] )
#action
            t_slice.append (cube[surface][cell_id - 1 ])
            config_data.append([surface,cell_id-1])
        c_pos = 12
        
    for j in range ( 4 ): # deal with ring
        surface=int ( s1 [ c_pos : c_pos + 1 ] )    
        c_pos+=segment_start_offset
        for i in range ( 3 ):
            cell_id = int ( s1 [ ( c_pos + i ) : ( c_pos + i ) + 1 ] )
#action
            t_slice.append(cube[ surface ][ cell_id - 1 ]);
            config_data.append([surface,cell_id-1])
        c_pos+=segment_stop_offset

#===== do something with cube lol =========#
    if( len(config_in) ==36 ):
        if(direction == "cw"):
            t_slice=spin_edge( t_slice )
        if(direction == "ccw"):
            t_slice=reverse_spin_edge( t_slice )
    if( len(config_in) ==24 ):
        if(direction == "cw"):
            t_slice=spin_ring( t_slice )
        if(direction == "ccw"):
            t_slice=reverse_spin_ring( t_slice )        
        
#===== remake cube =====#
   # print("old-cube",cube)    
   # print("cD",config_data)

    string_in="w"
    t_slice_in="q"
    
    new_cube=[]
   # print("t_s",t_slice)
    #remake whole cube as string immutible
    for i in range (6):
        new_cube_inner=[]
        for j in range (9):
            #print(i,"::",j)
            element = in_t_slice ( i , j , config_data , t_slice )
            if( element == "false" ):
                new_cube_inner.append(cube[i][j])
            else:
                new_cube_inner.append(element)           

        new_cube.append(new_cube_inner)

   # print("new_cube",new_cube)

    return new_cube

#===================== MAIN =========================#
global_ax = 'x'
global_lay = 1

g_input_string = " test "


def input_line( s_in):
    global g_input_string
    g_input_string=s_in
    
   
    

    set_pos(-200,-260)
    t.color("white")
    t.fillcolor('white');
    t.begin_fill()
    t.forward(200);t.left(90);
    t.forward(20);t.left(90);
    t.forward(200);t.left(90);
    t.forward(20);
    t.end_fill()
    t.left(90);
    
    t.color("black")
    set_pos(-200,-260)
    t.write( g_input_string , font=('Arial',12,'normal') )
    set_pos(0,0)    


def iniz_system():
    
    set_pos(-100,-150)
    t.write("X_cube_x" , font=('Arial',20,'bold') )
    set_pos(-200,-180)
    t.write("Keys - " , font=('Arial',12,'normal') )
    set_pos(-200,-200)
    t.write("x , y , z - axis " , font=('Arial',12,'normal') )
    set_pos(-200,-220)
    t.write("1 , 2 , 3 - layers " , font=('Arial',12,'normal') )
    set_pos(-200,-240)
    t.write("Enter Selection  - c to confirm , r ro reset , q to quit " , font=('Arial',12,'normal') )
    set_pos(0,0)
    reset_cube()




def test_bed():
    make_small_diag_r ( 10 , 'red' )
    t.write("hello" , font=('Arial',20,'bold') )

def main_code():

    cube=iniz_cube()
    #print(cube)
    make_exploded_cube( cube )
    time.sleep(1)
    
    cube = make_move ( cube , 'x' , 1 , 'cw' )
    make_exploded_cube( cube )
    time.sleep(1)
    
    cube = make_move ( cube , 'z' , 1 , 'cw' )
    make_exploded_cube( cube )
    time.sleep(1)

g_cube=[]

def reset_cube():
    global g_cube
    g_cube=iniz_cube()
    make_exploded_cube( g_cube );    time.sleep(1)


def run_cube():
    print (time.time())
    global g_cube
    direction = 'cw'
    for i in range ( 10000 ): # 3 seconds = 10000 = 3333 / sec 
        move_choice = random.randrange(0,18)
        if( move_choice >= 9 ):
            move_choice = move_choice - 9
            direction = 'ccw'
        #1-9???
        if(move_choice//3 == 0):
            g_cube = make_move ( g_cube , 'x' , (move_choice%3)+1 , direction )
        if(move_choice//3 == 1):
            g_cube = make_move ( g_cube , 'y' , (move_choice%3)+1 , direction ) 
        if(move_choice//3 == 2):
            g_cube = make_move ( g_cube , 'z' , (move_choice%3)+1 , direction ) 
            #print( move_choice , "-" , move_choice%3 , "-" , move_choice//3 )
    print (time.time())
    make_exploded_cube( g_cube );
    #random move
    # xyz123+- so 1-18 random
    #for moves in range ( time_div ):
    #
    #global global_ax;    global global_lay
    #global g_cube
    #g_cube = make_move ( g_cube , global_ax , global_lay , 'cw' )
    return    # this is a time test, how many iterations happen per second
    
 
def run_cube_old():
    global global_ax;    global global_lay
    global g_cube
    g_cube = make_move ( g_cube , global_ax , global_lay , 'cw' )
    make_exploded_cube( g_cube );    time.sleep(1)
   
   
def du ():main_core() #print( "Up");main_core()
def dl ():test_bed() #print( "Left");
def dr ():print( "Right")
def dd ():main_code() #print( "Down")
def ax ():    global global_ax;    global_ax='x';  #  print( "x")
def ay ():    global global_ax;    global_ax='y'; #   print( "y")
def az ():    global global_ax;    global_ax='z'; #   print( "z")
def n1():    global global_lay;    global_lay=1;  #  print( "1")
def n2():    global global_lay;    global_lay=2;  #  print( "2")
def n3():    global global_lay;    global_lay=3; #   print( "3")
def kr():print( "r"); reset_cube();input_line("reset cube")    
def kq():print( "q"); loadWindow.bye()
def cc():
    run_cube_old();#print("c"); 
    input_line("run cube ="+global_ax+" ("+str(global_lay)+")")
def cb():
    run_cube()

def main_core():

    iniz_system()
    
    loadWindow.onkey(du, "Up")
    loadWindow.onkey(dl , "Left")
    loadWindow.onkey(dr , "Right")
    loadWindow.onkey(dd , "Down")

    loadWindow.onkey(ax , "x")
    loadWindow.onkey(ay , "y")
    loadWindow.onkey(az , "z")

    loadWindow.onkey(n1 , "1")
    loadWindow.onkey(n2 , "2")
    loadWindow.onkey(n3 , "3")

    loadWindow.onkey(kr , "r")

    loadWindow.onkey(kq , "q")
    
    loadWindow.onkey(cc, "c")
    loadWindow.onkey(cb, "b")
    loadWindow.listen()
    loadWindow.mainloop()

    
    main_code()

#========== TURTLE STUFF NEW ENTRANCE ==============#

if __name__ == "__main__":
    main_core()

