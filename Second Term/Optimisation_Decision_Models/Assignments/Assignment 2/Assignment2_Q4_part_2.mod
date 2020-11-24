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

var estimated_chance {NUM};

var theta {NUM};

minimize chance: sum {i in NUM} theta[i];

subject to constr_1 {i in NUM}: estimated_chance[i] = beta_0 + beta_1 * GRE[i] + beta_2*TOEFL[i]+beta_3*Univ[i]+beta_4*SOP[i]+beta_5*LOR[i]+beta_6*CGPA[i]+beta_7*Res[i];
subject to constr_2 {i in NUM}: theta[i]>= Chance[i] -1* estimated_chance[i];
subject to constr_3 {i in NUM}: theta[i]>= -1*Chance[i] + estimated_chance[i];
subject to constr_4 {i in NUM}: theta[i]>=0;

