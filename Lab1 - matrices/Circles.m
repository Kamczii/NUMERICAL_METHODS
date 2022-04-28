clear
a = 1;
r_max=0.2;
n_max=100;

n=1;
x(n)=a*rand;
y(n)=a*rand;
r(n)=r_max*rand;
fields(n)=pi*r(n).^2;
history(n)=fields(n);
draws = zeros(1,n_max);

while ((x(n)+r(n)) > a || ...
        (x(n)-r(n))<0 || ...
        (y(n)+r(n)) > a || ...
        (y(n)-r(n))<0)
    x(n)=a*rand;
    y(n)=a*rand;
    r(n)=r_max*rand;
    draws(n)=draws(n)+1;
end
draws_avg = sum(draws)/n;
field = pi*pow2(r(n));
plot_circ(x(n),y(n),r(n));
axis equal
hold on

n=n+1;
while(n<=n_max)
    draws(n)=0;
    valid = false;
    while ~valid
        x(n)=a*rand;
        y(n)=a*rand;
        r(n)=r_max*rand;
        draws(n)=draws(n)+1;
        if ((x(n)+r(n)) > a || ...
            (x(n)-r(n))<0 || ...
            (y(n)+r(n)) > a || ...
            (y(n)-r(n))<0)
            valid = false;
        else
            valid = true;
        end

        if valid 
            for i = 1:n-1
                if  sqrt((x(n)-x(i)).^2 + (y(n)-y(i)).^2) <= (r(n)+r(i))
                    valid = false;
                    break;
                end
            end
        end
    end
    
    fields(n)=pi*r(n).^2;
    draws_avg = cumsum(draws)/n;
    history(n)=history(n-1)+fields(n);
    fprintf(1, ' %s%5d%s%.3g\r ', 'n =',  n, ' S = ', fields(n))
    plot_circ(x(n),y(n),r(n));
    pause(0.01)
    n=n+1;
end

figure;
semilogx(history);
xlabel("n");
title("Powierzchnia całkowita"); 
saveas(gcf,'wykres1.png')

figure;
loglog(draws_avg);
xlabel("n");
title("Średnia liczba losowań");
 saveas(gcf,'wykres2.png')
