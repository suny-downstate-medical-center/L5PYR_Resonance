%paths = {'ih_m0.15_im_0.15', 'ih_0.0_im_0.15', 'ih_0.15_im_0.15', 'ih_m0.15_im_0.0', 'ih_0.0_im_0.0', 'ih_0.15_im_0.0', 'ih_m0.15_im_m0.15', 'ih_0.0_im_m0.15', 'ih_0.15_im_0.15'};

paths = {'ih_m0.15_im_0.0', 'ih_0.0_im_0.0', 'ih_0.15_im_0.0'};

dista = [];
ZinResAmpa = [];
distb = [];
ZinResAmpb = [];
distc = [];
ZinResAmpc = [];
pname = paths{1};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            dista = [dista file.dist(j)];
            ZinResAmpa = [ZinResAmpa file.ZinResAmp(j)];
        end
    end
end
pname = paths{2};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distb = [distb file.dist(j)];
            ZinResAmpb = [ZinResAmpb file.ZinResAmp(j)];
        end
    end
end
pname = paths{3};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distc = [distc file.dist(j)];
            ZinResAmpc = [ZinResAmpc file.ZinResAmp(j)];
        end
    end
end
figure('units','normalized','outerposition',[0 0 1 1]);
subplot(2,3,1)
p1 = scatter(dista, ZinResAmpa, 'b');
hold on 
p2 = scatter(distb, ZinResAmpb, 'g');
p3 = scatter(distc, ZinResAmpc, 'r');
legend([p1,p2,p3], {'-15%', '0%', '15%'})
ylabel('Resonance Z_i_n Amplitude (M\Omega)')
set(gca, 'FontSize', 14)

dista = [];
ZinResFreqa = [];
distb = [];
ZinResFreqb = [];
distc = [];
ZinResFreqc = [];
pname = paths{1};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            dista = [dista file.dist(j)];
            ZinResFreqa = [ZinResFreqa file.ZinResFreq(j)];
        end
    end
end
pname = paths{2};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distb = [distb file.dist(j)];
            ZinResFreqb = [ZinResFreqb file.ZinResFreq(j)];
        end
    end
end
pname = paths{3};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distc = [distc file.dist(j)];
            ZinResFreqc = [ZinResFreqc file.ZinResFreq(j)];
        end
    end
end
subplot(2,3,2)
p1 = scatter(dista, ZinResFreqa, 'b');
hold on 
p2 = scatter(distb, ZinResFreqb, 'g');
p3 = scatter(distc, ZinResFreqc, 'r');
title('Global Changes in Ih Conductance')
ylabel('Resonance Frequency (Hz)')
set(gca, 'FontSize', 14)

dista = [];
QfactorIna = [];
distb = [];
QfactorInb = [];
distc = [];
QfactorInc = [];
pname = paths{1};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            dista = [dista file.dist(j)];
            QfactorIna = [QfactorIna file.QfactorIn(j)];
        end
    end
end
pname = paths{2};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distb = [distb file.dist(j)];
            QfactorInb = [QfactorInb file.QfactorIn(j)];
        end
    end
end
pname = paths{3};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distc = [distc file.dist(j)];
            QfactorInc = [QfactorInc file.QfactorIn(j)];
        end
    end
end
subplot(2,3,3)
p1 = scatter(dista, QfactorIna, 'b');
hold on 
p2 = scatter(distb, QfactorInb, 'g');
p3 = scatter(distc, QfactorInc, 'r');
ylabel('Resonance Strength (Q-factor)')
set(gca, 'FontSize', 14)

dista = [];
ZcResFreqa = [];
distb = [];
ZcResFreqb = [];
distc = [];
ZcResFreqc = [];
pname = paths{1};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            dista = [dista file.dist(j)];
            if isstr(file.ZcResFreq(j))
                ZcResFreqa = [ZcResFreqa NaN];    
            else
                ZcResFreqa = [ZcResFreqa file.ZcResFreq(j)];
            end
        end
    end
end
pname = paths{2};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distb = [distb file.dist(j)];
            if isstr(file.ZcResFreq(j))
                ZcResFreqb = [ZcResFreqb NaN];    
            else
                ZcResFreqb = [ZcResFreqb file.ZcResFreq(j)];
            end
        end
    end
end
pname = paths{3};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distc = [distc file.dist(j)];
            if isstr(file.ZcResFreq(j))
                ZcResFreqc = [ZcResFreqc NaN];    
            else
                ZcResFreqc = [ZcResFreqc file.ZcResFreq(j)];
            end
        end
    end
end
subplot(2,3,4)
p1 = scatter(dista, ZcResFreqa, 'b');
hold on 
p2 = scatter(distb, ZcResFreqb, 'g');
p3 = scatter(distc, ZcResFreqc, 'r');
ylabel('Transfer Frequency (Hz)')
set(gca, 'FontSize', 14)

dista = [];
ZinSynchFreqa = [];
distb = [];
ZinSynchFreqb = [];
distc = [];
ZinSynchFreqc = [];
pname = paths{1};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            dista = [dista file.dist(j)];
            if isstr(file.ZinSynchFreq(j))
                ZinSynchFreqa = [ZinSynchFreqa NaN];    
            else
                ZinSynchFreqa = [ZinSynchFreqa file.ZinSynchFreq(j)];
            end
        end
    end
end
pname = paths{2};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distb = [distb file.dist(j)];
            if isstr(file.ZinSynchFreq(j))
                ZinSynchFreqb = [ZinSynchFreqb NaN];    
            else
                ZinSynchFreqb = [ZinSynchFreqb file.ZinSynchFreq(j)];
            end
        end
    end
end
pname = paths{3};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distc = [distc file.dist(j)];
            if isstr(file.ZinSynchFreq(j))
                ZinSynchFreqc = [ZinSynchFreqc NaN];    
            else
                ZinSynchFreqc = [ZinSynchFreqc file.ZinSynchFreq(j)];
            end
        end
    end
end
subplot(2,3,5)
p1 = scatter(dista, ZinSynchFreqa, 'b');
hold on 
p2 = scatter(distb, ZinSynchFreqb, 'g');
p3 = scatter(distc, ZinSynchFreqc, 'r');
ylabel('Synchronous Frequency (Hz)')
set(gca, 'FontSize', 14)

dista = [];
ZinLeadPhaseBWa = [];
distb = [];
ZinLeadPhaseBWb = [];
distc = [];
ZinLeadPhaseBWc = [];
pname = paths{1};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            dista = [dista file.dist(j)];
            if isstr(file.ZinLeadPhaseBW(j))
                ZinLeadPhaseBWa = [ZinLeadPhaseBWa NaN];    
            else
                ZinLeadPhaseBWa = [ZinLeadPhaseBWa file.ZinLeadPhaseBW(j)];
            end
        end
    end
end
pname = paths{2};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distb = [distb file.dist(j)];
            if isstr(file.ZinLeadPhaseBW(j))
                ZinLeadPhaseBWb = [ZinLeadPhaseBWb NaN];    
            else
                ZinLeadPhaseBWb = [ZinLeadPhaseBWb file.ZinLeadPhaseBW(j)];
            end
        end
    end
end
pname = paths{3};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distc = [distc file.dist(j)];
            if isstr(file.ZinLeadPhaseBW(j))
                ZinLeadPhaseBWc = [ZinLeadPhaseBWc NaN];    
            else
                ZinLeadPhaseBWc = [ZinLeadPhaseBWc file.ZinLeadPhaseBW(j)];
            end
        end
    end
end
subplot(2,3,6)
p1 = scatter(dista, ZinLeadPhaseBWa, 'b');
hold on 
p2 = scatter(distb, ZinLeadPhaseBWb, 'g');
p3 = scatter(distc, ZinLeadPhaseBWc, 'r');
ylabel('Leading Phase Bandwidth (Hz)')
set(gca, 'FontSize', 14)

paths = {'ih_0.0_im_m0.15', 'ih_0.0_im_0.0', 'ih_0.0_im_0.15'};
dista = [];
ZinResAmpa = [];
distb = [];
ZinResAmpb = [];
distc = [];
ZinResAmpc = [];
pname = paths{1};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            dista = [dista file.dist(j)];
            ZinResAmpa = [ZinResAmpa file.ZinResAmp(j)];
        end
    end
end
pname = paths{2};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distb = [distb file.dist(j)];
            ZinResAmpb = [ZinResAmpb file.ZinResAmp(j)];
        end
    end
end
pname = paths{3};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distc = [distc file.dist(j)];
            ZinResAmpc = [ZinResAmpc file.ZinResAmp(j)];
        end
    end
end
figure('units','normalized','outerposition',[0 0 1 1]);
subplot(2,3,1)
p1 = scatter(dista, ZinResAmpa, 'b');
hold on 
p2 = scatter(distb, ZinResAmpb, 'g');
p3 = scatter(distc, ZinResAmpc, 'r');
legend([p1,p2,p3], {'-15%', '0%', '15%'})
ylabel('Resonance Z_i_n Amplitude (M\Omega)')
set(gca, 'FontSize', 14)

dista = [];
ZinResFreqa = [];
distb = [];
ZinResFreqb = [];
distc = [];
ZinResFreqc = [];
pname = paths{1};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            dista = [dista file.dist(j)];
            ZinResFreqa = [ZinResFreqa file.ZinResFreq(j)];
        end
    end
end
pname = paths{2};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distb = [distb file.dist(j)];
            ZinResFreqb = [ZinResFreqb file.ZinResFreq(j)];
        end
    end
end
pname = paths{3};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distc = [distc file.dist(j)];
            ZinResFreqc = [ZinResFreqc file.ZinResFreq(j)];
        end
    end
end
subplot(2,3,2)
p1 = scatter(dista, ZinResFreqa, 'b');
hold on 
p2 = scatter(distb, ZinResFreqb, 'g');
p3 = scatter(distc, ZinResFreqc, 'r');
title('Global Changes in Im Conductance')
ylabel('Resonance Frequency (Hz)')
set(gca, 'FontSize', 14)

dista = [];
QfactorIna = [];
distb = [];
QfactorInb = [];
distc = [];
QfactorInc = [];
pname = paths{1};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            dista = [dista file.dist(j)];
            QfactorIna = [QfactorIna file.QfactorIn(j)];
        end
    end
end
pname = paths{2};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distb = [distb file.dist(j)];
            QfactorInb = [QfactorInb file.QfactorIn(j)];
        end
    end
end
pname = paths{3};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distc = [distc file.dist(j)];
            QfactorInc = [QfactorInc file.QfactorIn(j)];
        end
    end
end
subplot(2,3,3)
p1 = scatter(dista, QfactorIna, 'b');
hold on 
p2 = scatter(distb, QfactorInb, 'g');
p3 = scatter(distc, QfactorInc, 'r');
ylabel('Resonance Strength (Q-factor)')
set(gca, 'FontSize', 14)

dista = [];
ZcResFreqa = [];
distb = [];
ZcResFreqb = [];
distc = [];
ZcResFreqc = [];
pname = paths{1};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            dista = [dista file.dist(j)];
            if isstr(file.ZcResFreq(j))
                ZcResFreqa = [ZcResFreqa NaN];    
            else
                ZcResFreqa = [ZcResFreqa file.ZcResFreq(j)];
            end
        end
    end
end
pname = paths{2};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distb = [distb file.dist(j)];
            if isstr(file.ZcResFreq(j))
                ZcResFreqb = [ZcResFreqb NaN];    
            else
                ZcResFreqb = [ZcResFreqb file.ZcResFreq(j)];
            end
        end
    end
end
pname = paths{3};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distc = [distc file.dist(j)];
            if isstr(file.ZcResFreq(j))
                ZcResFreqc = [ZcResFreqc NaN];    
            else
                ZcResFreqc = [ZcResFreqc file.ZcResFreq(j)];
            end
        end
    end
end
subplot(2,3,4)
p1 = scatter(dista, ZcResFreqa, 'b');
hold on 
p2 = scatter(distb, ZcResFreqb, 'g');
p3 = scatter(distc, ZcResFreqc, 'r');
ylabel('Transfer Frequency (Hz)')
set(gca, 'FontSize', 14)

dista = [];
ZinSynchFreqa = [];
distb = [];
ZinSynchFreqb = [];
distc = [];
ZinSynchFreqc = [];
pname = paths{1};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            dista = [dista file.dist(j)];
            if isstr(file.ZinSynchFreq(j))
                ZinSynchFreqa = [ZinSynchFreqa NaN];    
            else
                ZinSynchFreqa = [ZinSynchFreqa file.ZinSynchFreq(j)];
            end
        end
    end
end
pname = paths{2};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distb = [distb file.dist(j)];
            if isstr(file.ZinSynchFreq(j))
                ZinSynchFreqb = [ZinSynchFreqb NaN];    
            else
                ZinSynchFreqb = [ZinSynchFreqb file.ZinSynchFreq(j)];
            end
        end
    end
end
pname = paths{3};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distc = [distc file.dist(j)];
            if isstr(file.ZinSynchFreq(j))
                ZinSynchFreqc = [ZinSynchFreqc NaN];    
            else
                ZinSynchFreqc = [ZinSynchFreqc file.ZinSynchFreq(j)];
            end
        end
    end
end
subplot(2,3,5)
p1 = scatter(dista, ZinSynchFreqa, 'b');
hold on 
p2 = scatter(distb, ZinSynchFreqb, 'g');
p3 = scatter(distc, ZinSynchFreqc, 'r');
ylabel('Synchronous Frequency (Hz)')
set(gca, 'FontSize', 14)

dista = [];
ZinLeadPhaseBWa = [];
distb = [];
ZinLeadPhaseBWb = [];
distc = [];
ZinLeadPhaseBWc = [];
pname = paths{1};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            dista = [dista file.dist(j)];
            if isstr(file.ZinLeadPhaseBW(j))
                ZinLeadPhaseBWa = [ZinLeadPhaseBWa NaN];    
            else
                ZinLeadPhaseBWa = [ZinLeadPhaseBWa file.ZinLeadPhaseBW(j)];
            end
        end
    end
end
pname = paths{2};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distb = [distb file.dist(j)];
            if isstr(file.ZinLeadPhaseBW(j))
                ZinLeadPhaseBWb = [ZinLeadPhaseBWb NaN];    
            else
                ZinLeadPhaseBWb = [ZinLeadPhaseBWb file.ZinLeadPhaseBW(j)];
            end
        end
    end
end
pname = paths{3};
list = dir(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/'));
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat('~/Documents/Repos/L5PYR_Resonance/Kole/Vary_Global_Gs/',pname,'/',list(i).name));
        for j = 1:length(file.dist)
            distc = [distc file.dist(j)];
            if isstr(file.ZinLeadPhaseBW(j))
                ZinLeadPhaseBWc = [ZinLeadPhaseBWc NaN];    
            else
                ZinLeadPhaseBWc = [ZinLeadPhaseBWc file.ZinLeadPhaseBW(j)];
            end
        end
    end
end
subplot(2,3,6)
p1 = scatter(dista, ZinLeadPhaseBWa, 'b');
hold on 
p2 = scatter(distb, ZinLeadPhaseBWb, 'g');
p3 = scatter(distc, ZinLeadPhaseBWc, 'r');
ylabel('Leading Phase Bandwidth (Hz)')
set(gca, 'FontSize', 14)