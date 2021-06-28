//CCC Pattern Generator 96 S1
//August 21, 2019
//By Robin Nash

#include<iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector <string> getBit(int bits, int ones, string pattern, vector<string> patterns){
	
	if (pattern.length() < bits){
		if (count(pattern.begin(),pattern.end(),'1') < ones)
			getBit(bits, ones, pattern + "1", patterns);
		getBit(bits, ones, pattern + "0", patterns);
	}
	else{
		if (count(pattern.begin(), pattern.end(), '1') == ones){
			patterns.push_back(pattern);
		}
	}
	for (string pattern : patterns){
		cout << pattern << endl;

	}
	
	return patterns; // doesnt work :( 
	
}



int main(){

	vector <string> patterns;
	int n;
	scanf("%d", &n);
	for (int i =0; i < n; i++){
		int bits, ones;
		//scanf("%d %d\n", &bits, &ones);
		cin >> bits >> ones;
		printf("%s\n", "The bit patterns are");
		getBit(bits, ones, "", {});
		cout << endl;
	}
	
	
		
	return 0;
}

//1566358652.0