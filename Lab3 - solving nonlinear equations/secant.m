% l = x0, r = x1
function [iterations, approximation, diffs] = secant(f,l,r, EPS)
    x0 = l;
    x1 = r;
    iterations = 0;
    approximation = zeros(1);
    diffs = zeros(1);
    s=0;
    while true
        prev = s;
        fx1 = f(x1);
        fx0 = f(x0);
        s = x1 - (fx1*(x1-x0))/(fx1-fx0);
        if abs(f(s)) < EPS || abs(x1-x0) < eps
            return;
        elseif f(x0)*f(s)<0
            x1 = s;
        else
            x0 = s;
        end
        iterations = iterations+1;
        approximation(iterations)=s;
        if iterations > 1
            diffs(iterations-1)=abs(s-prev);
        end
    end 
end