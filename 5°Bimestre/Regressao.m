%====================== REGRESSÃO LINEAR ====================================
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Considerations of the method

% Autor : Daniel Marques
% Electrical Engeneering - 2021
%
% ============================== Space for Functions ==========================
% ============================== Main Loop/Output =============================

folder = 'E:\Faculdade\Numerico\5°Bimestre\';
arqtime = 'Dados_QuartetoAnscombe.xlsx';

[~,~,RAW] = xlsread([folder arqtime]);
x1=cell2mat(RAW(4:end,1));
y1=cell2mat(RAW(4:end,2));
x2=cell2mat(RAW(4:end,3));
y2=cell2mat(RAW(4:end,4));
x3=cell2mat(RAW(4:end,5));
y3=cell2mat(RAW(4:end,6));
x4=cell2mat(RAW(4:end,7));
y4=cell2mat(RAW(4:end,8));

n=length(x1);
xt1=0;  xq1=0; R1a0=0;  xm1=0;  sy1=0;  dp1=0;  ep1=0; cd1=0;
xt2=0;  xq2=0; R1a1=0;  xm2=0;  sy2=0;  dp2=0;  ep2=0; cd2=0;
xt3=0;  xq3=0; R2a0=0;  xm3=0;  sy3=0;  dp3=0;  ep3=0; cd3=0;
yt1=0;  xy1=0; R2a1=0;  ym1=0;  va1=0;  cv1=0;  epa1=0;cc1=0;
yt2=0;  xy2=0; R3a0=0;  ym2=0;  va2=0;  cv2=0;  epa2=0;cc2=0;
yt3=0;  xy3=0; R3a1=0;  ym3=0;  va3=0;  cv3=0;  epa3=0;cc3=0;
xt4=0;  xq4=0; R4a0=0;  xm4=0;  sy4=0;  dp4=0;  ep4=0; cd4=0;
yt4=0;  xy4=0; R4a1=0;  ym4=0;  va4=0;  cv4=0;  epa4=0; cc4=0;
 for i=1:n,
     xt1=xt1+x1(i); yt1=yt1+y1(i);          %Calculo dos somatorios de xi
     xt2=xt2+x2(i); yt2=yt2+y2(i);
     xt3=xt3+x3(i); yt3=yt3+y3(i);
     xt4=xt4+x4(i); yt4=yt4+y4(i);
     
     xq1=xq1+x1(i).^2;                      %Calculo dos somatorios de xi^2
     xq2=xq2+x2(i).^2;
     xq3=xq3+x3(i).^2;
     xq4=xq4+x4(i).^2;
     
     xy1=xy1+x1(i)*y1(i);                    %Calculo dos somatorios de xy
     xy2=xy2+x2(i)*y2(i);
     xy3=xy3+x3(i)*y3(i);
     xy4=xy4+x4(i)*y4(i);
 end
     
xm1=xt1/n;  ym1=yt1/n;          %X medio e Y medio da reta 1
xm2=xt2/n;  ym2=yt2/n;          %X medio e Y medio da reta 2
xm3=xt3/n;  ym3=yt3/n;          %X medio e Y medio da reta 3
xm4=xt4/n;  ym4=yt4/n;          %X medio e Y medio da reta 4

R1a1=(n*xy1-xt1*yt1)/(n*(xq1)-xt1^1);   %Coef.A1 Reta 1
R1a0=ym1-R1a1*xm1;                      %Coef.A0 Reta 1
R2a1=(n*xy2-xt2*yt2)/(n*(xq2)-xt2^1);   %Coef.A1 Reta 2
R2a0=ym2-R2a1*xm2;                      %Coef.A0 Reta 2
R3a1=(n*xy3-xt3*yt3)/(n*(xq3)-xt3^1);   %Coef.A1 Reta 3
R3a0=ym3-R3a1*xm3;                      %Coef.A0 Reta 3
R4a1=(n*xy4-xt4*yt4)/(n*(xq4)-xt4^1);   %Coef.A1 Reta 3
R4a0=ym4-R4a1*xm4;                      %Coef.A0 Reta 3

% desvio padrao
for i=1:n,
    sy1=sy1+(y1(i)-ym1).^2               %somatorio de yi-ym para a reta 1
    sy2=sy2+(y2(i)-ym2).^2  
    sy3=sy3+(y3(i)-ym3).^2
    sy4=sy4+(y4(i)-ym4).^2
end    
va1=sy1/(n-1)                            %variância 1
va2=sy2/(n-1)                            %variância 2
va3=sy3/(n-1)                            %variância 3
va4=sy4/(n-1)                            %variância 4

dp1=sqrt(va1)          %desvio padrão da amostra 1
dp2=sqrt(va2)          %desvio padrão da amostra 2
dp3=sqrt(va3)          %desvio padrão da amostra 3
dp4=sqrt(va4)          %desvio padrão da amostra 4

cv1=(dp1/ym1)*100          %coeficiente de variação 1
cv2=(dp2/ym2)*100          %coeficiente de variação 2
cv3=(dp3/ym3)*100          %coeficiente de variação 3
cv4=(dp4/ym4)*100          %coeficiente de variação 3

% erro padrao e coeficientes 

for i=1:n,
    ep1=ep1+(y1(i)-R1a0-(R1a1*x1(i))).^2       %coef erro padrão de 1
    ep2=ep2+(y2(i)-R2a0-(R2a1*x2(i))).^2       %coef erro padrão de 2
    ep3=ep3+(y3(i)-R3a0-(R3a1*x3(i))).^2       %coef erro padrão de 3
    ep4=ep4+(y4(i)-R4a0-(R4a1*x4(i))).^2       %coef erro padrão de 3
end
epa1=sqrt(ep1/(n-2))  %erro padrao 1
epa2=sqrt(ep2/(n-2))  %erro padrao 2
epa3=sqrt(ep3/(n-2))  %erro padrao 3
epa4=sqrt(ep4/(n-2))  %erro padrao 4

cd1=(sy1-ep1)/sy1          %coeficiente de determinação 1
cd2=(sy2-ep2)/sy2          %coeficiente de determinação 2
cd3=(sy3-ep3)/sy3          %coeficiente de determinação 3
cd4=(sy4-ep4)/sy4          %coeficiente de determinação 3

cc1=sqrt(cd1)         %coeficiente de correlação 1
cc2=sqrt(cd2)         %coeficiente de correlação 2
cc3=sqrt(cd3)         %coeficiente de correlação 3
cc4=sqrt(cd4)         %coeficiente de correlação 3

%% função
x = [-30:0.5:30];
fx1 = R1a0+(R1a1.*x1(1,1:end));
fx2 = R2a0+(R2a1.*x3(1,1:end));
fx3 = R3a0+(R3a1.*x3(1,1:end));
fx4 = R4a0+(R4a1.*x4(1,1:end));


figure(1)
set(gcf,'color','w');
set(0, 'DefaultAxesFontSize', 12)
subplot(2,1,1); plot(x1(1,1:end),fx1); title('Função 1'); ylabel('f(x)'); xlabel('x');
subplot(2,1,2); plot(x2(1,1:end),fx2); title('Função 2'); ylabel('f(x)'); xlabel('x');
figure(2)
set(gcf,'color','w');
set(0, 'DefaultAxesFontSize', 12)
subplot(2,1,1); plot(x3(1,1:end),fx3); title('Função 3'); ylabel('f(x)');xlabel('x');
subplot(2,1,2); plot(x4(1,1:end),fx4); title('Função 4'); ylabel('f(x)');xlabel('x');

