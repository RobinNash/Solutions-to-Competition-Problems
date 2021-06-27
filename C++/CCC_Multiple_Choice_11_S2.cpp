//CCC Multiple Choice 11 S2
//August 17, 2019
//By Robin Nash

#include<iostream>
#include <vector>

using namespace std;

int main(){
	
	int n;
	scanf("%d", &n);
	
	vector<char> answers1;
	vector<char> answers2;
	
	for (int i=0; i<2;i++){
		for (int j=0;j<n;j++){
			char ch;
			cin >> ch; 
			(i == 0) ? answers1.push_back(ch) : answers2.push_back(ch);
			
		}
	}
	
	int total = 0;
	for (int i=0;i<n;i++){
		total += (answers1[i] == answers2[i]) ? 1 : 0;
	}
	
	cout << total;
		
	return 0;
}
//1566080686.0