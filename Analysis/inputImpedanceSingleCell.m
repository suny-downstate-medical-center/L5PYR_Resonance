function inputImpedanceSingleCell(path_name)

% allocate space for variables
dist = [];
fVarIn = [];
QfactorIn = [];
ZinResAmp = [];
ZinResFreq = [];
ZinSynchFreq = [];
ZinPeakPhaseFreq = [];
ZinLeadPhaseMinFreq =[];
ZinLeadPhaseBW = [];
ZcResFreq = [];

% load in data from sim output files
list = dir(path_name);
for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat(path_name,list(i).name));
        for j = 1:length(file.dist)
            dist = [dist file.dist(j)];
            fVarIn = [fVarIn file.fVarIn(j)];
            QfactorIn = [QfactorIn file.QfactorIn(j)];
            ZinResAmp = [ZinResAmp file.ZinResAmp(j)];
            ZinResFreq = [ZinResFreq file.ZinResFreq(j)];
            if isstr(file.ZinSynchFreq(j))
                ZinSynchFreq = [ZinSynchFreq NaN];    
            else
                ZinSynchFreq = [ZinSynchFreq file.ZinSynchFreq(j)];
            end
            if isstr(ZinLeadPhaseBW)
                ZinLeadPhaseBW  = [ZinLeadPhaseBW  NaN];
            else
                ZinLeadPhaseBW  = [ZinLeadPhaseBW  file.ZinLeadPhaseBW(j)];
            end
            ZcResFreq =  [ZcResFreq file.ZcResFreq(j)];
        end
    end
end
clear file

% plot
figure('units','normalized','outerposition',[0 0 1 1]);
subplot(2,3,1)
scatter(dist, ZinResAmp ./ max(ZinResAmp), 'k' ,'o')
ylabel('Normalized Resonance Amplitude')
set(gca, 'FontSize', 14)
subplot(2,3,2)
scatter(dist, ZinResFreq, 'k', 'o')
ylabel('Resonance Frequency (Hz)')
set(gca, 'FontSize', 14)
subplot(2,3,3)
scatter(dist, QfactorIn, 'k', 'o')
ylabel('Resonance Strength (Q-factor)')
set(gca, 'FontSize', 14)
subplot(2,3,4)
try
    scatter(dist, ZcResFreq, 'k', 'o')
catch
    scatter(dist, cell2mat(ZcResFreq), 'k', 'o')
end
ylabel('Transfer Frequency (Hz)')
set(gca, 'FontSize', 14)
subplot(2,3,5)
try
    scatter(dist, ZinSynchFreq, 'k', 'o')
catch
    scatter(dist, cell2mat(ZinSynchFreq), 'k', 'o')
end
xlabel('Distance to Soma (\mum)')
ylabel('Synchronous Frequency (Hz)')
set(gca, 'FontSize', 14)
subplot(2,3,6)
try
    scatter(dist, ZinLeadPhaseBW, 'k', 'o')
catch
    for j = 1:length(ZinLeadPhaseBW)
        scatter(dist(j), ZinLeadPhaseBW{j}, 'k', 'o')
        hold on
    end
end
ylabel('Leading Phase Bandwidth (Hz)')
set(gca, 'FontSize', 14)

end