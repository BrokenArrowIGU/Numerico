clc;
clear;
 
A = [3 -0.1 -0.2; 0.1 7 -0.3; 0.3 -0.2 10];
B = eye(length(A));
 
Inv = zeros(length(A));
for i=1:length(A)
    Inv(:,i) = InversaLU_piv (A, B(:,i));
end
 
A %Matriz Original 
Inv %Matriz Inversa
