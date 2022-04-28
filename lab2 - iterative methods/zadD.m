arr = [500 1000 3000 6000 12000];

time = zeros(1,5);
for i = 1:length(arr)
N = arr(i);
density = 10;
[Edges] = generate_network(N, density);

B = sparse(Edges(2,:),Edges(1,:),1,N,N);

links = (1./sum(B(:,1:N)))';
A=spdiags(links,0,N,N);
I=speye(N);
d=0.85;
b_element = (1-d)/N;
b=zeros(N,1)+b_element;

M=I-(d*B*A);

tic
r=M\b;
time(i) = toc;
end

figure();
bar(time);
title("Czas rozwiązania metodą bezpośrednią");
xlabel("N");
ylabel("Czas [s]");
saveas(gcf, "zadD_184374.png");
