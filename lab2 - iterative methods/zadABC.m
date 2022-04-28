clc
clear all
close all
indeks = 184374;
N = 10;
density = 3; % parametr decydujący o gestosci polaczen miedzy stronami
[Edges] = generate_network(N, density);
B = sparse(Edges(2,:),Edges(1,:),1,N,N);

links = (1./sum(B(:,1:N)))';
A=spdiags(links,0,N,N);
I=speye(N);
d=0.85;
b_element = (1-d)/N;
b=zeros(N,1)+b_element;

M=I-(d*B*A);
save zadB indeks A B I b
time = [];
tic
r=M\b;
time(1) = toc;
save zadC indeks r
