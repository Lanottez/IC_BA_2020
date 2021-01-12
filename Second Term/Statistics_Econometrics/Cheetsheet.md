## Estimation

### Regression Model

* $y$ = $\beta_0$ + $\beta_1$$x_1$ + …. + $\beta_k$$x_k$ + $u$
* $k$ = 1: simple regression model
* $k$ > 1: multiple regression model

### ZCM Assumption

* Zero Conditional Mean Assumption
* $E$($u$ | $x_1$,….,$x_k$) = $E$($u$) = 0
* Require the average of $u$ to be the same irrespective of the value of $x$'s
* It implies that the factors in $u$ are uncorrelated with  $x_j$

### SSR

* Sum of Squard Residuals (SSR)
* Indicates the goodness of estimate 
* $ SSR = \sum^n_{i=1}{\hat{u}^2_i} = \sum^n_{i=1}{(y_i - \hat{\beta}_0 - \hat{\beta}_1x_{i1}-…-\hat{\beta_k}x_{ik})^2} $
* Good estiamtes should make SSR small

### SRF

* OLS Regression line / Sample Regression function (SRF)
* $\hat{y}$ = $\hat{\beta_0} + \hat{\beta_1} x_1 + …. + \hat{\beta_k}x_k$ + $u$
* "Run a regression of $y$ = $x_1$ ,….., $x_k$" is to use OLS regression line to estimate the multiple regression model $y$ = $\beta_0$ + $\beta_1$$x_1$ + …. + $\beta_k$$x_k$ + $u$
* The coefficient on $x_j$ it the parital effect on $x_j$ on $y$ holding other x's fixed: $\Delta \hat{y} = \hat{\beta_j}\Delta x_j$ 
* A estimate of PRF
  * SRF (Sample Regression Function) = PRF(Population Regression Function) "on average" on "when $n$ goes to infinity"
* Interpretation of SRF
  * $\Delta \hat{y} = \hat{\beta}_1 \Delta x_1 + …+ \hat{\beta}_k \Delta x_k $ 
  * The coefficient on $x_j$ is the partial effect on $x_j$ on $y$ holding other $x$'s fixed: $\Delta \hat{y} = \hat{\beta}_j \Delta x_j $

### R-Squared

* R-squared (coefficient of determination) 
* $R^2 = \frac{SSE}{SST} = 1-\frac{SSR}{SST}$
* Larger $R^2$, better fit
* Interpretation of R-squared: the fraction of variation in $y$ that is explained by $x$' s. 
* R-squared alwasy increase as more independent variable is added to the model.

### Functional Forms 

![image-20201212023620901](/Users/lyndon/Library/Application Support/typora-user-images/image-20201212023620901.png)

### Unbiasdness of OLS Estimators

* With a good model, the OLS estimators are unbiased, i.e., $E(\hat{\beta_j}) = \beta_j$, j = 0,1,…k
* Unbiased estimators: $(\hat{\beta}_0,…,\hat{\beta}_k)$
  * They are centred around $(\beta_0,…,\beta_k)$
  * The correctly estimate $(\beta_0,…,\beta_k) $ on average
  * They will be "near" $(\beta_0,…,\beta_k)$ for a "typcial" sample

* Including irrelevant x 
  * The population coefficient of that variable is 0
  * In particular, E($\hat{\beta_3}$) = $\beta_3$ = 0
* Omitting relevant $x$ 
  * The estimated model is $\tilde{y} = \tilde{\beta}_0 + \tilde{\beta}_1x_1 $

### Variance of OLS Estimators

- $Var(\hat{\beta}_j) = \frac{\sigma^2}{SST_j(1-R^2_j)}, j = 1,…,k$

- The larger $\sigma^2$, the greater $Var($$\hat{\beta_j}$)​
- The larger the variation in $x_j$, the smaller $Var($$\hat{\beta_j}$)
- The larger $R_j^2$, the greater $Var($$\hat{\beta_j}$)

### Estimation of $\sigma^2$

* As the residual approximates $u$, the estimator of $\sigma^2$ is 
* $\hat{\sigma}^2 = \frac{SSR}{n-(k+1)} = \frac{\sum^n_{i=1}{\hat{u}^2_i} }{n-(k+1)}$ 

* Degree of freedom: $n-(k+1)$ = # of observations - # of estimated coefficients 

### Multicollinearity 

* Higher correlation between two or more independent variables
* Important variables can appear to be insignificant 
* $R_j^2$ is the R-squared from regression $x_j$ on all other $x$'s
* The higher correlation between $x_j$ and other $x$'s, the larger is  $R_j^2$ 
* What do we do:
  * Nothing: Multicollinearity weakens ability to interpret, but may allow us to draw more reliable causal inference 
  * Get rid of one of the offenders 
    * if the correlation between $x_{1}$ and $x_{2}$ is high. It typically means that they are measuring the same thing. So after controlling for $x_{1}$, $x_{2}$ becomes irrelevant, meaning that its partial impact on $y$ is very close to 0. Thus, based on the formula for omitted variable bias, the bias $\tilde{\delta}\beta_2$ from omitting $x_{2}$ is very small.

* 

### Omitting relevant x

*  Omitted variable bias

## Inference

### t-statistic 

* For Simple Null Hypothesis 
  * $H_0$ : $\beta_j$ = 0
  * t-statistic  = estimated coefficient / standard errors 

* Significance level: the probability of rejecting $H_0$ when it is true
* Two-side test:
  * The critical value is based on $(1-a/2)$ percentile in a $t$ distribution when $n-k-1$ df
  * Reject $H_0$ : $\beta_j$ = 0 if the absoluate value of the t statistic is greater than c, 
    * If we reject the null, we typicall say $x_j$ is statistically significant at the $a$ level 
    * If we fail to reject the null, we say $x_j$ is statistically insignificant at the $a$ level 
* To test a Linear Combination of Parameters
  * $H_0: \beta_1 - \beta_2 = 0$
  * t-statistic  =   $\beta_1 - \beta_2$ / standard errors

### p-values

* Alternative to classical approach
* Smaller the $p$-value, stronger the evidences against $H_0$
* If you want a one-sided alternative, just divide the two-sided $p$-value by 2
* For example, if p-value is 0.0234, we could say that we fail to reject $H_0$ at the 5% level. 

### Economically/Statistically Significant

* An independent variable is statistically significant when the size of the t-value is sufficiently large beyond the critical value $c$
* An independent variable is economically significant when the size of the estimate $\hat{\beta_j}$ is sufficiently large in comparison to the size of $y$

### Confidence Intervals 

* A ($1-a$)% CI is defined as [$\hat{\beta_j} - c * se(\hat{\beta_j}), \hat{\beta_j} + c * se(\hat{\beta_j})$], where $c$ is $(1-a/2$) percentiles in a $t_{n-k-1}$ distribution 
* reject $H_0$ at the $a$% significant level if (and only if) the $(1-a)$% CI does not contain $a_j$ 

### F-Test(a group of parameters)

* Exclusion restrictions:
  * whether a group of parameters are all equal to 0. 
  * Or, whether or not a group of $x$ variables has joint effect on $y$
* Testing exclusion restrictions
  * Unrestriced model: $y = \beta_0 + \beta_1x_1 + ..+\beta_kx_k + u$ 
  * Restricted model: $y = \beta_0 + \beta_1x_1 + ..+\beta_{k-q}x_{k-q} + u$ 
  * $H_0: \beta_{k-q+1} = 0,…,\beta_{k}=0$
* $F = \frac{(SSR_r - SSR_{ur})/q}{SSR_{ur}/(n-k-1)}$ under $H_0$
  * Or, $F = \frac{(R_{ur}^2 - R_{r}^2)/q}{1-R_{ur}^2/(n-k-1)}$ 
  * $q$ = number of restrictions, or $df_r-df_{ur}$
  * $n-k-1 = df_{ur}$ 
  * Reject if $F$ > $c$, where $c$ is the $F_{q, n-k-1}$ critical value
* If $H_0$ is rejected, we say $x_{k-q+1},….,x_{k}$ are jointly statistically significant, and at least one of the variables has impact on y
* If $H_0$ is not rejected, we say $x_{k-q+1},….,x_{k}$ are jointly statistically insignificant, which justifies dropping them from the model
* Symptom of multicollinearity: a group of variables are jointly significant but individual insignificant 
  * **Individual insignificant+ Individual insignificant -> jointly significant**
* It is possible that a variable is individually significant but when we test the joint significance of this variable, along with some other variables, we find them jointly insignificant
  * **Indiviudal insignificant + Individually significant -> jointly insignificant**

### F-Test(overall significance)

* when $k = q$, 
  * $H_0$: none of the independent variables has effect on $y$
* F = $\frac{R^2/k}{(1-R^2)/(n-k-1)}$ 

## Dummy variables 

### Independent Dummy Variable 

* Interpretion
  * $\widehat{wage}  = -1.57 - 1.81female + 0.572educ + 0.025exper + 0.141tenure$
    * A female work is predicted to earn $1.81 less than a male worker at the same level of educ, expr and tenure 
  * $\widehat{log(wage)}  = 0.501 - 0.301female + 0.087educ + 0.005exper + 0.017tenure$
    * A female work is predicted to earn 30.1% less than a male worker at the same level of educ, expr and tenure 

* Interactions with Dummies
  * $log(wage) = (\beta_0 + \delta_0female) + (\beta_1 + \delta_1femae)educ + u$
  * ![image-20201212165426809](/Users/lyndon/Library/Application Support/typora-user-images/image-20201212165426809.png)

### Dependent Dummy Variable

* Dependent variable is binary: $y$ represents whether or not
* $P(y=1|x) = E(y|x) = \beta_0 + \beta_1x_1 + …+ \beta_kx_k$: Linear Probability Model 
* $P(y=1|x)$ : Response Probability 
* $\beta_j$: the change in the probability of success cased by one-unit increase in $x_j$: $\Delta P(y=1|x) = \beta_j \Delta x_j $
* Issues: 
  * LPM is not suitable for modelling probabilities, because the predicated probability can be outside [0,1]
  * The conditional variance depends on $x$ 's(heteroskedasticity). It does not cause estimation bias but does invalidate the standard errors 

## Homoskedasticity vs Heteroskedasticity

### Homoskedasticity

* For the function of variance of OLS Estimators to work, $u$(error term) needed to be homoskedastic
* Assumption: $Var(u_i | x_{i1},..,x_{ik} = \sigma^2$ for i = 1,2,…n​  (It implies $Var(u_i) = \sigma^2$) 

### Heteroskedasticity

* OLS estimators are still unbiased
* The standard errors of the estimates are biased if we ignore heteroskedasticity
* We cannot use the usual t-statistic or F statistic for drawing inferences

### Heteroskedasticity Tests

* $H_0: E(u^2|x_1,x_2,…,x_k) = E(u^2) = \sigma^2$
  * $u^2 = \delta_0 + \delta_1x_1 + …+\delta_kx_k + v$
  * $H_0: \delta_1 = \delta_2 = … = \delta_k = 0$
  * Reject the null if $F$ is too large
* The Breusch-Pagan Test
  * Detects any linear forms of heteroskedasticity
  * OLS $y$ = $\beta_0$ + $\beta_1$$x_1$ + …. + $\beta_k$$x_k$ + $u$, and save the squared residuals $\hat{u}^2$
  * OLS $\hat{u}^2 = \delta_0 + \delta_1x_1 + …+\delta_kx_k + error$ and save the R-squared $R_{\hat{u}^2}^{2}$
  * $ F =  \frac{R_{\hat{u}^2}^{2}/k}{(1-R_{\hat{u}^2}^{2})/(n-k-1)}$
* The White Test
  * Allows for nonlinearities by using squares and crosspoducts of all the $x$'s 
  * OLS  $y$ = $\beta_0$ + $\beta_1$$x_1$ + …. + $\beta_k$$x_k$ + $u$, and save the squared residuals $\hat{u}$ and $\hat{y}$  
  * OLS $\hat{u}^2 = \delta_0 + \delta_1\hat{y} + \delta_2\hat{y}^2 + error$ and save the R-squared $R_{\hat{u}^2}^{2}$
  * $F =  \frac{R_{\hat{u}^2}^{2}/k}{(1-R_{\hat{u}^2}^{2})/(n-3)}$ 

### Heteroskedasticity-Robust procedure

* Adjust the OLS standard errors to make the $t$ stat (or $F$ valid in the presence of heteroskedasticity of unknown form)
  * The adjusted $t$-stat (or $F$ stat) is valid regardless of the type of heteroskedasticity in the population
* Denote $r.se(\hat{\beta_j})$ as robust standard error
* robust $t$ stat = $\frac{\hat{\beta_j} - a_j}{r.se(\hat{\beta_j})}$  
  * Always report robust standard errors for models with non-constant variance, including linear probability model and panel data model
  * For other models
    * Test for heteroskedasticity
    * Report robust standard erroers only if there is evidence of heteroskedasticity, because
      * usual standard errors are typically smaller
      * robust standard errors only have asymptotic justification
        * With small sample sizes, robust $t$ stat will not have a distribution close to $t$, and inferences will not be correct

### Functional Forms

* Logarithmic form
  * Used when:
    * the distribution of residuals is skewed or heteroskedastic 
    * for model interpretation (i.e., percentage change)
    * for multiplicative models
  * $log(y) = \beta_0 + \beta_1log(x) + u$ 
    * if x increases 1%, y will increase by $\beta_1$% 
  * $log(y) = \beta_0 + \beta_1x + u$
    * 100$\beta_1$ is approximately the percentage change in $y$ given 1 unit increase in $x$ 
  * $y = \beta_0 + \beta_1log(x) + u$ 
    * $\beta_1$/100 is approximately the unit change in $y$ given 1 unit increase in $x$ 
* Quadratic form
  * $y = \beta_0 + \beta_1x + \beta_2x^2 + u$ for model where we cannot interpret $\beta_1$ alone as measuring the change in $y$ with respect to $x$
  * $ \frac{ \Delta{\hat{y}}}{\Delta{x}} \approx $ ${\hat{\beta_1}} + 2{\hat{\beta_2}}x$
  * For  $\hat{\beta_{1}}$ > 0 and $\hat{\beta_{2}}$ < 0, 
    * $y$ is increasing in $x$ at first, but will eventually turn around and be decreasing in $x$
    * the turning point will be at $x^*$ = $|{\hat{\beta_1}} / 2{\hat{\beta_2}}|$

### Functional Form Misspecification

* A regression is misspecified when its functional form is incorrect and fails to properly account for the relation between the dependent variable and independent variables 
* If x affects y in percentage: use logs
* If the derivative of $x_{1}$ to vary with $x_{1}$, use quadratic

### RESET 

* REgression Specification Error Test
* Key idea: when the model $y = β_0 +β_{1}x_{1} +···+β_{k}x_{k} +u$ is correct, no functions of x’s should be significant when added to the model. Therefore, the squared and cubed fitted values, which are functions of x’s, should be insignificant when added to the correct model
* Procedures:
  * OLS  $y$ = $\beta_0$ + $\beta_1$$x_1$ + …. + $\beta_k$$x_k$ + $u$, and save the fitted value $\hat{y}$
  * Test $H_0$ : $y$ = $\beta_0 + \beta_1 x_1 + …. + \beta_kx_k +\delta_1 \hat{y}^2$  + $\delta_2 \hat{y}^3$
  * Reject $H_0$ when $F$ stat > $c$

### Goodness-of-Fit: Adjusted R-Squared

* R-Squared 
  * $R^2 = 1-\frac{SSR}{SST}$
  * $R^2$ is the proportion of variation in $y$ that is explained by $x$'s 
  * $R^2$ always increases as more independent variables are added to the model
  * To compare different models, we need to take into account the  model size(number of independent variables)
* Adjusted R-Squard
  * $\bar{R}^2$ = $1-\frac{SSR/(n-k-1)}{SST/(n-1)}$
  * You can compare the fit of 2 models (with the same $y$) by comparing the adj-$R^2$
  * You cannot use the adj-$R^2$ to compare models where $y$ are in different function forms 

### Goodness-of-Fit: Information Criteria

* $AIC$ selecting a model tries to balance the conflicting demand of accuracy (fit) and simplicity (small number of variables)
  * $AIC = nln(SSR/n) + 2k$
  * $AIC$ for a single model is not very meaningful 
    * Models with smaller $AIC$ are preferred
    * Rule of thumb: Model with $AIC$ not differing by 2 should be treated as equally adequate
    * Larger differences in $AIC$ indicate significant differences between the quality of models
* $BIC$
  * modificaton of $AIC$
  * $BIC = nln(SSR/n) + kln(n)$
  * Difference between $AIC$ and $BIC$ is in the severity of penality for $k$ 
* $AIC_c$
  * $AIC_c = AIC + \frac{2(k+2)(k+3)}{n-k-3}$
  * Typically used for small samples
  * Correction to $AIC$ is small for large $n$ and moderate $k$
  * Correction is large when $n$ is small and $k$ is large 

### Gauss-Markov Assumptions

* MLR1-4 are required for OLS estimators to be unbiased 
* MLR1: in the population model, $y$ is related to $x$'s by $y = \beta_0 + \beta_1x_1 + … +   \beta_kx_k + u$ 
  * Common causes lead to violation of this assumption:
    * functional form misspecification: log vs level form, omitting quadratic term
  * Identification of assumption violation
    *  RESET, Residual plots
* MLR2 ${(x_{i1},…,x_{ik},y_i),i=1,2,..n}$ with $n>k+1$ is a random sample drawn from the popualtion model
  * If any observation has missing data on one of the variables in the model, it cannot be used.
  * A problem can arise if the data is missing in a systematic way. The sample becomes nonrandom(violation to MLR2)
  * **Exogenous sample selection**: if the sample is chosen on the basis of an independent variable $x$, the OLS estimators will still be unbiased 
  * **Endogenous sample selection**: if the sample is chosen on the basis of the dependent variable $y$, the OLS estimators will be biased, and zero-conditional mean assumption fails 
* MLR3 (no perfect collinearity): none of $x$'s is constant and there is no perfect linear relationships among $x$'s 
  * Common cause lead to violation of this assumption
    * Multiple variables measure the same thing, dummy variables trap
  * Identification of assumption violation:
    * Routinely reported by statistic softwares
* MLR4 (zero conditonal mean): the disturbance $u$ satifies $E(u|x_1,…x_k) = 0$ for any given value of $(x_1,….x_k)$ 
  * Common causes lead to violation of this assumption
    * Missing important variables in the model
  * Identification of assumption violation
    * No test for this
  * Mitigation
    * Direction of omitted variable bias
    * If we can find a variable that is closely related to the omitted variable, we can use it as an instrument variable or a proxy variable 

* MLR5 (homoskedasticity):  $Var(u_i|x_{i1},…,x_{ik}) = \sigma^2$ for $i = 1,2,…,n$. (It implies $Var(u_{i} =\sigma^2 )$)
  * Common causes lead to violation of this assumption
    * Data issue
  * Identification of assumption violation
    * Residual plots, Breusch-Pagan test, White test
  * Solutions
    * Robust standard errors

## Binary Dependent Variable Models

### Logits and Probits

* Alternative Way to model the LPM as a function: 
  * G($ \beta_0 + \beta_1x_1 + ..+\beta_kx_k + u$),  where 0 < G($Z$) < 1
* Logistic Function: the cumulative distribution function for a standard logistic random variable
  * $G(z) = \frac{exp(z)}{1+exp(z)}$
* Probit Model: the standard normal cumulative distribution function
  * G($z$) = $\Phi(z)$ = $$\int_{-\infty}^z \frac{1}{\sqrt{2\pi}}exp(-\frac{v^2}{2}) \,dv$$ 
* No need to prefer one over the other 

### Interpretation

* What is the effect of $x_j$ on $P(y  = 1|x)$ 
* For linear case: it is the coefficient on $x_j$ 
* For non-linear logit and probit model:
  * Since we are bounding the dependent variable using a non-linear function, the margin effect depends on all the estimates and their values 
  * The effects on $x_j$ on the response probability is roughly: 
  * $\Delta P(y=1|x) \approx [g(\hat{\beta_0} + \hat{\beta_1}x_1 + ..+\hat{\beta_k}x_k)\hat{\beta_j}] \Delta x_j $ 
  * APE(average partial effect): we average the individual partial effects accross the sample

### The likelihood Ratio Test

* used to test exclusion restrictions 
* Maximum Likelihood Estimation (MLE)
  * log-likelihood function: $l_i(\beta) = y_ilog[G(z_i)] + (1-y_i)log[1-G(z_i)]$
  * log-likelihoold for a sample: $L(\beta) = \sum^{n}_{i=1}{l_i(\beta)}$ 
  * The MLE of $\beta$, denoted as $\hat\beta$, maximizes $L(\beta)$
* Likelihood ratio statistic: $LR = 2(L_{ur} - L_r)$
* Reject the null $H_0 : \beta_{k-q+1} = 0, … , \beta_k = 0$ if LR > c
* Goodness of Fit
  * Pseudo R-squared: is based on the log likelihood and defined as $1-L_{ur}/L_r$ where $L_{ur}$  is the log-likelihood for the estimated model, and $L_r$ is the log-likelihood in the model with only an intercept
  * AIC: $AIC = 2k-2L$, where $k$ is the number of independent variables and $L$ is the log-likelihood for the model
  * BIC: $ln(n)k - 2L$ 

### Confusion Matrix

* Actual: True/False
* Predicted: Positive/Negative
* False Positive ~  Type I error 
  * mistakenly predict a non-pregnant customer to be pregnant 
* False Negative ~ Type II error 
  * mistakenly predict a pregnant customer to be non-pregnant 
* Metrics: 
  * Accuracy (all correct/all) = $\frac{TP+TN}{TP+TN+FP+FN}$
  * Precison (true positives/predicted positives) = $\frac{TP}{TP+FP}$
  * Recall (true positives/all actual postives) = $\frac{TP}{TP+FN}$ 

## Panel Data Analysis

### Fixed Effects Model

* If the omitted variables are fixed over time, then we can decompose the error into two parts: factors that vary over time and those do not
* $y_{it} = \beta_0 + \delta_0d2_t + \beta_1x_{it1} + … +  \beta_kx_{itk} + a_i + u_{it}$, t = 1,2
  * $a_{i}$ is the fixed effect (invariant to $t$) that represents factors specific to individual $i$ (allowed to be correlated with $x_{it}$)
  * $u_{it}$ is called the idiosyncartic error that represents unobserved factors varying both over time and across sections (typically assumed to be uncorrelated with $x_{it}$)

### First Differencing

* Write the model seperately:
  * $y_{i1} = \beta_0 + \delta_0*0 + \beta_1x_{i11} + … +  \beta_kx_{i1k} + a_i + u_{i1}$, t = 1
  * $y_{i2} = \beta_0 + \delta_0 *1 + \beta_1x_{i12} + … +  \beta_kx_{i2k} + a_i + u_{i2}$, t = 2
* Subtracting the first equation from the second one gives
  * $y_{i} = \beta_0 + \beta_1\Delta x_{i1} + … +  \beta_k\Delta x_{ik}  +  \Delta u_{i}$
* Example: $\Delta crmret = 15.40 + 2.22 \Delta umen$
  * One percentage point rise in unemployment rate increases 2.22 crimes per 1,000 people 
  * The crimes per 1,000 people increased by 15.4 in 1987, in comparison to 1982

### Fixed effects  

* Consider a model with a single independent variable
  * $y_{it} = \beta_0 + \beta_1x_{it} + a_{i} + u_{it}$
* The average over time for individual $i$ is 
  * $\bar{y}_{i} = \beta_0 + \beta_1\bar{x}_{1} + a_{i} + \bar{u}_{i}$
* If we subtract the average from $y_{it}$, we have
  * $y_{it} - \bar{y}_i = \beta_1(x_{it} - \bar{x}_i) + (u_{it}-\bar{u}_i)$ 
* Each individual has been "de-manded" for all variables, which eliminates the fixed effect