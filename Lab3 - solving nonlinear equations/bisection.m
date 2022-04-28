function [iterations, approximation, diffs] = bisection(f,l,r,eps)
    iterations = 0;
    approximation = zeros(1);
    diffs = zeros(1);
    c=0;
    while true
        prev = c;
        c = (l+r)./2;
        if abs(f(c)) < eps || abs(r-l) < eps
            return;
        elseif f(l).*f(c)<0
            r = c;
        else
            l = c;
        end
        iterations = iterations+1;
        approximation(iterations)=c;
        if iterations > 1
            diffs(iterations-1)=abs(c-prev);
        end
    end
end
