clear all;
close all;
warning('off','all')
load('trajektoria2.mat');

N = 60;
[~, xa] = aproksymacjaWiel(n,x,N);
[~, ya] = aproksymacjaWiel(n,y,N);
[~, za] = aproksymacjaWiel(n,z,N);

plot3(x,y,z,'o');
hold on;
plot3(xa,ya,za,LineWidth=4);
grid on;
axis equal;
hold off;
title("Położenie drona bazując na lokalizacji i aproksymacji trajektoria2")
xlabel("x [m]");
ylabel("y [m]");
zlabel("z [m]");

saveas(gcf,'184374_czepiel_zad5.png');

errx = zeros(1,71);
erry = zeros(1,71);
errz = zeros(1,71);

for N = 1:71
    [~, xa] = aproksymacjaWiel(n,x,N);
    [~, ya] = aproksymacjaWiel(n,y,N);
    [~, za] = aproksymacjaWiel(n,z,N);

    errx(N) = sqrt(sum((x-xa).^2))/N;
    erry(N) = sqrt(sum((y-ya).^2))/N;
    errz(N) = sqrt(sum((z-za).^2))/N;
end

err = errx + erry + errz;

semilogy(1:71,err);
title("Błąd aproksymacji wielomianowej")
xlabel("Rząd aproksymacji [N]")
ylabel("Wartość błędu")
grid on
saveas(gcf,'184374_czepiel_zad5_b.png');

