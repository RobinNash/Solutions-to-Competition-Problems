//CCC Aromatic Numbers 12 S2
//August 06, 2019
//By Robin Nash

#include<iostream>
#include<string>
#include<map>
#include<vector>

using namespace std;

int main(){
	
	string line;
	getline(cin, line);
	//line = "2I3I2X9V1X";
	
	string bases = "IVXLCDM";
	vector<int> numbers{1,5,10,50,100,500,1000};
	map<char, int> roman;
	for(int i=0; i<7; i++){
		char n = bases.at(i);
		roman[n] = numbers.at(i);
	}
	


	
	int total = 0;
	for (int i=0;i<line.length();i+=2){
		int x = line.at(i) - '0';
		char a, b;
		a = line.at(i+1);
		
		
		if(i+3 > line.length()){
			total += x * roman[a];
			break;
		}
			
		b = line.at(i+3);
		
		
		if (roman[b] > roman[a])
			total -= x * roman[a];
		else
			total += x * roman[a];
		


	}
	char a = '3';
	int b = a - '0';
	
	
	
	printf("%d%", total);
	
		
	return 0;
}
//1565124334.0