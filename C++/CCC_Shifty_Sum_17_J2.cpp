//CCC Shifty Sum 17 J2
//August 16, 2019
//By Robin Nash

#include <iostream>

using namespace std;

int main(){
	
	int n, shifts;
	
	scanf("%d", &n);
	scanf("%d", &shifts);
	
	int total = n;
	
	for (int i=0;i<shifts;i++){
		n*=10;
		total += n;
	}
	
	printf("%d", total);
	

	return 0;
}
//1565998146.0