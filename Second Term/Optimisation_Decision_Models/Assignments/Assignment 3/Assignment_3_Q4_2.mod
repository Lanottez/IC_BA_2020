set NUM ordered; 
param GRE {NUM}; 
param TOEFL {NUM}; 
param Univ {NUM}; 
param SOP {NUM}; 
param LOR {NUM}; 
param CGPA {NUM}; 
param Res {NUM}; 
param Chance {NUM}; 
data Graduate_Admissions.dat;


var beta_0;
var beta_1;
var beta_2;
var beta_3;
var beta_4;
var beta_5;
var beta_6;
var beta_7;

var a1 binary;
var a2 binary;
var a3 binary;
var a4 binary;
var a5 binary;
var a6 binary;
var a7 binary;

var estimated_chance {NUM};

var theta {NUM};

minimize chance: sum {i in NUM} theta[i];

subject to constr_1 {i in NUM}: estimated_chance[i] = beta_0 + beta_1*GRE[i] + beta_2*TOEFL[i]+beta_3*Univ[i]+beta_4*SOP[i]+beta_5*LOR[i]+beta_6*CGPA[i]+beta_7*Res[i];
subject to constr_2 {i in NUM}: theta[i]>= Chance[i] -1* estimated_chance[i];
subject to constr_3 {i in NUM}: theta[i]>= -1*Chance[i] + estimated_chance[i];
subject to constr_4 {i in NUM}: theta[i]>=0;

subject to beta_1_1: beta_1 <= 10*a1;
subject to beta_1_2: beta_1 >= -10*a1;
subject to beta_2_1: beta_2 <= 10*a2;
subject to beta_2_2: beta_2 >= -10*a2;
subject to beta_3_1: beta_3 <= 10*a3;
subject to beta_3_2: beta_3 >= -10*a3;
subject to beta_4_1: beta_4 <= 10*a4;
subject to beta_4_2: beta_4 >= -10*a4;
subject to beta_5_1: beta_5 <= 10*a5;
subject to beta_5_2: beta_5 >= -10*a5;
subject to beta_6_1: beta_6 <= 10*a6;
subject to beta_6_2: beta_6 >= -10*a6;
subject to beta_7_1: beta_7 <= 10*a7;
subject to beta_7_2: beta_7 >= -10*a7;



subject to k: a1 + a2 + a3 + a4 + a5 + a6 + a7 <= 0;

