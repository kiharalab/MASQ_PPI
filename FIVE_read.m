% Contributors: Prof. Daisuke Kihara, Ziyun Ding, Xi He, Zixuan Liu
% Lab HomePage: http://www.kiharalab.org/
% License: GNU LGPLv3
% https://www.gnu.org/licenses/gpl-3.0.en.html

function read();
%input path need to be changed
fileID = fopen('input_path','r');
tline = fgetl(fileID);
C = strsplit(tline,',');
proteinA = regexprep(char(C(1)),'[^\w'']','');
proteinB = regexprep(char(C(2)),'[^\w'']','');
Predict_PPI(proteinA,proteinB);
while ischar(tline)
    tline = fgetl(fileID)
    C = strsplit(tline,',');
    proteinA = regexprep(char(C(1)),'[^\w'']','');
    proteinB = regexprep(char(C(2)),'[^\w'']','');
    Predict_PPI(proteinA,proteinB, output_path);
end

fclose(fileID);
end


function Predict_PPI(proteinA,proteinB);
% proteinA and proteinB are two protein sequences for a protein pair AB
OriginData = dlmread('Descriptors.csv',',');
% property.csv is the file for listing the normalized values of seven descriptors of amino acids.
OriginData = OriginData';
AAindex = 'ACDEFGHIKLMNPQRSTVWY';
Pse=[];
L1=length(proteinA); 
L2=length(proteinB);
AAnum1= [];
AAnum2= [];
for i=1:L1
AAnum1 = [AAnum1,OriginData(:,findstr(AAindex,proteinA(i)))];
end
for i=1:L2
AAnum2 = [AAnum2,OriginData(:,findstr(AAindex,proteinB(i)))];
end
Matrix1=[];
Matrix2=[];
for i=1:7
    t1=zeros(1,30);
    t2=zeros(1,30);
    for j=1:30
        for k=1:(L1-j)
           J=(AAnum1(i,k)-sum(AAnum1(i,:)/L1))*(AAnum1(i,(k+j))-sum(AAnum1(i,:)/L1));
            t1(j)=t1(j)+J;
        end
        for k=1:(L2-j)
           J=(AAnum2(i,k)-sum(AAnum2(i,:)/L2))*(AAnum2(i,(k+j))-sum(AAnum2(i,:)/L2));
            t2(j)=t2(j)+J;
        end
        t1(j)=t1(j)/(L1-j);
        t2(j)=t2(j)/(L2-j);
     end
       Matrix1=[Matrix1,t1];
       Matrix2=[Matrix2,t2];
end
Matrix=[0,Matrix1,Matrix2];
L=length(Matrix);
%output path need to be changed
fid=fopen('output_path','a+');
fprintf(fid,'\n');
% proteinAB.txt: the vector of the protein pair AB are listed in this file for further predicting using SVM. This is the format required by libSVM.
for i=1:L
    if i==1
        fprintf(fid,'%3d',Matrix(i));
    else
    fprintf(fid,'\t%d',(i-1));fprintf(fid,':');fprintf(fid,'%f',Matrix(i));
    end
end
fclose(fid);
end
