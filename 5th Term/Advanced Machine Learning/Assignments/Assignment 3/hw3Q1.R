library(R.matlab)
library(plotrix)
library(ggplot2)
library(tidyverse)

data = readMat("/Users/zhengyutong/Desktop/AML/作业/Assignment_3/olivettifaces.mat")  
faces = data$faces
dim(faces)
NumFaces = length(faces[1,])
NumPixels = length(faces[,1]) 

NumFacesPCA = 400 # Number of images we will use for PCA 
set.seed(1)
index = sample(1:NumFaces, NumFacesPCA)
TrainImages = data.matrix(faces[,index])

n = 2
par(mfrow = c(n,n),     # 2x2 layout
    oma = c(0, 0, 0, 0), # controls rows for text at outer  margins
    mar = c(1, 1, 0, 0), # space for one row of text at ticks and to separate plots
    mgp = c(2, 1, 0),    # axis label at 2 rows distance, tick labels at 1 row
    xpd = NA)  
for (i in 1:n^2){
  Face = matrix(TrainImages[,i],sqrt(NumPixels),byrow=FALSE)
  color2D.matplot(Face,axes=FALSE)
}

pr.out <- prcomp(t(TrainImages), scale = T)
names(pr.out)
loading <- pr.out$rotation
scale <- pr.out$scale
center <- pr.out$center
x <- pr.out$x

k <- 50
ReconstructFace <- center + scale * loading[,1:k] %*% t(x[,1:k])
dim(ReconstructFace)

par(mfrow = c(n,n),     # 2x2 layout
    oma = c(0, 0, 0, 0), # controls rows for text at outer  margins
    mar = c(1, 1, 0, 0), # space for one row of text at ticks and to separate plots
    mgp = c(2, 1, 0),    # axis label at 2 rows distance, tick labels at 1 row
    xpd = NA)  
for (i in 1:n^2){
  Face = matrix(ReconstructFace[,i],sqrt(NumPixels),byrow=FALSE)
  color2D.matplot(Face,axes=FALSE)
}