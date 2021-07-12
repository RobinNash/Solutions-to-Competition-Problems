//CCC Cell- Phone Messaging 06 J3
//August 27, 2019
//By Robin Nash

#include<iostream>
#include<vector>
#include<string>
using namespace std;


int main(){
	
	vector<string> keys {"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};

	while (true){
		string word;
		getline(cin,word);
		if (word == "halt")
			break;
		
		int seconds = 0;
		int prevPos = -1;
		for (char ch : word){
			for (int i =0; i < keys.size(); i++){
				size_t pos = keys.at(i).find(ch);
				if (pos != string::npos){
					seconds+=pos+1;
					if (prevPos == i)
						seconds+=2;
					prevPos = i;
					break;
				}
			}
		}
		cout << seconds << endl;

		
	}
		
	return 0;
}

//1566864734.0