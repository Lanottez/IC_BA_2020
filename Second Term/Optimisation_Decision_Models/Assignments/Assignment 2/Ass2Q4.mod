#load in data
set NUM ordered; # candidate number
param GRE {NUM}; # GRE Score
param TOEFL {NUM}; # TOEFL Score
param Univ {NUM}; # University Rating
param SOP {NUM}; # Statement of Purpose Strength
param LOR {NUM}; # Letter of Recommend. Strength
param CGPA {NUM}; # Undergraduate GPA
param Res {NUM}; # Research Experience
param Chance {NUM}; # Chance of Admission
data Graduate_Admissions.dat;


#define regression coefficients
var beta_0;
var beta_1;
var beta_2;
var beta_3;
var beta_4;
var beta_5;
var beta_6;
var beta_7;

#define estimated chance (estimated y)
var estimated_chance {NUM};

# define auxiliary variables
var theta {NUM};

#define objective function
minimize chance: sum {i in NUM} theta[i];

#define constraints
subject to constr_1 {i in NUM}: estimated_chance[i] = beta_0 + beta_1 * GRE[i] + beta_2*TOEFL[i]+beta_3*Univ[i]+beta_4*SOP[i]+beta_5*LOR[i]+beta_6*CGPA[i]+beta_7*Res[i];
subject to constr_2 {i in NUM}: theta[i]>= Chance[i] -1* estimated_chance[i];
subject to constr_3 {i in NUM}: theta[i]>= -1*Chance[i] + estimated_chance[i];
subject to constr_4 {i in NUM}: theta[i]>=0;

