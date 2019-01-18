#include "matlab.hpp"

mwArray x, y, z, xi, yi;    // Input argument(s)
mwArray YI;                 // Output argument(s) 
mwArray ZI, XI;             

ZI = griddata(x,y,z,XI,YI);
XI = griddata(&YI,&ZI,x,y,z,xi,yi);
