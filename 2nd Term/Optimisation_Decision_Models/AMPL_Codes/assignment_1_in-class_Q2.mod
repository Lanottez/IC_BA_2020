var S_Bags >= 0;
var B_Bags >= 0;
var H_Bags >= 0;
var V_Bags >= 0;

maximize earning: 0.22*S_Bags + 0.20*B_Bags + 0.18*H_Bags + 0.18*V_Bags;

subject to carrots: 62.5*S_Bags + 50*B_Bags + 62.5*V_Bags <= 3750000;
subject to mushrooms: 75*S_Bags + 100*H_Bags <= 2000000;
subject to green_peppers: 62.5*S_Bags + 50*B_Bags + 75*H_Bags + 62.5*V_Bags <= 3475000;
subject to broccoli: 50*S_Bags + 75*B_Bags + 75*H_Bags + 62.5*V_Bags <= 3500000;
subject to corn: 72*B_Bags + 62.5*V_Bags <= 3750000;