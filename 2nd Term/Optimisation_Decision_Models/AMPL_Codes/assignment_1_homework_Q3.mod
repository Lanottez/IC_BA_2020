var RProject >= 0;
var GProject >= 0;
var IProject >= 0;

maximize earnings: 25000*RProject + 30000*GProject + 20000*IProject;

subject to strategy_consultants: 2*RProject + 3*GProject + IProject <=100;
subject to IT_exports: RProject + GProject + 3*IProject <= 75;

