# define the variables
var Arlington binary;
var Belmont binary;
var Cambridge binary;
var Lexington binary;
var Somerville binary;
var Winchester binary;

# define the objective function
minimize obj: Arlington + Belmont + Cambridge + Lexington + Somerville + Winchester;

# define the constraints
subject to D_Arlington:	Arlington + Belmont + Cambridge >= 1;
subject to D_Belmont:	Arlington + Belmont + Cambridge + Lexington >= 1;
subject to D_Cambridge:	Arlington + Belmont + Cambridge + Winchester >= 1;
subject to D_Lexington:	Belmont + Lexington + Somerville >= 1;
subject to D_Somerville:	Lexington + Somerville >= 1;
subject to D_Winchester:	Cambridge + Winchester >= 1;
 