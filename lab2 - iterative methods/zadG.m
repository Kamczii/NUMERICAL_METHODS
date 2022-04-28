clc;
clear all;
close all;

load Dane_Filtr_Dielektryczny_lab3_MN.mat;

tic
direct = M\b;
time(1)=toc();

L=tril(M,-1);
U=triu(M,1);
D=diag(diag(M));

jacobi = ones(length(M),1);
residuum = ones(length(M),1);
tic
while norm(residuum) > 10^-14 && ~isnan(norm(residuum)) 
    jacobi = -D\(L+U)*jacobi+D\b;
    residuum=M*jacobi-b;
end
if isnan(norm(residuum))
    disp("Jacobi nie zbiegł się!")
end

time(2)=toc;

gauss_seidel = ones(length(M),1);
residuum2 = ones(length(M),1);
tic
while norm(residuum2) > 10^-14 && ~isnan(norm(residuum))
    gauss_seidel = -(D+L)\(U*gauss_seidel)+(D+L)\b;
    residuum2=M*gauss_seidel-b;
end
if isnan(norm(residuum))
    disp("Gauss-Seidel nie zbiegł się!")
end
time(3)=toc;
bar(time);
