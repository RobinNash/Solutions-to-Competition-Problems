//CCC Big Bang Secrets 12 J4
//July 18, 2019
//By Robin Nash

#include <iostream>
#include <string>

using namespace std;

int main(){
	
	string alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	string code;
	int s, k;

	
	//scanf("%d", k);
	cin >> k;
	cin >> code;
	//scanf("%s", code);
	
	for (int i=1; i<code.length()+1; i++){
		s = 3*i + k;
		char ch = code.at(i-1);
		s = (alpha.find(ch) - s);
		while (s<0){
			s+=26;
		}
		printf("%c", alpha.at(s));
		
	}
	
	
	
	
	return 0;
}
//1563479096.0