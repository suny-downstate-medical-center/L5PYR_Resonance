function inputImpedanceSingleCell(path_name, fig_name)

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
ZinLeadPhaseBool = [];
dendType = []; % 0 - basal, 1 - trunk, 2 - obl, 3 - tuft

% trunks = [0, 2, 3, 4, 5, 6, 7];
% tufts = 8:32;
% obls = [1, 33:44];
trunks = 0:5;
obls = 6:78;
tufts = 79:108;


% load in data from sim output files
list = dir(path_name);
count = 1;

for i = 1:length(list)
    if ~list(i).isdir
        file = load(strcat(path_name,list(i).name));
        
%         if strcmp(list(i).name(1:5), 'basal')
        str1 = strsplit(list(i).name,'.');
        str2 = char(str1(2));
        if strcmp(str2(1:4), 'dend')
            type = 0;
        else
%             spl1 = strsplit(list(i).name,'[');
            spl1 = str1;
            spl2 = strsplit(spl1{2}, '[');
            spl3 = strsplit(spl2{2},']');
%             dendInd = str2num(char(spl2(1)));
            dendInd = str2num(char(spl3));
            
            if any(trunks == dendInd)
                type = 1;
            elseif any(obls == dendInd)
                type = 2;
            else
                type = 3;
            end
        end            
        
        for j = 1:length(file.dist)
            dist = [dist file.dist(j)];
            fVarIn = [fVarIn file.fVarIn(j)];
            QfactorIn = [QfactorIn file.QfactorIn(j)];
            ZinResAmp = [ZinResAmp file.ZinResAmp(j)];
            ZinResFreq = [ZinResFreq file.ZinResFreq(j)];
            ZinLeadPhaseBool(count,:) = file.ZinLeadPhaseBool(j,:);
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
            dendType = [dendType type];
            count = count + 1;
        end
    end
end
clear file

figure()
hold on
set(gca, 'Visible', 'off')
for i = 1:length(dist)
    if dendType(i) == 0
        scatter(dist(i), ZinResFreq(i), 'b')
    elseif dendType(i) == 1
        scatter(dist(i), ZinResFreq(i), 'r')
    elseif dendType(i) == 2
        scatter(dist(i), ZinResFreq(i), 'g')
    elseif dendType(i) == 3
        scatter(dist(i), ZinResFreq(i), 'm')
    end
end
set(gca, 'Visible','on')

figure()
hold on
set(gca, 'Visible', 'off')
for i = 1:length(dist)
    if dendType(i) == 0
        scatter(dist(i), ZcResFreq(i), 'b')
    elseif dendType(i) == 1
        scatter(dist(i), ZcResFreq(i), 'r')
    elseif dendType(i) == 2
        scatter(dist(i), ZcResFreq(i), 'g')
    elseif dendType(i) == 3
        scatter(dist(i), ZcResFreq(i), 'm')
    end
end
set(gca, 'Visible','on')

% % plot

% fig = figure('units','normalized','outerposition',[0 0 1 1]);%,'visible','off');
% subplot(2,3,1)
% scatter(dist, ZinResAmp ./ max(ZinResAmp), 'k' ,'o')
% ylabel('Normalized Resonance Amplitude')
% set(gca, 'FontSize', 14)
% subplot(2,3,2)
% scatter(dist, ZinResFreq, 'k', 'o')
% ylabel('Resonance Frequency (Hz)')
% set(gca, 'FontSize', 14)
% subplot(2,3,3)
% scatter(dist, QfactorIn, 'k', 'o')
% ylabel('Resonance Strength (Q-factor)')
% set(gca, 'FontSize', 14)
% subplot(2,3,4)
% try
%     scatter(dist, ZcResFreq, 'k', 'o')
% catch
%     scatter(dist, cell2mat(ZcResFreq), 'k', 'o')
% end
% ylabel('Transfer Frequency (Hz)')
% set(gca, 'FontSize', 14)
% subplot(2,3,5)
% try
%     scatter(dist, ZinSynchFreq, 'k', 'o')
% catch
%     scatter(dist, cell2mat(ZinSynchFreq), 'k', 'o')
% end
% xlabel('Distance to Soma (\mum)')
% ylabel('Synchronous Frequency (Hz)')
% set(gca, 'FontSize', 14)
% subplot(2,3,6)
% try
%     scatter(dist, ZinLeadPhaseBW, 'k', 'o')
% catch
%     for j = 1:length(ZinLeadPhaseBW)
%         scatter(dist(j), ZinLeadPhaseBW{j}, 'k', 'o')
%         hold on
%     end
% end
% ylabel('Leading Phase Bandwidth (Hz)')
% set(gca, 'FontSize', 14)
% % 
% % saveas(fig, strcat(fig_name,'.png'))
% % saveas(fig, strcat(fig_name,'.fig'))
% 
% end