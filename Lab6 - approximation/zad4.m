close all;
warning('off','all')

load('trajektoria1.mat');

N = 50;
[~, xa] = aproksymacjaWiel(n,x,N);
[~, ya] = aproksymacjaWiel(n,y,N);
[~, za] = aproksymacjaWiel(n,z,N);

plot3(x,y,z,'o');
hold on;
plot3(xa,ya,za,LineWidth=4);
grid on;
axis equal;
hold off;
title("Położenie drona bazując na lokalizacji i aproksymacji trajektoria1")
xlabel("x [m]");
ylabel("y [m]");
zlabel("z [m]");

saveas(gcf,'184374_czepiel_zad4.png');