This is an update business model for analyzing the breakeven point.

The inputs to this models are the following: n,p_energy,P1,P2,P3,FC,VC

n is degree of DR penetration, or how many households join in this DR program

p_energy is the monthly demand for curtailed energy from all household who are in this DR penetration.   

P1 is the wholesale price that generator sells the electricity in the general market, searched from online

P2 is the gas price which the local residents are used for heating

P3 is  the electricity price that local residents will pay if they use electricity to heat

FC is the installment cost of this DR program, given by professor

VC is variable cost of this DR program, given by professor



Columns in the final Table:

**Revenue_Generator**: p_energy * P1, which is the revenues that the generator could earn by selling those electricity that was original curtailed

**Loss_All_Household**: p_energy * (P2-P1), which is how much all household will lose if they switch from using gas to heat to using electricity to heat 

**Revenue_minus_Loss**: **Revenue_Generator** + **Loss_All_Household**, since we need to partial of the revenue to subsidy the loss of all household, this column is how much revenue left minus the subsidy

**Net_Income_for_Generator**: **Revenue_minus_Loss**/2. Half the revenue stays at generator

**Net_Income_for_Kaluza**: **Revenue_minus_Loss**/2. The result of net income goes to Kaluza

**Fixed_Cost_Kaluza**: n * FC. The fixed cost for installing the household equipment. The value is 0 for all months except the first one.

**Variable_Cost_Kaluza**: n * VC. The fixed cost for maintaining the infrastructure. It is a monthly cost

**Total_cost_Kaluza**: **Fixed_Cost_Kaluza** + **Variable_Cost_Kaluza**

**Net_Cash_flow_Kaluza** = **Net_Income_for_Kaluza**-**Total_cost_Kaluza**

