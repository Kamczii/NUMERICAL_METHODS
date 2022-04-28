clear
Edges = [1,1,2,2,2,3,3,3,4,4,5,5,6,6,7;4,6,4,5,3,6,5,7,6,5,4,6,4,7,6];
N=7;
B = sparse(Edges(2,:),Edges(1,:),1,N,N);

links = (1./sum(B(:,1:N)))';
A=spdiags(links,0,N,N);
I=speye(N);
d=0.85;
b_element = (1-d)/N;
b=zeros(N,1)+b_element;

M=I-(d*B*A);
r=M\b;
bar(r);