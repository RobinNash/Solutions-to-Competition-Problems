//CCC G P S Text Entry 08 J3
//August 06, 2019
//By Robin Nash

#include<iostream>
#include<string>
#include<vector>
#include<typeinfo>

using namespace std;

int main(){
	string text = "A";
	string input;
	getline(cin,input);
	text+=input;
	text+="*";
	
	vector<string> keypad{"ABCDEF", "GHIJKL", "MNOPQR", "STUVWX", "YZ -.*"};
	
	int total = 0;
	for (int i=0;i<text.length()-1;i++){
		string a, b;
		a = text.at(i);
		b = text.at(i+1);
		
		int aLine, bLine, apos, bpos;
		aLine = 0;
		for(;aLine<5;aLine++){
			string line = keypad.at(aLine);
			size_t found = line.find(a);
			
			if (found!=string::npos){
				apos = line.find(a);
				break;
			}
		}
		
		bLine = 0;
		for (;bLine<5;bLine++){
			string line = keypad.at(bLine);
			size_t found = line.find(b);
			if (found!=string::npos){
				bpos = line.find(b);
				break;
			}
		}
		
		if (aLine > bLine)
			total += aLine-bLine;
		else
			total += bLine-aLine;
		
		if (bpos > apos)
			total += bpos-apos;
		else
			total += apos-bpos;
	}
	
	printf("%d", total);
	
	
	return 0;
}
//1565129330.0