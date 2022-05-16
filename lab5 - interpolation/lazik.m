function [ x,y,f,xp,yp ] = lazik( K )
% K - funkcja zostanie sprobkowana w punktach na plaszczyznie ulozonych w siatke K x K punktow
% x - wspolrzedne x punktow probkowania
% y - wspolrzedne y punktow probkowania
% f - wartosc funkcji w punktach probkowania
% xp - wspolrzedne x punktow probkowania zgodne z torem jazdy lazika
% yp - wspolrzedne y punktow probkowania zgodne z torem jazdy lazika

% generacja polozenia probek
[x,y]=meshgrid(linspace(0,1,K),linspace(0,1,K));

w1=5; a1=30; x1=0.2; y1=0.3;
w2=6; a2=40; x2=0.6; y2=1.0;
w3=7; a3=50; x3=0.9; y3=0.5;
w4=6; a4=40; x4=0.6; y4=0.1;
w5=7; a5=70; x5=0.1; y5=0.95;
w6=-5; a6=10; x6=0.5; y6=0.5;
f=10+w1*exp(-a1*((x-x1).^2+(y-y1).^2))+w2*exp(-a2*((x-x2).^2+(y-y2).^2))+w3*exp(-a3*((x-x3).^2+(y-y3).^2))+w4*exp(-a4*((x-x4).^2+(y-y4).^2))+w5*exp(-a5*((x-x5).^2+(y-y5).^2))+w6*exp(-a6*((x-x6).^2+(y-y6).^2));

D = 100; % skala dystansu
x = x*D;
y = y*D;

% utworzenie wektora toru ruchu lazika
xp = x;
xp(2:2:end,:) = xp(2:2:end,end:-1:1);
xp = xp';
yp = y';

% macierz -> wektor
x = reshape(x,K*K,1);
y = reshape(y,K*K,1);
f = reshape(f,K*K,1);
xp = reshape(xp,K*K,1);
yp = reshape(yp,K*K,1);


end

