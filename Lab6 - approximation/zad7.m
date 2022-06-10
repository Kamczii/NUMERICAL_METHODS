clear all;

load('trajektoria2.mat');

N = 60;
xa = aprox_tryg(n,x,N);
ya = aprox_tryg(n,y,N);
za = aprox_tryg(n,z,N);

plot3(x,y,z,'o');
hold on;
plot3(xa,ya,za,LineWidth=4);
grid on;
axis equal;
hold off;
title("Lok. rzeczywista i Trygonometryczna aproksymacja N=60")
xlabel("x [m]");
ylabel("y [m]");
zlabel("z [m]");

saveas(gcf,'184374_czepiel_zad7.png');

errx = zeros(1,71);
erry = zeros(1,71);
errz = zeros(1,71);

M = length(x);
for N = 1:71
    xa = aprox_tryg(n,x,N);
    ya = aprox_tryg(n,y,N);
    za = aprox_tryg(n,z,N);

    errx(N) = sqrt(sum((x-xa).^2))/M;
    erry(N) = sqrt(sum((y-ya).^2))/M;
    errz(N) = sqrt(sum((z-za).^2))/M;
end

err = errx + erry + errz;

semilogy(1:71,err);
title("Błąd aproksymacji trygonometrycznej");
xlabel("Rząd aproksymacji [N]");
ylabel("Wartość błędu");
grid on
saveas(gcf,'184374_czepiel_zad7_b.png');


% automatyczne szukanie rzędu aproksymacji
epsilon = 10^-4;
err = 1;
i = 0;

M = length(x);
while err > epsilon
    i=i+1;
    xa = aprox_tryg(n,x,i);
    ya = aprox_tryg(n,y,i);
    za = aprox_tryg(n,z,i);
    
    errx(N) = sqrt(sum((x-xa).^2))/M;
    erry(N) = sqrt(sum((y-ya).^2))/M;
    errz(N) = sqrt(sum((z-za).^2))/M;
    err = errx + erry + errz;
end

xa = aprox_tryg(n,x,i);
ya = aprox_tryg(n,y,i);
za = aprox_tryg(n,z,i);


plot3(x,y,z,'o');
hold on;
plot3(xa,ya,za,LineWidth=4);
grid on;
axis equal;
hold off;
title("Lok. rzeczywista i Trygonometryczna aproksymacja N = auto")
xlabel("x [m]");
ylabel("y [m]");
zlabel("z [m]");

saveas(gcf,'184374_czepiel_zad7_c.png');