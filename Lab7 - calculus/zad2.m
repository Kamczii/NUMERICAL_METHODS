clear all;
close all;
xmax=100;
ymax=100;
zmax=-50;

N = 1e5;

n1 = 0;
for i=1:N
    x = rand()*xmax;
    y = rand()*ymax;
    z = rand()*zmax;
    if z>glebokosc(x, y)
        n1 = n1+1;
    end
end
V = abs(xmax*ymax*zmax);
P = (n1/N)*V;
