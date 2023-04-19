---
title: "football"
output:
  pdf_document:
    keep_md: yes
date: "2023-03-23"
---




```
## Warning: package 'kableExtra' was built under R version 4.2.3
```

```
## 
## Attaching package: 'kableExtra'
```

```
## The following object is masked from 'package:dplyr':
## 
##     group_rows
```

```
## Rows: 4450 Columns: 21
## -- Column specification --------------------------------------------------------
## Delimiter: ","
## chr  (5): Date, HomeTeam, AwayTeam, FTR, HTR
## dbl (16): FTHG, FTAG, HTHG, HTAG, HS, AS, HST, AST, HF, AF, HC, AC, HY, AY, ...
## 
## i Use `spec()` to retrieve the full column specification for this data.
## i Specify the column types or set `show_col_types = FALSE` to quiet this message.
```

```
## tibble [4,450 x 22] (S3: tbl_df/tbl/data.frame)
##  $ HomeTeam: Factor w/ 37 levels "Arsenal","Aston Villa",..: 3 13 18 22 25 36 29 34 19 1 ...
##  $ AwayTeam: Factor w/ 37 levels "Arsenal","Aston Villa",..: 37 2 30 1 4 23 10 20 31 18 ...
##  $ FTHG    : num [1:4450] 1 0 1 0 0 1 0 1 4 0 ...
##  $ FTAG    : num [1:4450] 2 0 1 0 4 1 0 2 0 2 ...
##  $ FTR     : Factor w/ 3 levels "A","D","H": 1 2 2 2 1 2 2 1 3 1 ...
##  $ HTHG    : num [1:4450] 1 0 1 0 0 1 0 1 0 0 ...
##  $ HTAG    : num [1:4450] 1 0 0 0 1 1 0 1 0 0 ...
##  $ HTR     : Factor w/ 3 levels "A","D","H": 2 2 3 2 1 2 2 2 2 2 ...
##  $ HS      : num [1:4450] 16 13 11 6 13 18 6 14 26 10 ...
##  $ AS      : num [1:4450] 13 7 15 9 13 13 20 11 8 13 ...
##  $ HST     : num [1:4450] 8 9 4 1 7 11 3 8 19 6 ...
##  $ AST     : num [1:4450] 4 1 6 4 7 3 11 5 5 8 ...
##  $ HF      : num [1:4450] 14 10 17 9 9 11 12 16 9 11 ...
##  $ AF      : num [1:4450] 10 18 12 11 16 8 12 9 2 6 ...
##  $ HC      : num [1:4450] 12 2 6 2 3 7 4 6 7 9 ...
##  $ AC      : num [1:4450] 6 3 3 5 2 3 6 5 4 5 ...
##  $ HY      : num [1:4450] 4 2 4 3 1 2 2 3 0 2 ...
##  $ AY      : num [1:4450] 2 4 4 5 2 2 2 2 0 2 ...
##  $ HR      : num [1:4450] 0 0 0 0 1 0 0 0 0 1 ...
##  $ AR      : num [1:4450] 0 0 0 1 0 0 0 0 0 0 ...
##  $ Year    : chr [1:4450] "2011" "2011" "2011" "2011" ...
##  $ col_ind : int [1:4450] 1 2 3 4 5 6 7 8 9 10 ...
```










```
## Numerical Columns within dataset:  FTHG FTAG HTHG HTAG HS AS HST AST HF AF HC AC HY AY HR AR col_ind
```

```
## Categorical Columns within dataset:  HomeTeam AwayTeam FTR HTR Year
```

![](EDA_files/figure-latex/distributions-analysis-1.png)<!-- --> 

```
## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.
## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.
```

![](EDA_files/figure-latex/distributions-analysis-2.png)<!-- --> 

![](EDA_files/figure-latex/boxplot-1.png)<!-- --> 

![](EDA_files/figure-latex/correlation-plot-1.png)<!-- --> 

```
## NULL
```


```
## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter
```

![](EDA_files/figure-latex/observed-correlation-1.png)<!-- --> 

```
## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter
```

![](EDA_files/figure-latex/observed-correlation-2.png)<!-- --> 

![](EDA_files/figure-latex/WDL-team-1.png)<!-- --> 



![](EDA_files/figure-latex/team-strength-1.png)<!-- --> 


```
## tibble [4,157 x 15] (S3: tbl_df/tbl/data.frame)
##  $ HomeTeam: Factor w/ 37 levels "Arsenal","Aston Villa",..: 3 13 18 22 25 36 29 34 19 1 ...
##  $ AwayTeam: Factor w/ 37 levels "Arsenal","Aston Villa",..: 37 2 30 1 4 23 10 20 31 18 ...
##  $ FTR     : Factor w/ 3 levels "A","D","H": 1 2 2 2 1 2 2 1 3 1 ...
##  $ HTHG    : int [1:4157] 1 0 1 0 0 1 0 1 0 0 ...
##  $ HTAG    : int [1:4157] 1 0 0 0 1 1 0 1 0 0 ...
##  $ HST     : int [1:4157] 8 9 4 1 7 11 3 8 19 6 ...
##  $ AST     : int [1:4157] 4 1 6 4 7 3 11 5 5 8 ...
##  $ HF      : int [1:4157] 14 10 17 9 9 11 12 16 9 11 ...
##  $ AF      : int [1:4157] 10 18 12 11 16 8 12 9 2 6 ...
##  $ HC      : int [1:4157] 12 2 6 2 3 7 4 6 7 9 ...
##  $ AC      : int [1:4157] 6 3 3 5 2 3 6 5 4 5 ...
##  $ HY      : int [1:4157] 4 2 4 3 1 2 2 3 0 2 ...
##  $ AY      : int [1:4157] 2 4 4 5 2 2 2 2 0 2 ...
##  $ HR      : int [1:4157] 0 0 0 0 1 0 0 0 0 1 ...
##  $ AR      : int [1:4157] 0 0 0 1 0 0 0 0 0 0 ...
```



```
## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter

## Warning in par(usr): argument 1 does not name a graphical parameter
```

![](EDA_files/figure-latex/final-correlation-1.png)<!-- --> 

![](EDA_files/figure-latex/category-distribution-1.png)<!-- --> ![](EDA_files/figure-latex/category-distribution-2.png)<!-- --> ![](EDA_files/figure-latex/category-distribution-3.png)<!-- --> ![](EDA_files/figure-latex/category-distribution-4.png)<!-- --> 

![](EDA_files/figure-latex/home-strength-team-1.png)<!-- --> 
![](EDA_files/figure-latex/away-strength-team-1.png)<!-- --> 
