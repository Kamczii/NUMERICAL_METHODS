clc
clear all
close all

% stałe
EPS = 1e-12;
START = 1;
FINISH = 50;

%metoda bisekcji
l = START;
r = FINISH;
[iterations, approximation, diffs] = bisection(@v,l,r, EPS);
%
figure;
semilogy(1:iterations,approximation)
xlabel("Numer iteracji");
ylabel("Kolejne przybliżenia");
title("3.1 Prędkość v[m/s] - Metoda bisekcji - kolejne przybliżenia"); 
saveas(gcf,'3_bisekcji_wykres_aproksymacji.png');
%
figure;
semilogy(2:iterations,diffs)
xlabel("Numer iteracji");
ylabel("Różnica przybliżeń");
title("3.2 Prędkość v[m/s] - Metoda bisekcji - różnica przybliżeń"); 
saveas(gcf,'3_bisekcji_wykres_przbliżeń.png');
%


%metoda siecznych
l = START;
r = FINISH;
[iterations, approximation, diffs] = secant(@v, l, r, EPS);
%
figure;
plot(1:iterations,approximation)
xlabel("Numer iteracji");
ylabel("Kolejne przybliżenia");
title("3.3 Prędkość v[m/s] - Metoda siecznych - kolejne przybliżenia"); 
saveas(gcf,'3_sieczna_wykres_aproksymacji.png');
%
figure;
semilogy(2:iterations,diffs)
xlabel("Numer iteracji");
ylabel("Różnica przybliżeń");
title("3.4 Prędkość v[m/s] -  Metoda siecznych - różnica przybliżeń"); 
saveas(gcf,'3_sieczna_wykres_przbliżeń.png');
%

%funkcja
function velocity = v(t)
    m0 = 150000; % kg
    q = 2700; % kg/s
    u = 2000; % m/s
    g = 9.81; % m/s^2
    velocity = u*log(m0/(m0-q*t))-g*t-750;
end
