clear all;
close all;
load('P_ref.mat')
a = 0;
b = 5;

fmin = f(0);
fmax = f(5);
fdiff = fmax-fmin;

err_cp = [];
err_ct = [];
err_cs = [];
err_mc = [];

for N = 5:50:10^4

    % Metoda prostokątów
    cp = 0;
    delta_x = (b-a)/N;
    for i=1:N
        xi = a + (i-1)*delta_x;
        xi1 = a + i*delta_x;
        cp = cp + f((xi+xi1)/2);
    end
    cp = cp * delta_x;
    err_cp = [err_cp, abs(cp - P_ref)];

    % Metoda trapezów - zamknięta
    ct = 0;
    for i=1:N
        xi = a + (i-1)*delta_x;
        xi1 = a + i*delta_x;
        ct = ct + ((f(xi1)+f(xi))/2);
    end
    ct = delta_x*ct;
    err_ct = [err_ct, abs(ct - P_ref)];

    % Metoda Simpsona
    cs = 0;
    for i=1:N
        xi = a + (i-1)*delta_x;
        xi1 = a + i*delta_x;
        cs = cs + (f(xi)+4*f((xi1+xi)/2) + f(xi1));
    end
    cs = (delta_x/6)*cs;
    err_cs = [err_cs, abs(cs - P_ref)];
    % Monte Carlo
    n1 = 0;
    for i=1:N
        x = rand()*(b-a)+a;
        y = rand()*fdiff+fmin;
        if y<f(x)
            n1 = n1+1;
        end
    end
    S = fdiff*(b-a);
    P = (n1/N)*S;
    err_mc = [err_mc, abs(P - P_ref)];
end

x = 5:50:10^4;
figure();
loglog(x, err_cp);
title('Błąd - metoda prostokątów');
xlabel('Liczba przedziałów [N]');
ylabel('Wartość błędu');
saveas(gcf, 'prostokatow_blad.png')

figure();
loglog(x, err_ct);
title('Błąd - metoda trapezów');
xlabel('Liczba przedziałów [N]');
ylabel('Wartość błędu');
saveas(gcf, 'trapezow_blad.png')

figure();
loglog(x, err_cs);
title('Błąd - metoda Simpsona');
xlabel('Liczba przedziałów [N]');
ylabel('Wartość błędu');
saveas(gcf, 'simpson_blad.png')

figure();
loglog(x, err_mc);
title('Błąd - metoda Monte Carlo');
xlabel('Liczba losowanych punktów [N]');
ylabel('Wartość błędu');
saveas(gcf, 'monte_carlo_blad.png')

N = 10^7;

times = zeros(4);

% Metoda prostokątów
 
tic;
cp = 0;
delta_x = (b-a)/N;
for i=1:N
    xi = a + (i-1)*delta_x;
    xi1 = a + i*delta_x;
    cp = cp + f((xi+xi1)/2);
end
cp = cp * delta_x;
times(1) = toc;

% Metoda trapezów - zamknięta
tic;
ct = 0;
for i=1:N
    xi = a + (i-1)*delta_x;
    xi1 = a + i*delta_x;
    ct = ct + ((f(xi1)+f(xi))/2);
end
ct = delta_x*ct;
times(2) = toc;
% Metoda Simpsona
tic;
cs = 0;
for i=1:N
    xi = a + (i-1)*delta_x;
    xi1 = a + i*delta_x;
    cs = cs + (f(xi)+4*f((xi1+xi)/2) + f(xi1));
end
cs = (delta_x/6)*cs;
times(3) = toc;
% Monte Carlo
tic;
n1 = 0;
for i=1:N
    x = rand()*(b-a)+a;
    y = rand()*fdiff+fmin;
    if y<f(x)
        n1 = n1+1;
    end
end
S = fdiff*(b-a);
P = (n1/N)*S;
times(4) = toc;

figure();
X = categorical({'Prostokątów','Trapezów','Simpsona','Monte Carlo'});
X = reordercats(X,{'Prostokątów','Trapezów','Simpsona','Monte Carlo'});
Y = times;
bar(X,Y)
title("Czas wykonania")
xlabel('Metoda');
ylabel('Czas [s]');
saveas(gcf, "czas_wykonania_wykres.png");


function f = f(t)
  SIGMA = 3;
  M = 10;
  
  f = (1/(SIGMA * sqrt(2 * pi))) * exp(-(t - M)^2 /(2 * SIGMA^2));
end
