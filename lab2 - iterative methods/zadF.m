%F
clc;
close all;
clear all;

arr = [500 1000 3000 6000 12000];
iterations = zeros(length(arr),1);
res_norm = zeros(1);
time = zeros(1,5);
%loop
for i = 1:length(arr)
N = arr(i);
density = 10;
[Edges] = generate_network(N, density);
B = sparse(Edges(2,:),Edges(1,:),1,N,N);
links = (1./sum(B(:,1:N)))';
A=spdiags(links,0,N,N);
I=speye(N);
d=0.85;
M=I-(d*B*A);
N = arr(i);
L = tril(M,-1);
U = triu(M,1);
D = diag(diag(M));
b_element = (1-d)/N;
b=zeros(N,1)+b_element;
results = ones(N,1);
residuum = ones(N,1);
ITER=1;
res_i = 1;
%clock
tic
while norm(residuum) > 10^-14
    results = -(D+L)\(U*results)+(D+L)\b;
    residuum=M*results-b;
    if N == 1000
        res_norm(res_i)=norm(residuum);
        res_i=res_i+1;
    end
    ITER=ITER+1;
end
time(i) = toc;
iterations(i)=ITER;
end

figure();
plot(arr, time);
title("Czas analizy Gauss-Seidel");
xlabel("Rozmiar macierzy");
ylabel("Czas [s]");
saveas(gcf, "zadF_184374_1.png");

figure();
plot(arr, iterations);
title("Liczba iteracji Gauss-Seidel");
xlabel("Rozmiar macierzy");
ylabel("Liczba iteracji");
saveas(gcf, "zadF_184374_2.png");

figure();
semilogy(res_norm);
title("Wartości normy błędu rezydualnego dla N=1000");
xlabel("Iteracji");
ylabel("Norma błędu rezydualnego");
saveas(gcf, "zadF_184374_3.png");
