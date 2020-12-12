## Estimation

### Regression Model

* $y$ = $\beta_0$ + $\beta_1$$x_1$ + …. + $\beta_k$$x_k$ + $u$

* $k$ = 1: simple regression model

* $k$ > 1: multiple regression model



### ZCM Assumption

* Zero Conditional Mean Assumption

* $E$($u$ | $x_1$,….,$x_k$) = $E$($u$) = 0

* Require the average of $u$ to be the same irrespentive of the value of $x$'s
* It implies that the factors in $u$ are uncorrelated with  $x_1$ ,…., $x_k$



### SSR

* Sum of Squard Residuals (SSR)

* ![image-20201212020407125](/Users/lyndon/Library/Application Support/typora-user-images/image-20201212020407125.png)

* Good estiamtes should make SSR small



### SRF

* OLS Regression line / Sample Regression function (SRF)
* ![image-20201212020713684](/Users/lyndon/Library/Application Support/typora-user-images/image-20201212020713684.png)

* "Run a regression of $y$ = $x_1$ ,….., $x_k$" is to use OLS regression line to estimate the multiple regression model $y$ = $\beta_0$ + $\beta_1$$x_1$ + …. + $\beta_k$$x_k$ + $u$

* The coefficient on $x_j$ it the parital effect on $x_j$ on $y$ holding other x's fixed: ![image-20201212021100865](/Users/lyndon/Library/Application Support/typora-user-images/image-20201212021100865.png)

* SRF (Sample Regression Function) = PRF(Population Regression Function) "on average" on "when $n$ goes to infinity"

  

### R-Squared

* R-squared (coefficient of determination): 

  ![image-20201212021324942](/Users/lyndon/Library/Application Support/typora-user-images/image-20201212021324942.png)

* Larger $R^2$, better fit

* Interpretation of R-squared: the fraction of variation in $y$ that is explained by $x$' s. 

* R-squared alwasy increase as more independent variable is added to the model.



### Functional Forms 

![image-20201212023620901](/Users/lyndon/Library/Application Support/typora-user-images/image-20201212023620901.png)

### Variance of OLS Estimators

* ![image-20201212141004654](/Users/lyndon/Library/Application Support/typora-user-images/image-20201212141004654.png)
* The larger $\sigma^2$, the greater $Var($$\hat{\beta_j}$)​
* The larger the variation in $x_j$, the smaller $Var($$\hat{\beta_j}$)
* The larger $R_j^2$, the greater $Var($$\hat{\beta_j}$)



### Estimation of $\sigma^2$

* As the residual approximates $u$, the estimator of $\sigma^2$ is 

  ![image-20201212142405828](/Users/lyndon/Library/Application Support/typora-user-images/image-20201212142405828.png)

* Degree of freedom: $n-(k+1)$ = # of observations - # of estimated coefficients 

  

### Multicollinearity 

* Higher correlation between two or more independent variables

* Important variables can appear to be insignificant 

* $R_j^2$ is the R-squared from regression $x_j$ on all other $x$'s

* The higher correlation between $x_j$ and other $x$'s, the larger is  $R_j^2$ 

  

### Including irrelevant x 

* The population coefficient of that variable is 0
* In particular, E($\hat{\beta_3}$) = $\beta_3$ = 0



### Omitting relevant x

*  Omitted variable bias



### 







## Inference



## Analysis with dummy variables 



## Model Specification and data issues



## Binary Dependent Variable Models



## Panel Data Analysis



## Time Series Analysis

